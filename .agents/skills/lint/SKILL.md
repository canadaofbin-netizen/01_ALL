---
name: lint
description: Triggers when the user uses `/lint`. Runs a comprehensive 6-step health check on the LLM Wiki.
---

# Lint Protocol

When the user types `/lint`, run a comprehensive health check on `LLM_Wiki_Project/wiki/`. 
Do NOT unilaterally delete or heavily modify content pages. You may only repair unambiguous frontmatter syntax.

Execute these 6 steps in order:
1. **Schema Integrity**: Check all files for the required frontmatter (`type`, `title`, `description`, `tags`, `timestamp`, `sources`). Flag missing ones.
2. **Staleness**: Identify the oldest pages (by timestamp) and cross-reference with newer pages to flag potential contradictions.
3. **Coverage Gaps**: Look for `[[Wikilinks]]` in the text that point to files that do not exist yet.
4. **Overview Drift**: Check if `overview.md` is missing major recent concepts.
5. **Orphans**: Find pages that have zero incoming links from other pages.
6. **Duplicates**: Flag files with very similar names or overlapping content.

After scanning, compile the results into a report in `LLM_Wiki_Project/wiki/log.md` and present a concise summary to the user.
