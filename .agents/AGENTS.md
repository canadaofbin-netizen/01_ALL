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
   - **Ingest (via `/ingest` command)**: Automatically read the latest raw sources, generate corresponding pages in `wiki/`, update `wiki/index.md` to reflect new pages, and append an entry to `wiki/log.md`.
   - **Chat (via `/ask` command)**: General conversation mode. Respond using general knowledge or standard assistance.
   - **Query (via `/query` command)**: Strictly query the Wiki's Knowledge Base. Search `wiki/index.md` first to find relevant context, synthesize an answer based ONLY on the wiki, and optionally file the answer back as a new page.
   - **Lint (via `/lint` command)**: Run a 6-step health check referring to `LLM_Wiki_Project/Wiki_Linter_Prompt.md`. Do NOT unilaterally delete duplicate or orphan files; only flag them for the user. Do NOT create or edit content pages during a lint pass. Log the lint pass to `wiki/log.md`.
   - **GitHub Automation**: After successfully performing any operation that modifies the wiki (such as Ingest or Query updates), automatically run `git add .`, `git commit -m "[Auto] ..."`, and `git push origin main` to keep the remote repository synchronized.
