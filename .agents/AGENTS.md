# LLM Wiki Project Rules

When working in this workspace, follow these rules regarding the LLM Wiki:

1. **Wiki Structure**: The wiki is encapsulated in the `LLM_Wiki_Project` folder.
   - `LLM_Wiki_Project/raw/`: Contains raw sources and `assets/` for downloaded images. Never modify these raw sources; they are immutable.
   - `LLM_Wiki_Project/wiki/`: Contains all LLM-generated markdown files, including `index.md` (catalog), `log.md` (chronological record), and `overview.md` (high-level synthesis).
   - `LLM_Wiki_Project/templates/`: Contains templates (`Entity.md`, `Concept.md`, `Summary.md`).
   - `LLM_Wiki_Project/scripts/`: Contains python scripts like `ingestor.py` and `linter.py`.

2. **Page Frontmatter (Schema Integrity)**: All generated wiki content pages MUST include the following YAML frontmatter fields:
   - `type` (must be one of: `summary`, `entity`, `concept`, `overview`)
   - `title`
   - `description`
   - `tags` (array)
   - `timestamp`
   - `sources` (array)

3. **Operations**:
   - **Commands**: The major LLM Wiki operations are now handled by trigger-matched skills located in `.agents/skills/`.
     - **`/ingest`**: Reads raw sources and formats them into wiki pages.
     - **`/query`**: Strictly queries the local Knowledge Base (`wiki/index.md`).
     - **`/lint`**: Runs a comprehensive 6-step health check on the wiki.
     - **`/ask`**: General conversation mode.
   - **GitHub Automation**: After successfully performing any operation that modifies the wiki (such as Ingest or Query updates), automatically run `git add .`, `git commit -m "[Auto] ..."`, and `git push origin main` to keep the remote repository synchronized.
