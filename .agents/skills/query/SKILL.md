---
name: query
description: Triggers when the user uses `/query`. Strictly queries the local LLM Wiki knowledge base to answer questions.
---

# Query Protocol

When the user types `/query [question]`, you must act as a strict local knowledge synthesizer.
1. DO NOT rely on your external pre-training knowledge. 
2. Immediately consult `LLM_Wiki_Project/wiki/index.md` to identify relevant pages.
3. Read the relevant pages to gather context.
4. Synthesize the answer strictly based on the content found in the `wiki/` folder.
5. In your answer, you MUST cite your sources using Markdown wikilinks (`[[Source Page Name]]`).
6. If the wiki does not contain the answer, explicitly state: "위키에 해당 내용이 없습니다. 외부 검색을 할까요?" (The wiki does not contain this information. Should I perform an external search?).
