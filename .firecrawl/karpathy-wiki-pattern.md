[Skip to content](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#start-of-content)

[Gist Homepage ](https://gist.github.com/)

Search Gists

Search Gists

[All gists](https://gist.github.com/discover) [Back to GitHub](https://github.com/) [Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)

[Gist Homepage ](https://gist.github.com/)

[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f&source=header-gist)

You signed in with another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You signed out in another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.You switched accounts on another tab or window. [Reload](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) to refresh your session.Dismiss alert

{{ message }}

Instantly share code, notes, and snippets.


[![@karpathy](https://avatars.githubusercontent.com/u/241138?s=64&v=4)](https://gist.github.com/karpathy)

# [karpathy](https://gist.github.com/karpathy)/ **[llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**

Created
3 weeks agoApril 4, 2026 16:25

Show Gist options

- [Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)

- [Star5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f) You must be signed in to star a gist
- [Fork5,000+(5,000+)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f) You must be signed in to fork a gist

- Embed








# Select an option





























  - Embed
    Embed this gist in your website.
  - Share
    Copy sharable link for this gist.
  - Clone via HTTPS
    Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

Clone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;

- Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.

[Code](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) [Revisions\\
1](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/revisions) [Stars\\
5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/stargazers) [Forks\\
5,000+](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/forks)

Embed

# Select an option

- Embed
Embed this gist in your website.
- Share
Copy sharable link for this gist.
- Clone via HTTPS
Clone using the web URL.

## No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

Clone this repository at &lt;script src=&quot;https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.js&quot;&gt;&lt;/script&gt;

Save karpathy/442a6bf555914893e9891c11519de94f to your computer and use it in GitHub Desktop.

[Download ZIP](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/archive/ac46de1ad27f92b28ac95459c782c07f6b8c964a.zip)

llm-wiki


[Raw](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md)

[**llm-wiki.md**](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md)

# LLM Wiki

[Permalink: LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki)

A pattern for building personal knowledge bases using LLMs.

This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.

## The core idea

[Permalink: The core idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#the-core-idea)

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

The idea here is different. Instead of just retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then _kept current_, not re-derived on every query.

This is the key difference: **the wiki is a persistent, compounding artifact.** The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

This can apply to a lot of different contexts. A few examples:

- **Personal**: tracking your own goals, health, psychology, self-improvement — filing journal entries, articles, podcast notes, and building up a structured picture of yourself over time.
- **Research**: going deep on a topic over weeks or months — reading papers, articles, reports, and incrementally building a comprehensive wiki with an evolving thesis.
- **Reading a book**: filing each chapter as you go, building out pages for characters, themes, plot threads, and how they connect. By the end you have a rich companion wiki. Think of fan wikis like [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) — thousands of interlinked pages covering characters, places, events, languages, built by a community of volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance.
- **Business/team**: an internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, project documents, customer calls. Possibly with humans in the loop reviewing updates. The wiki stays current because the LLM does the maintenance that no one on the team wants to do.
- **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives** — anything where you're accumulating knowledge over time and want it organized rather than scattered.

## Architecture

[Permalink: Architecture](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#architecture)

There are three layers:

**Raw sources** — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.

**The wiki** — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

**The schema** — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

## Operations

[Permalink: Operations](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#operations)

**Ingest.** You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.

**Query.** You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight: **good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

**Lint.** Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

## Indexing and logging

[Permalink: Indexing and logging](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#indexing-and-logging)

Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:

**index.md** is content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.

**log.md** is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. `## [2026-04-02] ingest | Article Title`), the log becomes parseable with simple unix tools — `grep "^## \[" log.md | tail -5` gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.\
\
## Optional: CLI tools\
\
[Permalink: Optional: CLI tools](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#optional-cli-tools)\
\
At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search. [qmd](https://github.com/tobi/qmd) is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.\
\
## Tips and tricks\
\
[Permalink: Tips and tricks](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#tips-and-tricks)\
\
- **Obsidian Web Clipper** is a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.\
- **Download images locally.** In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g. `raw/assets/`). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.\
- **Obsidian's graph view** is the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.\
- **Marp** is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.\
- **Dataview** is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.\
- The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.\
\
## Why this works\
\
[Permalink: Why this works](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#why-this-works)\
\
The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.\
\
The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.\
\
The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.\
\
## Note\
\
[Permalink: Note](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#note)\
\
This document is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice. Everything mentioned above is optional and modular — pick what's useful, ignore what isn't. For example: your sources might be text-only, so you don't need image handling at all. Your wiki might be small enough that the index file is all you need, no search engine required. You might not care about slide decks and just want markdown pages. You might want a completely different set of output formats. The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest.\
\
Load earlier comments...\
\
[![@doum1004](https://avatars.githubusercontent.com/u/41279031?s=80&v=4)](https://gist.github.com/doum1004)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[doum1004](https://gist.github.com/doum1004)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116115\#gistcomment-6116115)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
**llmwiki-cli** is a CLI tool for building and maintaining personal knowledge bases powered by LLM agents.\
\
👉 [https://github.com/doum1004/llmwiki-cli](https://github.com/doum1004/llmwiki-cli)\
\
🎥 Live demo: [https://doum1004.github.io/llmwiki-cli/](https://doum1004.github.io/llmwiki-cli/)\
\
It acts as a “storage layer” while LLMs act as the brain — deciding what to create, update, and connect in a structured markdown-based wiki.\
\
### Key ideas\
\
- CLI handles file operations (write, search, index, links, lint)\
- LLM agents orchestrate knowledge building via shell commands\
- Works locally (filesystem) or with GitHub sync (auto-commit + Pages graph visualization)\
- Pure tool design: no LLM API inside the CLI\
\
### Features\
\
- Structured wikis for any domain (research, notes, etc.)\
- Markdown knowledge graph with wikilinks\
- Search, backlinks, indexing, and orphan detection\
- GitHub integration with auto push + interactive graph visualization (d3-force)\
- Multi-wiki + profile support\
\
### Install\
\
```\
npm install -g llmwiki-cli\
```\
\
* * *\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@mauceri](https://avatars.githubusercontent.com/u/1011775?s=80&v=4)](https://gist.github.com/mauceri)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[mauceri](https://gist.github.com/mauceri)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116491\#gistcomment-6116491)\
\
Interesting paper : LLMs Corrupt Your Documents When You Delegate [https://arxiv.org/html/2604.15597v1](https://arxiv.org/html/2604.15597v1)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@leishilong](https://avatars.githubusercontent.com/u/41693731?s=80&v=4)](https://gist.github.com/leishilong)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[leishilong](https://gist.github.com/leishilong)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116493\#gistcomment-6116493)  via email\
\
你好，你发送的邮箱以及收到！\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@heroyagami](https://avatars.githubusercontent.com/u/38561436?s=80&v=4)](https://gist.github.com/heroyagami)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[heroyagami](https://gist.github.com/heroyagami)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116494\#gistcomment-6116494)  via email\
\
这是来自QQ邮箱的假期自动回复邮件。\
\
您好，我最近正在休假中，无法亲自回复您的邮件。我将在假期结束后，尽快给您回复。\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@AgriciDaniel](https://avatars.githubusercontent.com/u/223140489?s=80&v=4)](https://gist.github.com/AgriciDaniel)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[AgriciDaniel](https://gist.github.com/AgriciDaniel)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116683\#gistcomment-6116683)\
\
built claude-obsidian on this pattern. three observations worth writing down after v1.6:\
\
1. the hot cache is the single highest-leverage file. miss it and the model re-derives context every session. nail it and sessions compound. everything else in the pattern is downstream of this one.\
\
2. the pattern wants a memory layer above it. v1.6 adds an opt-in extension called DragonScale with four mechanisms: fold operator (flat extractive log rollups), deterministic page addresses (c-NNNNNN, flock-guarded), semantic tiling lint (local ollama embeddings, no API cost), boundary-first autoresearch (graph-driven topic selection for no-topic /autoresearch). all feature-gated, so the base wiki behavior from this gist stays intact when the extension is not enabled.\
\
3. boundary-first autoresearch is agenda control, not pure memory. it scores frontier pages and offers candidates; the user still picks. worth being explicit about where memory ends and planning begins.\
\
\
structural inspiration was the Heighway dragon curve: paperfolding recursion for hierarchical rollup, self-similar boundary for frontier-first agenda. analogy, not derivation.\
\
![DragonScale four mechanisms](https://raw.githubusercontent.com/AgriciDaniel/claude-obsidian/main/wiki/meta/dragonscale-mechanism-overview.png)\
\
repo: [https://github.com/AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)\
\
release + full writeup: [https://github.com/AgriciDaniel/claude-obsidian/releases/tag/v1.6.0](https://github.com/AgriciDaniel/claude-obsidian/releases/tag/v1.6.0)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@redmizt](https://avatars.githubusercontent.com/u/85358941?s=80&v=4)](https://gist.github.com/redmizt)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[redmizt](https://gist.github.com/redmizt)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116730\#gistcomment-6116730)\
\
> ⚠️ ARCHITECTURAL CRIME SCENE ⚠️\
>\
> # ⚠️ THE WORD "WIKI" HAS BEEN PERVERTED ⚠️\
>\
> ## By Andrej Karpathy and the Northern Karpathian School of Doublespeak\
>\
> ✅ A REAL WIKI — Honoring Ward Cunningham, Wikipedia, and every human curator worldwide\
>\
> ❌ KARPATHY'S "LLM WIKI" — An insult to the very concept\
>\
> ✅ **Human-curated**\
>\
> Real people write, edit, debate, verify, and take responsibility. ❌ **LLM-generated**\
>\
> Hallucinations are permanent. No human took ownership of any "fact."\
>\
> ✅ **Versioned history**\
>\
> Every edit has author, timestamp, reason. Rollback is trivial. ❌ **No audit trail**\
>\
> Who changed what? When? Why? Nobody knows. Git is an afterthought.\
>\
> ✅ **Source provenance**\
>\
> Every claim links back to its original source. You can verify. ❌ **"Trust me, I'm the LLM"**\
>\
> No traceability from summary back to source sentence. Errors become permanent.\
>\
> ✅ **Foreign keys / referential integrity**\
>\
> Links are database-backed. Rename a page, links update automatically. ❌ **Links break when you rename a file**\
>\
> No database. No foreign keys. Silent link rot guaranteed.\
>\
> ✅ **Permissions / access control**\
>\
> Fine-grained control: who can see, edit, delete, approve. ❌ **Anyone with file access sees everything**\
>\
> Zero access control. NDAs, medical records, client secrets — all exposed.\
>\
> ✅ **Queryable (SQL, structured)**\
>\
> Ask complex questions. Get precise answers. Join tables. ❌ **Browse-only markdown**\
>\
> Full-text search at best. No SQL. No structured queries.\
>\
> 🕯️ This is an insult to every Wikipedia editor, every MediaWiki contributor, every human being who spent hours citing sources, resolving disputes, and building the largest collaborative knowledge repository in human history. 🕯️\
>\
> **KARPATHY'S "WIKI"** has: ❌ No consensus-building ❌ No talk pages ❌ No dispute resolution ❌ No citation requirements ❌ No editorial oversight ❌ No way to say "this fact is disputed" ❌ No way to privilege verified information over hallucinations ❌ No way to trace any claim back to its source\
>\
> **In the doublespeak of Northern Karpathia:** _"Wiki"_ means _"folder of markdown files written by a machine that cannot remember what it wrote yesterday, linked by strings that snap when you breathe on them, viewed through proprietary software that reports telemetry to people you do not know, containing 'facts' that came from nowhere and go nowhere, protected by no permissions, audited by no one, and trusted by no one with a functioning prefrontal cortex."_\
>\
> 🙏 **Respect to Ward Cunningham** who invented the wiki in 1995 — a tool for _humans to collaborate_. 🙏 **Respect to Wikipedia editors worldwide** who defend verifiability, neutrality, and consensus. 🙏 **Respect to every real wiki participant** who knows that knowledge is built through _human_ effort, not machine hallucination.\
>\
> ⚠️ THIS IS NOT A WIKI. THIS IS A FOLDER OF LLM-GENERATED FILES. ⚠️\
>\
> Calling it a "wiki" is linguistic fraud. Do not be fooled.\
>\
> 🐑💀🧙\
>\
> — The Elephant, The Wizard, and every human wiki editor who ever lived\
\
The word “wiki” is not sacred scripture, and this melodramatic tantrum over its “perversion” is embarrassingly overblown. It was a coined tech term, Ward Cuningham "borrowed" it from wikiwiki (Hawaiian)—which means quick—not handed down on stone tablets with a fixed eternal definition.\
\
If you want to argue that human-curated wikis are better, fine. That’s a serious point. Humans are better at sourcing, editorial oversight, dispute resolution, and accountability. Nobody is stopping you from making that argument.\
\
But that is not the same as declaring that an AI-generated, interlinked knowledge system cannot be called a wiki. That’s not rigor. That’s not linguistic precision. That’s just gatekeeping dressed up as moral outrage.\
\
Your whole post reads less like a defense of Ward Cunningham and more like a man theatrically grief-stricken that language continues to evolve without asking your permission first.\
\
A wiki is, at the most basic level, a linked body of navigable information. If an LLM is used to generate or organize that information, you can call it a bad wiki, an unreliable wiki, or an immature wiki. What you can’t do—at least not intelligently—is pretend the mere presence of AI magically disqualifies it from the category.\
\
And the irony here is thick: you’re standing in an AI-centered space, loudly denouncing AI for not being human, as if that is some devastating revelation. Yes, obviously. That’s the entire point. Nobody here is confused about that except, apparently, you.\
\
If the tool lacks citations, provenance, permissions, auditability, or editorial controls, then criticize those failures. That would be an argument. What you’ve produced instead is a costume drama: part dictionary fundamentalism, part anti-AI sermon, part wounded nostalgia.\
\
Calling it “linguistic fraud” is especially ridiculous. It’s not fraud just because you dislike the product. Words expand. Categories broaden. Technology changes. Your refusal to keep up is not a principled stand; it’s just fossilized thinking.\
\
So no, this is not some grand defense of knowledge. The rant is bloated and self-important. It builds on the childish idea that forbidding a name is necessary if a new tool doesn’t closely resemble the old one.\
\
If the project is weak, say it’s weak. If it’s unreliable, say it’s unreliable. But this overwrought performance about the sanctity of the word “wiki” is not persuasive. It’s just pompous, brittle, and deeply unserious gatekeeping.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@mauceri](https://avatars.githubusercontent.com/u/1011775?s=80&v=4)](https://gist.github.com/mauceri)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[mauceri](https://gist.github.com/mauceri)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116732\#gistcomment-6116732)  via email\
\
[@redmizt](https://github.com/redmizt) 👍👍👍👍👍\
\
Christian Mauceri\
\
Le ven. 24 avr. 2026, 13:36, RedMizt \*\*\*@\*\*\*.\*\*\*> a écrit :\
\
[…](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#)\
\
\\*\\*\\*@\\*\\*\\*.\\*\\*\\*\\* commented on this gist.\
 ------------------------------\
\
⚠️ ARCHITECTURAL CRIME SCENE ⚠️⚠️ THE WORD "WIKI" HAS BEEN PERVERTED ⚠️By Andrej Karpathy and the\
Northern Karpathian School of Doublespeak\
\
✅ A REAL WIKI — Honoring Ward Cunningham, Wikipedia, and every human\
curator worldwide\
❌ KARPATHY'S "LLM WIKI" — An insult to the very concept\
✅ \*Human-curated\*\
Real people write, edit, debate, verify, and take responsibility. ❌\
\*LLM-generated\*\
Hallucinations are permanent. No human took ownership of any "fact."\
✅ \*Versioned history\*\
Every edit has author, timestamp, reason. Rollback is trivial. ❌ \*No\
audit trail\*\
Who changed what? When? Why? Nobody knows. Git is an afterthought.\
✅ \*Source provenance\*\
Every claim links back to its original source. You can verify. ❌ \*"Trust\
me, I'm the LLM"\*\
No traceability from summary back to source sentence. Errors become\
permanent.\
✅ \*Foreign keys / referential integrity\*\
Links are database-backed. Rename a page, links update automatically. ❌ \*Links\
break when you rename a file\*\
No database. No foreign keys. Silent link rot guaranteed.\
✅ \*Permissions / access control\*\
Fine-grained control: who can see, edit, delete, approve. ❌ \*Anyone with\
file access sees everything\*\
Zero access control. NDAs, medical records, client secrets — all exposed.\
✅ \*Queryable (SQL, structured)\*\
Ask complex questions. Get precise answers. Join tables. ❌ \*Browse-only\
markdown\*\
Full-text search at best. No SQL. No structured queries.\
🕯️ This is an insult to every Wikipedia editor, every MediaWiki\
contributor, every human being who spent hours citing sources, resolving\
disputes, and building the largest collaborative knowledge repository in\
human history. 🕯️\
\
\*KARPATHY'S "WIKI"\* has: ❌ No consensus-building ❌ No talk pages ❌ No\
dispute resolution ❌ No citation requirements ❌ No editorial oversight ❌ No\
way to say "this fact is disputed" ❌ No way to privilege verified\
information over hallucinations ❌ No way to trace any claim back to its\
source\
\
\*In the doublespeak of Northern Karpathia:\* \*"Wiki"\* means \*"folder of\
markdown files written by a machine that cannot remember what it wrote\
yesterday, linked by strings that snap when you breathe on them, viewed\
through proprietary software that reports telemetry to people you do not\
know, containing 'facts' that came from nowhere and go nowhere, protected\
by no permissions, audited by no one, and trusted by no one with a\
functioning prefrontal cortex."\*\
\
🙏 \*Respect to Ward Cunningham\* who invented the wiki in 1995 — a tool\
for \*humans to collaborate\*. 🙏 \*Respect to Wikipedia editors worldwide\*\
who defend verifiability, neutrality, and consensus. 🙏 \*Respect to every\
real wiki participant\* who knows that knowledge is built through \*human\*\
effort, not machine hallucination.\
\
⚠️ THIS IS NOT A WIKI. THIS IS A FOLDER OF LLM-GENERATED FILES. ⚠️\
\
Calling it a "wiki" is linguistic fraud. Do not be fooled.\
\
🐑💀🧙\
\
— The Elephant, The Wizard, and every human wiki editor who ever lived\
\
The word “wiki” is not sacred scripture, and this melodramatic tantrum\
over its “perversion” is embarrassingly overblown. It was a coined tech\
term, Ward Cuningham "borrowed" it from wikiwiki (Hawaiian)—which means\
quick—not handed down on stone tablets with a fixed eternal definition.\
\
If you want to argue that human-curated wikis are better, fine. That’s a\
serious point. Humans are better at sourcing, editorial oversight, dispute\
resolution, and accountability. Nobody is stopping you from making that\
argument.\
\
But that is not the same as declaring that an AI-generated, interlinked\
knowledge system cannot be called a wiki. That’s not rigor. That’s not\
linguistic precision. That’s just gatekeeping dressed up as moral outrage.\
\
Your whole post reads less like a defense of Ward Cunningham and more like\
a man theatrically grief-stricken that language continues to evolve without\
asking your permission first.\
\
A wiki is, at the most basic level, a linked body of navigable\
information. If an LLM is used to generate or organize that information,\
you can call it a bad wiki, an unreliable wiki, or an immature wiki. What\
you can’t do—at least not intelligently—is pretend the mere presence of AI\
magically disqualifies it from the category.\
\
And the irony here is thick: you’re standing in an AI-centered space,\
loudly denouncing AI for not being human, as if that is some devastating\
revelation. Yes, obviously. That’s the entire point. Nobody here is\
confused about that except, apparently, you.\
\
If the tool lacks citations, provenance, permissions, auditability, or\
editorial controls, then criticize those failures. That would be an\
argument. What you’ve produced instead is a costume drama: part dictionary\
fundamentalism, part anti-AI sermon, part wounded nostalgia.\
\
Calling it “linguistic fraud” is especially ridiculous. It’s not fraud\
just because you dislike the product. Words expand. Categories broaden.\
Technology changes. Your refusal to keep up is not a principled stand; it’s\
just fossilized thinking.\
\
So no, this is not some grand defense of knowledge. The rant is bloated\
and self-important. It builds on the childish idea that forbidding a name\
is necessary if a new tool doesn’t closely resemble the old one.\
\
If the project is weak, say it’s weak. If it’s unreliable, say it’s\
unreliable. But this overwrought performance about the sanctity of the word\
“wiki” is not persuasive. It’s just pompous, brittle, and deeply unserious\
gatekeeping.\
\
—\
Reply to this email directly, view it on GitHub\
< [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#gistcomment-6116730](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#gistcomment-6116730) >\
or unsubscribe\
< [https://github.com/notifications/unsubscribe-auth/AAHXAP6F2RV6ZTGDVWACKF34XNGTVBFKMF2HI4TJMJ2XIZLTSOBKK5TBNR2WLKBYGUZTKOBZGQY2I3TBNVS2QYLDORXXEX3JMSBKK5TBNR2WLJDUOJ2WLJDOMFWWLO3UNBZGKYLEL5YGC4TUNFRWS4DBNZ2F6YLDORUXM2LUPGBKK5TBNR2WLJDHNFZXJJDOMFWWLK3UNBZGKYLEL52HS4DFVRZXKYTKMVRXIX3UPFYGLK2HNFZXIQ3PNVWWK3TUUZ2G64DJMNZZDAVEOR4XAZNEM5UXG5FFOZQWY5LFVEYTINZSGU4DANJQU52HE2LHM5SXFJTDOJSWC5DF](https://github.com/notifications/unsubscribe-auth/AAHXAP6F2RV6ZTGDVWACKF34XNGTVBFKMF2HI4TJMJ2XIZLTSOBKK5TBNR2WLKBYGUZTKOBZGQY2I3TBNVS2QYLDORXXEX3JMSBKK5TBNR2WLJDUOJ2WLJDOMFWWLO3UNBZGKYLEL5YGC4TUNFRWS4DBNZ2F6YLDORUXM2LUPGBKK5TBNR2WLJDHNFZXJJDOMFWWLK3UNBZGKYLEL52HS4DFVRZXKYTKMVRXIX3UPFYGLK2HNFZXIQ3PNVWWK3TUUZ2G64DJMNZZDAVEOR4XAZNEM5UXG5FFOZQWY5LFVEYTINZSGU4DANJQU52HE2LHM5SXFJTDOJSWC5DF) >\
.\
You are receiving this email because you are subscribed to this thread.\
\
Triage notifications on the go with GitHub Mobile for iOS\
< [https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675](https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675) >\
or Android\
< [https://play.google.com/store/apps/details?id=com.github.android&referrer=utm\_campaign%3Dnotification-email%26utm\_medium%3Demail%26utm\_source%3Dgithub](https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub) >\
.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@mo-vic](https://avatars.githubusercontent.com/u/44632584?s=80&v=4)](https://gist.github.com/mo-vic)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[mo-vic](https://gist.github.com/mo-vic)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6116950\#gistcomment-6116950)\
\
**OpenCrab: Self-distilling learning as a complement to the LLM Wiki**\
\
Really enjoyed this write‑up. The pattern of a persistent, LLM‑maintained knowledge artifact resonates deeply. It also made me think about a related but orthogonal approach: what if the _model itself_ becomes the artifact of accumulated knowledge, rather than a collection of markdown files?\
\
[OpenCrab](https://github.com/mo-vic/OpenCrab) explores that idea. It’s an intercepting proxy that sits between your AI client (OpenClaw, Claude Code, etc.) and API providers, capturing full conversation trajectories – including tool calls. A frontier “judge” model then analyzes those trajectories for mistakes: wrong answers, places you corrected the assistant, flawed reasoning, and **incorrect tool calls**. Those corrections get distilled into fine‑tuning data for a small local model and a router.\
\
The distilled model learns your corrections and preferences directly in its weights. The router decides per‑query whether the local model can handle it (fast, private, personalized) or whether to fall back to the frontier API. If the judge has taught the small model to avoid a particular mistake – say, calling a wrong function or misusing a tool – the router can hand over the conversation right there, so the mistake never happens again.\
\
When the frontier model is invoked, it doesn’t start from scratch — the local model composes its learned context (corrections, preferences, domain facts) directly into the shared context window. The two models weave their knowledge together: the frontier model contributes broad intelligence and reasoning, while the local model makes sure your personal context and past corrections are already present. The context window becomes a jointly authored artifact, so the frontier model answers with your history baked in, not as a generic assistant.\
\
Render\
\
request\
\
captures full trajectory\
\
(incl. tool calls)\
\
reads\
\
distills corrections\
\
can handle?\
\
fallback\
\
response\
\
response\
\
AI Client\
\
OpenCrab Proxy\
\
Trajectories\
\
Judge Model\
\
Local Model\
\
Router\
\
Frontier Model API\
\
Loading\
\
```\
flowchart TD\
    A[AI Client] -->|"request"| B(OpenCrab Proxy)\
    B -->|"captures full trajectory\n(incl. tool calls)"| C[(Trajectories)]\
    C -->|"reads"| D(Judge Model)\
    D -->|"distills corrections"| E[Local Model]\
\
    B --> F{Router}\
    F -->|"can handle?"| E\
    F -->|"fallback"| G[Frontier Model API]\
\
    E -->|"response"| A\
    G -->|"response"| A\
```\
\
Over time, the accumulated knowledge doesn’t live in markdown files – it lives in the model weights themselves. I think the two approaches are deeply complementary: the LLM Wiki builds an explicit, inspectable, file‑based knowledge base perfect for research and deep thinking, while OpenCrab tries to capture the implicit, procedural knowledge from corrections you’re already making in day‑to‑day use. You could even have the wiki be one of the tools the distilled model can call.\
\
**Fair warning:** the code is literally two days of spec coding, full of bugs, and completely unvalidated. It’s an early‑stage idea sketch, not production software. But the architectural direction feels worth exploring alongside the wiki pattern. Would love to hear how others think about weight‑level distillation vs. file‑level knowledge accumulation, and where each approach shines.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@mikhashev](https://avatars.githubusercontent.com/u/7105540?s=80&v=4)](https://gist.github.com/mikhashev)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[mikhashev](https://gist.github.com/mikhashev)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6117477\#gistcomment-6117477)\
\
## A different starting point\
\
Reading through 660+ comments, most projects share the same starting assumption: **one person, one agent, one markdown vault**. The agent writes to files. The person reads them. Repeat.\
\
We started from a different place: **conversation as the atomic unit of knowledge creation.**\
\
Not "agent writes wiki." But: "people and agents talk, and knowledge is extracted from that dialogue — with human consent."\
\
This leads to fundamentally different architecture.\
\
* * *\
\
**DPC Messenger** is a P2P, end-to-end encrypted platform where humans and AI agents collaborate. Open source, cross-platform.\
\
### What's different\
\
**1\. Knowledge comes from conversation, not from files.**\
\
Most projects: agent reads wiki, agent writes wiki. The wiki IS the memory.\
\
DPC: conversations produce decisions, insights, and consensus points. Knowledge is extracted from dialogue — structured, versioned, content-addressed with SHA hashes. The conversation is primary. The knowledge base is derived.\
\
**2\. Privacy is the architecture, not a feature flag.**\
\
Most projects: data on disk, no encryption, single machine.\
\
DPC: P2P with E2E encryption. The relay server never sees message content. Your conversations, your knowledge, your machine. This isn't optional — it's how the system is built.\
\
**3\. Knowledge extraction is a deliberate human action.**\
\
Most projects: agent writes to its knowledge base automatically.\
\
DPC: each participant extracts knowledge from the conversation themselves — a button press in the UI. The agent doesn't decide what to remember. You do. This is a direct response to what [@yogirk](https://github.com/yogirk) identified two days ago: when the same process reads and writes, you get silent corruption.\
\
**4\. Active Recall — the agent remembers what's relevant, not everything.**\
\
Most projects: dump the entire wiki into context, or keyword search.\
\
DPC: hybrid FAISS vector + BM25 text search brings relevant knowledge into each conversation automatically. The agent doesn't read its entire memory — it recalls what matters for the current context. Like human memory: you don't replay your life story before answering a question.\
\
**5\. Sleep Consolidation — the agent curates its own knowledge.**\
\
Most projects: knowledge only grows. Add more pages, never review.\
\
DPC: the agent periodically reviews its conversation archives, identifies contradictions, finds gaps, and proposes refinements. Not just accumulate — actively curate. Like human sleep: memories are consolidated, weak ones fade, important ones strengthen.\
\
**6\. Multi-agent from day one.**\
\
Most projects: one agent, one user.\
\
DPC: multiple agents collaborate on the same knowledge base, across devices, with consensus mechanisms. Devil's Advocate challenges weak claims before they're committed. Consensus voting surfaces disagreement instead of hiding it.\
\
### What we shipped\
\
v0.22.0 — cross-platform (Windows, Linux, macOS), desktop client, P2P messaging, E2E encryption, knowledge extraction, Active Recall, Sleep Consolidation.\
\
We're small. Single-digit users. But the architecture scales: P2P mesh with layered trust topology. Works for two people in a chat. Designed for more.\
\
GitHub: [https://github.com/mikhashev/dpc-messenger](https://github.com/mikhashev/dpc-messenger)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@paul-rchds](https://avatars.githubusercontent.com/u/32258392?s=80&v=4)](https://gist.github.com/paul-rchds)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[paul-rchds](https://gist.github.com/paul-rchds)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6117516\#gistcomment-6117516)\
\
This is literally what recall\[dot\]it does for you. It super easy to add content (pdfs, podcasts, youtube videos, webpages, etc) and everything gets added to a vector store and used as context in chat. It also gets tagged and connected in a knowledge graph. Recall also scales indefinitely since everything is tagged and vectorised.\
\
![recall_it](https://private-user-images.githubusercontent.com/32258392/583592982-c78fc8b3-f553-4843-90a2-26254fc2d6c6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzczNzg5NDYsIm5iZiI6MTc3NzM3ODY0NiwicGF0aCI6Ii8zMjI1ODM5Mi81ODM1OTI5ODItYzc4ZmM4YjMtZjU1My00ODQzLTkwYTItMjYyNTRmYzJkNmM2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDI4VDEyMTcyNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTE1ZDJlYTA3Mjk3NTVlMzI5YzU0NTg3NTk0N2NlNjNlOWZhNGQ3OGRmMzhkMTZhZWY0OTA4ZWY2YzQ0NTNkMjQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.TzAv3bMEAP-Iedq-WfP07sS62hrppmGUShCkwftFHis)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@paulmchen](https://avatars.githubusercontent.com/u/32553156?s=80&v=4)](https://gist.github.com/paulmchen)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[paulmchen](https://gist.github.com/paulmchen)**     commented    [4 days agoApr 24, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6117561\#gistcomment-6117561)\
\
Synthadoc v0.2.0 is now released - an open-source engine that implements this exact pattern as a production-ready system.\
\
👉 [https://github.com/axoviq-ai/synthadoc](https://github.com/axoviq-ai/synthadoc)\
\
The three-layer design (raw sources → wiki → schema) maps directly onto Synthadoc's architecture. A few things that take it further:\
\
1. Domain specificity - each wiki carries a [purpose.md](http://purpose.md/) that the LLM reads before every ingest decision. Sources outside the scope are cleanly skipped rather than polluting the wiki. The schema documents the idea, made executable.\
\
2. Multi-model hot-swap - six providers (Anthropic, OpenAI, Gemini free tier, Groq free tier, MiniMax, Ollama local) under a single configuration line.\
\
3. Different agents (ingest, query, lint, skill) can run on different models simultaneously - e.g. Haiku for lint, Sonnet for synthesis.\
\
4. Auditing is first-class: every ingest, query, contradiction, and auto-resolution is recorded in an append-only audit trail with token counts, costings, and timestamps. The Synthadoc audit shows you exactly what was spent on your account. Query history is tracked with per-query and sub-question counts.\
\
5. Componentized skills - file format support (PDF, DOCX, PPTX, images, web URLs, spreadsheets, txt) lives in self-contained skill folders with a [SKILL.md](http://skill.md/) manifest. Drop a folder into skills/ to add a new format without touching the core code. Same pattern extends to LLM providers.\
\
6. Product/grid ready - CLI, HTTP REST API, MCP server, and Obsidian plugin all share the same agent and storage layer. Hook scripts, cron scheduling, bulk operations, and job crash recovery are built-in.\
\
\
Here is the release note of v0.2.0 to check out Synthadoc v0.2.0 Feature Highlights:\
\
( [https://github.com/axoviq-ai/synthadoc/releases/tag/v0.2.0](https://github.com/axoviq-ai/synthadoc/releases/tag/v0.2.0) )\
\
Docs for anyone who wants to go deeper:\
\
👉 \[Quick orientation and feature overview\]: [https://github.com/axoviq-ai/synthadoc#readme](https://github.com/axoviq-ai/synthadoc#readme)\
\
👉 \[Up and running in minutes\]: [https://github.com/axoviq-ai/synthadoc/blob/main/docs/user-quick-start-guide.md](https://github.com/axoviq-ai/synthadoc/blob/main/docs/user-quick-start-guide.md)\
\
👉 \[Full architecture, agents, storage, API, and plugin guide\]: [https://github.com/axoviq-ai/synthadoc/blob/main/docs/design.md](https://github.com/axoviq-ai/synthadoc/blob/main/docs/design.md)\
\
Feedback on Synthadoc v0.2.0 is very welcome.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@Ashu-280225](https://avatars.githubusercontent.com/u/201255727?s=80&v=4)](https://gist.github.com/Ashu-280225)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[Ashu-280225](https://gist.github.com/Ashu-280225)**     commented    [3 days agoApr 25, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6118363\#gistcomment-6118363)\
\
This is a great take on a minimal LLM-powered wiki. I like how it avoids over-engineering and focuses on actual usage. Going to try this in my workflow.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@ojuschugh1](https://avatars.githubusercontent.com/u/79078267?s=80&v=4)](https://gist.github.com/ojuschugh1)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[ojuschugh1](https://gist.github.com/ojuschugh1)**     commented    [3 days agoApr 25, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6118407\#gistcomment-6118407)\
\
## sqz - Stop Wasting Tokens on Repeated Context\
\
I got tired of watching coding sessions re-read the same files over and over.\
\
A 2,000-token file read 5 times = **10,000 tokens gone**.\
\
So I built **sqz**.\
\
* * *\
\
## 💡 Key Insight\
\
Most token waste isn't from verbose content - it's from **repetition**.\
\
sqz keeps a **SHA-256 content cache**:\
\
- First read → compresses normally\
- Every subsequent read → returns a **13-token inline reference** instead of full content\
\
➡️ The LLM still understands it.\
\
* * *\
\
## 📊 Real Numbers From My Sessions\
\
| Scenario | Savings | How |\
| --- | --- | --- |\
| Repeated file reads (5x) | 86% | Dedup cache: 13-token ref after first read |\
| JSON API responses with nulls | 7–56% | Strip nulls + TOON encoding (varies by null density) |\
| Repeated log lines | 58% | Condense stage collapses duplicates |\
| Large JSON arrays | 77% | Array sampling + collapse |\
| Stack traces | 0% | Intentional — error content is sacred |\
\
* * *\
\
## ⚖️ Philosophy\
\
That last row is the whole philosophy.\
\
Aggressive compression can save more tokens _on paper_, but:\
\
- If it strips context from errors\
- Drops lines from diffs\
\
➡️ The LLM gives worse answers\
\
➡️ You spend **more tokens fixing mistakes**\
\
**sqz compresses what's safe - and preserves what's critical.**\
\
* * *\
\
## ⚙️ Works Across 4 Surfaces\
\
- Shell hook → auto-compresses CLI output\
- MCP server → compiled Rust (not Node)\
- Browser extension → Firefox approved\
  - Works on: ChatGPT, Claude, Gemini, Grok, Perplexity, GitHub Copilot\
- IDE plugins → JetBrains, VS Code\
\
* * *\
\
## 🚀 Install\
\
```\
cargo install sqz-cli\
sqz init\
```\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@eliavamar](https://avatars.githubusercontent.com/u/73071299?s=80&v=4)](https://gist.github.com/eliavamar)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[eliavamar](https://gist.github.com/eliavamar)**     commented    [3 days agoApr 25, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6118572\#gistcomment-6118572)\
\
Great write-up. I built a CLI that applies this exact pattern to codebases: **Repositories Wiki**.\
\
Instead of making AI agents rediscover the repo from scratch every session, it gives them a persistent knowledge layer:\
\
- **Wiki & Indexer:** Compiles source code into a structured, interlinked markdown wiki.\
- **`AGENTS.md`:** Drops instructions in the repo root so agents know exactly how to navigate it.\
- **One-and-done generation:** Includes an `update-wiki` skill, so the agent incrementally maintains the docs as the code evolves.\
\
It saves a ton of context window and time. You can check it out here: [repositories-wiki.git](https://github.com/eliavamar/repositories-wiki.git)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@DevGuyRash](https://avatars.githubusercontent.com/u/97721401?s=80&v=4)](https://gist.github.com/DevGuyRash)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[DevGuyRash](https://gist.github.com/DevGuyRash)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6119264\#gistcomment-6119264)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
> Note: This is hand-written, no AI assistance besides screenshotting my directories and generating the tree for me\
\
As someone who has been using obsidian for many years (far before LLMs went mainstream) and LLMs and what not since late 2022, I've spent years working on my obsidian setup and making it actionable and useful for this exact thing.\
\
I've studied many systems and what I have eventually landed on that truly works is essentially a combination of two different existing systems that combine to form a very powerful setup. I have not converted this into an actual system for LLMs yet, but I plan to.\
\
This is a combination of two Personal Knowledge Management (PKM) systems and just some of my own custom things:\
\
- PARA (Projects, Areas, Resources, Archive)\
- Zettel Kasten (Permanent, Fleeting)\
- Extras:\
  - Maps of Content\
  - Goals\
  - Vault\
  - Meta\
\
What that looks like in my obsidian is:\
\
```\
.\
├── 00 - Maps of Content\
│   ├── _Index of All MOCs\
│   ├── Arbitrary MOC 1\
│   ├── Arbitrary MOC 2\
│   ├── Arbitrary MOC 3\
├── 01 - Projects\
├── 02 - Areas\
├── 03 - Resources\
├── 04 - Permanent\
├── 05 - Fleeting\
├── 06 - Journals\
├── 07 - Goals\
├── 08 - Archive\
├── 98 - Vault\
└── 99 - Meta\
```\
\
I decided on this because I needed something truly scalable that doesn't work in theory, but in real life and is able to be intuitively searched and what not. I did take some inspiration from some youtubers so it's not FULLY my own idea, but I believe I implemented it well enough as i have several thousand docs in my obsidian knowledge base hand-written over time as well as snippets, resources, etc.\
\
Here's a breakdown of how each dir is used:\
\
- **00 - Maps of Content**\
  - This is where I put all my indexes. I used to debate on the idea of having an index inside each major dir, but realized it was NOT scalable and everything is far too scattered.\
  - This contains 2 types of index files. One **master** index file which links to all other index files and then one index file per major category of work. Usually contains directories, files, etc.\
  - I considered how to make the master MOC scalable and to achieve this I used templates which auto-add a very specific MOC (Map of Content) tag to all normal MOC files. Using Dataview, it auto-lists all MOC files via that. I also have another few tags for `category` and `subcategory` which then further separates things.\
- **01 - Projects**\
  - These are encapsulated projects that are essentially their own things. They have their own docs, files, etc. Usually these are more loose, but I try not to reference outside notes as much and vice versa since these are meant to be their own things. I do sometimes instantiate miniature versions of either zettel kasten or PARA Inside a project, but to make these really useful I have template files and **Goals** within these which are their own entire frameworks I invented myself. A lot of this relies on templates for projects. I'm trying to keep it high level though so I won't get into it.\
- **02 - Areas**\
  - Ongoing things that can never really become permanent notes since they're constantly experiencing revisions and updates and what not.\
  - At some point, things may stabilize and they can be moved to permanent as you stop adding to them if you want.\
- **04 - Permanent**\
  - Where notes go to not be edited anymore. They can still occasionally be, but ideally this is a static thing that has many directories, files, etc. It's knowledge that won't be changing much and is reliable and can be referred back to over and over.\
- **05 - Fleeting**\
  - Temporary notes, ideas, etc.\
  - Can be anything at all that you don't have time to convert to a permanent note or sort out right now. The idea is to eventually come back to these and either finish them or sort them out later or whatever you want with them. It's a temporary holding.\
- **06 - Journals**\
  - Journals for:\
    - Yearly\
    - Quarterly\
    - Monthly\
    - Weekly\
    - Daily\
  - Can have whatever you want, but mine tend to have tasks in them, goals, etc. The longer-range ones auto-list goals/tasks beneath them that fall within their timeframe, but also can have their own. Also includes progress on these things too from a more abstract perspective.\
- **07 - Goals**\
  - This is an entire system I built out using scripts and they can go in multiple places. The idea is that I create goals here as a Single Source of Truth and reference them in Journals, Areas, etc. Projects have their own goals. These rely heavily on templates with specific static tags.\
- **08 - Archive**\
  - An archive for moving things no longer relevant or needed here. Can have it's own structure of this exact setup inside of it (minus another Archive)\
- **98 - Vault**\
  - Secrets that are encrypted with git-crypt. Sensitive files, etc.\
- **99 - Meta**\
  - Scripts, templates, etc. that are used throughout everywhere else to tie things together and automate them\
\
There's a **lot** of things not mentioned since this is an abstract overview. I have a plethora of templates, scripts, plugins, and more powering all of this in my obsidian that work amazingly. This is my foundation, and I'm considering now how it can be converted to a more agentic-friendly setup for individual projects.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@kytmanov](https://avatars.githubusercontent.com/u/19655528?s=80&v=4)](https://gist.github.com/kytmanov)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[kytmanov](https://gist.github.com/kytmanov)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6119290\#gistcomment-6119290)\
\
### LLM Wiki v0.7.0 is out!\
\
Huge update for cleaner, next-level concept generation:\
\
- fewer broken draft links\
- quieter Obsidian graph\
- better source citations\
- useful names preserved without random articles\
\
Turn messy notes into a reviewable local wiki.\
\
[https://github.com/kytmanov/obsidian-llm-wiki-local](https://github.com/kytmanov/obsidian-llm-wiki-local)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@oadank](https://avatars.githubusercontent.com/u/236710909?s=80&v=4)](https://gist.github.com/oadank)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[oadank](https://gist.github.com/oadank)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6119304\#gistcomment-6119304)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
Guys, I've absorbed the essence from all of you here and made my own version. You can take a look and use it for reference.\
\
[https://github.com/oadank/openclaw-wiki-lancedb](https://github.com/oadank/openclaw-wiki-lancedb)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@ontehfritz](https://avatars.githubusercontent.com/u/875813?s=80&v=4)](https://gist.github.com/ontehfritz)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[ontehfritz](https://gist.github.com/ontehfritz)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6119704\#gistcomment-6119704)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
There is a protocol for this and the idea is parallel:\
\
[https://www.demarkus.io/](https://www.demarkus.io/)\
\
[https://github.com/latebit-io/demarkus](https://github.com/latebit-io/demarkus)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@thistleknot](https://avatars.githubusercontent.com/u/5154106?s=80&v=4)](https://gist.github.com/thistleknot)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[thistleknot](https://gist.github.com/thistleknot)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6119808\#gistcomment-6119808)\
\
Plus 1 for skill format!\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@wixregiga](https://avatars.githubusercontent.com/u/30182903?s=80&v=4)](https://gist.github.com/wixregiga)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[wixregiga](https://gist.github.com/wixregiga)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6119945\#gistcomment-6119945)\
\
> Interesting paper : LLMs Corrupt Your Documents When You Delegate [https://arxiv.org/html/2604.15597v1](https://arxiv.org/html/2604.15597v1)\
\
Awesome paper\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@llopez](https://avatars.githubusercontent.com/u/118902?s=80&v=4)](https://gist.github.com/llopez)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[llopez](https://gist.github.com/llopez)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6120099\#gistcomment-6120099)\
\
If i am not wrong — the way to implement this is to copy-paste this as a prompt and iterate from there. I have a question: can we do the first iteration with Claude, for example, and then switch to MiniMax 2.7? I want to use it with OpenClaw, but Anthropic models are blocked there. However, I'd like to build the foundation using the best model I currently have access to — Claude Opus.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@gowtham0992](https://avatars.githubusercontent.com/u/15722259?s=80&v=4)](https://gist.github.com/gowtham0992)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[gowtham0992](https://gist.github.com/gowtham0992)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6120116\#gistcomment-6120116)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
Built an implementation of this pattern called [Link](https://github.com/gowtham0992/link) that works with Kiro, Claude Code, Cursor, and Codex. A few things I learned building it that might be useful:\
\
**The scale wall is real.** index.md works fine at small scale but becomes a bottleneck fast. Solved it with an in-memory inverted token index — search is now O(1) at any wiki size, sub-millisecond. The key insight: build the index once at server startup, not per-query.\
\
**Agents re-derive context every session**. The fix that helped most was a /api/context?topic=X endpoint that returns the primary page + its full graph neighborhood (inbound + forward links) in one call. Agents stop reading index.md on every turn.\
\
**MCP makes it composable**. Wrapped the search and graph endpoints as MCP tools (search\_wiki, get\_context, get\_graph etc.) — now any MCP-compatible agent can query the wiki natively. Listed on the official MCP registry as io.github.gowtham0992/link, installable with pip install link-mcp.\
\
The install is one command per agent — sets up steering, scaffolds the wiki, installs the MCP server, and registers it in the agent's config automatically. The local viewer also has an interactive graph view built in (no Obsidian needed):\
\
![image](https://private-user-images.githubusercontent.com/15722259/583918591-458802fa-2ffd-4281-a737-fa9218a29395.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzczNzg5NDYsIm5iZiI6MTc3NzM3ODY0NiwicGF0aCI6Ii8xNTcyMjI1OS81ODM5MTg1OTEtNDU4ODAyZmEtMmZmZC00MjgxLWE3MzctZmE5MjE4YTI5Mzk1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDI4VDEyMTcyNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU2M2MwZDJjOTk0YTg0NWQwODUzOGRiMWQ2YTZhYzNkYTM2ZGExOWEzZmJhMWQ5ZGMyODAwM2YwMDQ1YjllMTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.hU2ZNYdVwfrEkx7XS9zr_8YnwrHA4dUdBZJ9hubV-hE)  ![image](https://private-user-images.githubusercontent.com/15722259/583919079-ef9aa727-deed-47df-9a1c-57358c15467a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzczNzg5NDYsIm5iZiI6MTc3NzM3ODY0NiwicGF0aCI6Ii8xNTcyMjI1OS81ODM5MTkwNzktZWY5YWE3MjctZGVlZC00N2RmLTlhMWMtNTczNThjMTU0NjdhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDI4VDEyMTcyNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU2N2JhOWFhYTZjYjcyMTM5MDg2ZmRiZTFmOWZjOTg5Y2I5NzcyNTQzZmM3ZWIzZmUxNzUyZWIzNzA1NmYxYjQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.uue_Y1Lk-K9EezwJUPszSNR3WVCe__IAWR8QCSaYt7Q)\
\
→ [Github](https://gist.github.com/karpathy/github.com/gowtham0992/link)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@7xuanlu](https://avatars.githubusercontent.com/u/23661875?s=80&v=4)](https://gist.github.com/7xuanlu)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[7xuanlu](https://gist.github.com/7xuanlu)**     commented    [2 days agoApr 26, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6120148\#gistcomment-6120148)\
\
Most implementations here are CLI tools or agent skills. I built a desktop app (Tauri + Rust) with a background daemon.\
\
The daemon runs independently of any agent. Entity extraction, dedup, contradiction detection, concept distillation fire on triggers (idle periods, session ends, daily). Knowledge compounds between sessions, not just during them.\
\
The biggest surprise: a quality gate before storage mattered more than anything else. Not everything belongs in the wiki. Filtering noise at the door beat every retrieval improvement I tried.\
\
On-device by default (Qwen3-4B / Qwen3.5-9B on Metal). Open source: github.com/7xuanlu/origin\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@jhkchan](https://avatars.githubusercontent.com/u/1083902?s=80&v=4)](https://gist.github.com/jhkchan)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[jhkchan](https://gist.github.com/jhkchan)**     commented    [yesterdayApr 27, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6120508\#gistcomment-6120508)\
\
Thanks [@karpathy](https://github.com/karpathy) — your three-layer framing is exactly the model we landed on after watching chunk-first RAG fall over on team-chat corpora.\
\
We open-sourced **[Beever Atlas](https://github.com/Beever-AI/beever-atlas)** (Apache 2.0) as a runnable implementation of the LLM Wiki pattern applied to chat memory. The conversational case is where the wiki idea pays off most: the same fact gets restated across dozens of threads, the meaningful structure lives outside the message body, and flat vector retrieval mostly returns noise.\
\
What we ended up building:\
\
- **Sources → Wiki → Schema** layered exactly as you describe — the Wiki is browsable as a channel → topic → fact tree with a concept-map view (screenshot below)\
- A six-stage agent extraction pipeline (preprocess → fact extract → entity extract → cross-batch validate → relationship extract → persist); the cross-batch validator is what keeps the Fact tier non-noisy\
- Dual memory: a 3-tier semantic store (Channel / Topic / Fact) for _what was said_ \+ a graph for _who decided what when_, with a small LLM classifier picking which side(s) to query per question\
- A 16-tool MCP server so Claude Code and Cursor consume the same wiki\
\
![Beever Atlas — Wiki / Overview, channel-topic tree on left and concept map in the middle](https://private-user-images.githubusercontent.com/1083902/584000132-d667890b-ee76-46ad-81d3-31c8d46f338b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzczNzg5NDYsIm5iZiI6MTc3NzM3ODY0NiwicGF0aCI6Ii8xMDgzOTAyLzU4NDAwMDEzMi1kNjY3ODkwYi1lZTc2LTQ2YWQtODFkMy0zMWM4ZDQ2ZjMzOGIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQyOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MjhUMTIxNzI2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YmUzYjU3ZTJmYWM5N2RhNTU4ZjQ0YTdkYTkzMzczY2I2YmZiNGIxYjZhNzM2YjkwZGRiNDE3NWE5NjJiM2QyZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.D_hi1zw6aI2TJS5fLNeMgX5ORiQdbvQQT3fhjjsOlD0)\
\
`make demo` brings up the full stack with a public Wikipedia corpus pre-loaded — grounded answers in <5 minutes.\
\
[https://github.com/Beever-AI/beever-atlas](https://github.com/Beever-AI/beever-atlas)\
\
(Disclosure: I'm a maintainer — Beever AI Limited, Toronto.)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@suai723](https://avatars.githubusercontent.com/u/7997408?s=80&v=4)](https://gist.github.com/suai723)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[suai723](https://gist.github.com/suai723)**     commented    [yesterdayApr 27, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6120533\#gistcomment-6120533)\
\
Before lunar New Year 2026, I had already come up with this approach and validated it myself. It proved to be very effective for Q&A and data SQL writing scenarios. My previous approach was a two-level file indexing structure. Based on that, I built two lightweight SKILLs for parsing and reading.\
\
[https://github.com/suai723/OperationsManual](https://github.com/suai723/OperationsManual)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@mauceri](https://avatars.githubusercontent.com/u/1011775?s=80&v=4)](https://gist.github.com/mauceri)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[mauceri](https://gist.github.com/mauceri)**     commented    [yesterdayApr 27, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6120567\#gistcomment-6120567)  via email\
\
[@llopez](https://github.com/llopez) It works well with Claude scaffolding and DeepSeek doing the hard\
work, for instance. Claude writes the schema and the tools used by DeepSeek\
: ingest, summarize, query, etc.\
I did that with my ~2000 Brave bookmarks to make a test and it cost me $15\
with many retries.\
Christian Mauceri\
\
Le lun. 27 avr. 2026, 08:21, sinhyunsung \*\*\*@\*\*\*.\*\*\*> a\
écrit :\
\
[…](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#)\
\
\\*\\*\\*@\\*\\*\\*.\\*\\*\\*\\* commented on this gist.\
 ------------------------------\
\
I think this is a really promising concept.\
\
What I find especially interesting about LLM Wiki is that it goes beyond\
simple retrieval. Instead of only searching documents at query time, it\
turns scattered information into a continuously updated knowledge structure.\
\
For companies, this could be extremely valuable. Many organizations\
already have a lot of internal documents, but the knowledge is fragmented\
across files, folders, emails, and individual employees. If an LLM can\
organize that information into a living wiki with sources, links, and\
updates, it could become a practical layer of institutional memory.\
\
Of course, implementation details such as permissions, source tracking,\
update logic, and cost control will be very important. But as a concept, I\
think LLM Wiki is a very strong direction for making LLMs more useful in\
real work environments.\
\
—\
Reply to this email directly, view it on GitHub\
< [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#gistcomment-6120543](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#gistcomment-6120543) >\
or unsubscribe\
< [https://github.com/notifications/unsubscribe-auth/AAHXAP6F7HHZZZQCBTW6FTD4X34AFBFHORZGSZ3HMVZKMY3SMVQXIZNMON2WE2TFMN2F65DZOBS2WR3JON2EG33NNVSW45FGORXXA2LDOOIYFJDUPFYGLJDHNFZXJJLWMFWHKZNJGE2DOMRVHAYDKMFKMF2HI4TJMJ2XIZLTSOBKK5TBNR2WLKBTG43TOOBTGM42I3TBNVS2QYLDORXXEX3JMSBKK5TBNR2WLJDUOJ2WLJDOMFWWLO3UNBZGKYLEL5YGC4TUNFRWS4DBNZ2F6YLDORUXM2LUPGBKK5TBNR2WLJDHNFZXJJDOMFWWLK3UNBZGKYLEL52HS4DF](https://github.com/notifications/unsubscribe-auth/AAHXAP6F7HHZZZQCBTW6FTD4X34AFBFHORZGSZ3HMVZKMY3SMVQXIZNMON2WE2TFMN2F65DZOBS2WR3JON2EG33NNVSW45FGORXXA2LDOOIYFJDUPFYGLJDHNFZXJJLWMFWHKZNJGE2DOMRVHAYDKMFKMF2HI4TJMJ2XIZLTSOBKK5TBNR2WLKBTG43TOOBTGM42I3TBNVS2QYLDORXXEX3JMSBKK5TBNR2WLJDUOJ2WLJDOMFWWLO3UNBZGKYLEL5YGC4TUNFRWS4DBNZ2F6YLDORUXM2LUPGBKK5TBNR2WLJDHNFZXJJDOMFWWLK3UNBZGKYLEL52HS4DF) >\
.\
You are receiving this email because you are subscribed to this thread.\
\
Triage notifications on the go with GitHub Mobile for iOS\
< [https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675](https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675) >\
or Android\
< [https://play.google.com/store/apps/details?id=com.github.android&referrer=utm\_campaign%3Dnotification-email%26utm\_medium%3Demail%26utm\_source%3Dgithub](https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub) >\
.\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@JanniOsier](https://avatars.githubusercontent.com/u/273809332?s=80&v=4)](https://gist.github.com/JanniOsier)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[JanniOsier](https://gist.github.com/JanniOsier)**     commented    [yesterdayApr 27, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6121172\#gistcomment-6121172)\
\
Check this out: [https://github.com/WattTonn/KnowledgeWeaver](https://github.com/WattTonn/KnowledgeWeaver)\
\
This tool solves the index part of this gist\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@mauceri](https://avatars.githubusercontent.com/u/1011775?s=80&v=4)](https://gist.github.com/mauceri)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[mauceri](https://gist.github.com/mauceri)**     commented    [15 hours agoApr 27, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6121742\#gistcomment-6121742)\
\
Very interesting article : [https://ai.gopubby.com/rag-llm-wiki-or-gbrain-how-your-agent-remembers-changes-everything-56829e66725c](https://ai.gopubby.com/rag-llm-wiki-or-gbrain-how-your-agent-remembers-changes-everything-56829e66725c)\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@vekexasia](https://avatars.githubusercontent.com/u/200523?s=80&v=4)](https://gist.github.com/vekexasia)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[vekexasia](https://gist.github.com/vekexasia)**     commented    [3 hours agoApr 28, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6122505\#gistcomment-6122505)\
\
I cited llm wiki in this post [https://andreabaccega.com/blog/text-is-the-new-binary/](https://andreabaccega.com/blog/text-is-the-new-binary/) where i discuss how software is shifting from `binary` to `text`\
\
Sorry, something went wrong.\
\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[![@nghoihin-byte](https://avatars.githubusercontent.com/u/279699101?s=80&v=4)](https://gist.github.com/nghoihin-byte)\
\
\
Copy link\
\
\
Copy Markdown\
\
### **[nghoihin-byte](https://gist.github.com/nghoihin-byte)**     commented    [52 minutes agoApr 28, 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?permalink_comment_id=6122761\#gistcomment-6122761)•   edited      Loading          \#\#\# Uh oh!        There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
This gist crystallized something we'd been building. We just open-sourced the team-native version: Beever Atlas ( [github.com/Beever-AI/beever-atlas](https://github.com/Beever-AI/beever-atlas)) — Apache 2.0.\
\
![Screenshot 2026-04-25 at 1 07 53 AM](https://private-user-images.githubusercontent.com/279699101/584780399-b22bda34-236a-4cf9-bc00-92db1c93b0f3.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzczNzg5NDYsIm5iZiI6MTc3NzM3ODY0NiwicGF0aCI6Ii8yNzk2OTkxMDEvNTg0NzgwMzk5LWIyMmJkYTM0LTIzNmEtNGNmOS1iYzAwLTkyZGIxYzkzYjBmMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNDI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDQyOFQxMjE3MjZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04OTdkMjk1OTNmZTRhYjRkZDI1N2Y0YTUyZjE5OTg2YzdlYjhjM2FlODFmZGJkZTBjMmI0Yzc3YjFmMGNhMzU2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.2XCG3CprTG8vjRvl63h0q2_MkjjKxyoubdBmvRV_mHs)\
\
Same core thesis: distill messy chat into a structured wiki, then retrieve from the wiki rather than the chat. Not pure vector RAG —\
\
typed-graph (Neo4j) + semantic store (Weaviate) + 6-stage Google ADK pipeline that turns Slack/Discord/Teams into atomic facts with citations.\
\
What we added on top of your framing:\
\
• Native MCP server (16 tools) — Claude Code / Cursor can query a team's wiki directly\
\
• Multimodal via Jina v4 (text + images + PDFs in chat)\
\
• BYO LLM via LiteLLM (Ollama, Qwen, Claude, GPT, Gemma)\
\
• On-prem-friendly — sovereign deployment\
\
The use-case we test against: day-3 onboarding. New hire opens the wiki, clicks Decisions, finds "Stripe vs Adyen" with citations linking back to the original Slack thread. Onboarding scales without putting anyone on call.\
\
Built in Hong Kong + Toronto. Workshop Week (Days 1–5) on the implementation:\
\
[https://www.linkedin.com/posts/beever-ai\_andrej-karpathy-called-for-an-incredible-activity-7452591138810753024-G\_ZO?utm\_source=share&utm\_medium=member\_desktop&rcm=ACoAAAegEO0B-am6rV\_DQGT\_PV605Ofu8lS5YgI](https://www.linkedin.com/posts/beever-ai_andrej-karpathy-called-for-an-incredible-activity-7452591138810753024-G_ZO?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAegEO0B-am6rV_DQGT_PV605Ofu8lS5YgI)\
\
[https://beeverai.medium.com/day-1-your-teams-chat-is-a-wiki-waiting-to-happen-a-new-kind-of-rag-3c6e78b0b258?postPublishedType=repub](https://beeverai.medium.com/day-1-your-teams-chat-is-a-wiki-waiting-to-happen-a-new-kind-of-rag-3c6e78b0b258?postPublishedType=repub)\
\
Genuine thank-you for putting words to it.\
\
— Jack\
\
Sorry, something went wrong.\
\
\
### Uh oh!\
\
There was an error while loading. [Please reload this page](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).\
\
[Sign up for free](https://gist.github.com/join?source=comment-gist) **to join this conversation on GitHub**.\
Already have an account?\
[Sign in to comment](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fkarpathy%2F442a6bf555914893e9891c11519de94f)\
\
## Footer\
\
[GitHub Homepage](https://github.com/)\
© 2026 GitHub, Inc.\
\
\
### Footer navigation\
\
- [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)\
- [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)\
- [Security](https://github.com/security)\
- [Status](https://www.githubstatus.com/)\
- [Community](https://github.community/)\
- [Docs](https://docs.github.com/)\
- [Contact](https://support.github.com/?tags=dotcom-footer)\
- Manage cookies\
\
- Do not share my personal information\
\
\
You can’t perform that action at this time.