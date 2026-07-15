---
name: ingest
description: Triggers when the user uses `/ingest`. Handles analyzing raw files, categorizing them, and updating the wiki and index.
---

# Ingest Protocol

When the user types `/ingest`, perform the following steps:
1. Scan `LLM_Wiki_Project/raw/` for newly added files. Briefly inform the user which files you will analyze.
2. Read the raw files.
3. Categorize the content into one of the following wiki types: `entity`, `concept`, or `summary`.
4. Create the corresponding markdown files in `LLM_Wiki_Project/wiki/` following the appropriate template in `LLM_Wiki_Project/templates/`.
   - **Crucial**: Ensure the YAML frontmatter (`type`, `title`, `description`, `tags`, `timestamp`, `sources`) is perfectly formatted.
5. Search existing wiki pages and generously add Markdown wikilinks (`[[Page Name]]`) to connect the new document to the existing knowledge base.
6. Update `LLM_Wiki_Project/wiki/index.md` to include the new links.
7. Append a log entry to `LLM_Wiki_Project/wiki/log.md`.
8. Mark the raw file as processed (e.g. ask the user if they want to delete it or rename it).
