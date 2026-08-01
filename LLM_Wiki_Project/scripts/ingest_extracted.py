import os
import json
import glob
import re
import datetime
import subprocess
from pathlib import Path

# Paths
BASE_DIR = r"g:\My Drive\UCL\AI Lab\01_ALL\LLM_Wiki_Project"
WIKI_DIR = os.path.join(BASE_DIR, "wiki")
RAW_DIR = os.path.join(BASE_DIR, "raw", "assets")
TEMP_DIR = os.path.join(BASE_DIR, "temp_extractions")
INDEX_FILE = os.path.join(WIKI_DIR, "index.md")
OVERVIEW_FILE = os.path.join(WIKI_DIR, "overview.md")
LOG_FILE = os.path.join(WIKI_DIR, "log.md")

def sanitize_filename(name):
    return re.sub(r'[^\w\-]', '_', name)

def read_frontmatter_and_content(filepath):
    if not os.path.exists(filepath):
        return None, ""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        body = match.group(2)
        fm = {}
        for line in fm_text.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip()
                if val.startswith('[') and val.endswith(']'):
                    val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',') if v.strip()]
                else:
                    val = val.strip('"').strip("'")
                fm[key] = val
        return fm, body
    return {}, content

def write_page(filepath, frontmatter, body):
    fm_lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, list):
            v_str = "[" + ", ".join(f'"{item}"' for item in v) + "]"
            fm_lines.append(f"{k}: {v_str}")
        else:
            fm_lines.append(f'{k}: "{v}"')
    fm_lines.append("---")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(fm_lines) + "\n" + body)

def update_or_create_page(title, p_type, description, claims, source_file, tags):
    filename = sanitize_filename(title) + ".md"
    filepath = os.path.join(WIKI_DIR, filename)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    fm, body = read_frontmatter_and_content(filepath)
    is_new = not bool(fm)
    
    if is_new:
        fm = {
            "title": title,
            "description": description,
            "type": p_type,
            "tags": tags,
            "timestamp": today,
            "sources": [source_file]
        }
        body = f"# {title}\n\n{description}\n\n## Information\n"
    else:
        if "sources" not in fm:
            fm["sources"] = []
        if isinstance(fm["sources"], str):
            fm["sources"] = [fm["sources"]]
        if source_file not in fm["sources"]:
            fm["sources"].append(source_file)
            
        if "tags" not in fm:
            fm["tags"] = []
        if isinstance(fm["tags"], str):
            fm["tags"] = [fm["tags"]]
        for t in tags:
            if t not in fm["tags"]:
                fm["tags"].append(t)
        
        fm["timestamp"] = today

    if claims:
        body += f"\n### Added from [[{source_file}]] on {today}\n"
        for claim in claims:
            body += f"- {claim} ([{source_file}])\n"

    write_page(filepath, fm, body)
    return is_new, filename

def update_index(new_pages):
    if not new_pages: return
    with open(INDEX_FILE, 'a', encoding='utf-8') as f:
        f.write("\n\n### Newly Added\n")
        for p in new_pages:
            f.write(f"- [[{p['title']}]] ({p['type']})\n")
            
    with open(OVERVIEW_FILE, 'a', encoding='utf-8') as f:
        f.write("\n\n### Recent Additions\n")
        for p in new_pages:
            f.write(f"- [[{p['title']}]] ({p['type']})\n")

def process_extractions():
    json_files = glob.glob(os.path.join(TEMP_DIR, "*.json"))
    new_pages = []
    processed_count = 0
    
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        today_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_f.write(f"\n\n## Ingest Log - {today_str}\n")
        
        for jf in json_files:
            with open(jf, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except:
                    continue
            
            source_file = data.get("source_file", os.path.basename(jf).replace(".json", ""))
            entities = data.get("entities", [])
            concepts = data.get("concepts", [])
            claims = data.get("claims", [])
            summary = data.get("summary", "")
            
            # Create summary page
            summary_title = source_file
            is_new, fname = update_or_create_page(summary_title, "summary", summary, claims, source_file, ["source"])
            if is_new:
                new_pages.append({"title": summary_title, "type": "summary"})
            
            # Create entities
            for ent in entities:
                ent_name = ent.get("name", "")
                ent_desc = ent.get("description", "")
                if not ent_name: continue
                is_new, fname = update_or_create_page(ent_name, "entity", ent_desc, [], source_file, ["entity"])
                if is_new:
                    new_pages.append({"title": ent_name, "type": "entity"})
                    
            # Create concepts
            for con in concepts:
                con_name = con.get("name", "")
                con_desc = con.get("description", "")
                if not con_name: continue
                is_new, fname = update_or_create_page(con_name, "concept", con_desc, [], source_file, ["concept"])
                if is_new:
                    new_pages.append({"title": con_name, "type": "concept"})
                    
            log_f.write(f"- Processed `{source_file}`: created/updated {len(entities)} entities and {len(concepts)} concepts.\n")
            
            # Rename raw file to _processed
            possible_raw = [
                os.path.join(RAW_DIR, source_file),
                os.path.join(RAW_DIR, os.path.basename(jf).replace(".json", ".pdf")),
                os.path.join(RAW_DIR, os.path.basename(jf).replace(".json", ".txt"))
            ]
            for rp in possible_raw:
                if os.path.exists(rp) and not "_processed" in rp:
                    base, ext = os.path.splitext(rp)
                    os.rename(rp, base + "_processed" + ext)
                    break
            
            processed_count += 1
            
    update_index(new_pages)
    
    # Git sync
    try:
        subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "commit", "-m", "[Auto] Ingest pipeline completed"], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
    except Exception as e:
        print(f"Git sync error: {e}")

if __name__ == "__main__":
    process_extractions()
    print("Ingestion complete.")
