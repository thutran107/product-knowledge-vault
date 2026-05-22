# Generic Obsidian + Claude Code Knowledge Base Setup

The lightweight starting point for building a local AI-powered knowledge base.
No vector database. No backend. Just Markdown files, Obsidian, and Claude Code.

---

## What You're Building

A local folder of Markdown files that Claude Code can read, navigate, and write to.
Obsidian is your visual browser. Claude Code is your knowledge worker.
You drop raw content in. Claude turns it into an organized, cross-linked wiki.

```
raw/         ← Dump everything here: articles, PDFs, web clips, notes
wiki/        ← Claude writes organized knowledge pages here
claude.md    ← Rules file: tells Claude how to navigate and write
```

![Karpathy's Cheat Code RAG — A Lightweight Obsidian Setup](assets/obsidian_claude_code_guide.png)

The setup has two phases: building the file structure and configuring Claude (Phase 1), then ingesting content and generating the wiki (Phase 2). The comparison on the right shows why this approach beats traditional RAG for most use cases — no vector database, no infrastructure, solo-friendly complexity.

---

## Step 1: Download and Install Obsidian

Obsidian is a free desktop app that renders Markdown files as a navigable wiki.

1. Go to **obsidian.md** and download the app (free, available for Mac, Windows, Linux)
2. Install and open it
3. When prompted, choose **Create new vault** and point it at a new folder on your machine — call it something like `the-vault`

```
┌─────────────────────────────────────────┐
│ Welcome to Obsidian                     │
│                                         │
│  [ Create new vault ]  ← click here     │
│  [ Open folder as vault ]               │
│  [ Open from Obsidian Sync ]            │
└─────────────────────────────────────────┘
```

---

## Step 2: Create the Folder Structure

Inside your vault, create two folders and one file:

```
📁 the-vault/
 ├── 📄 claude.md          ← Rules file for Claude Code
 ├── 📁 raw/               ← Staging area: drop all source content here
 └── 📁 wiki/              ← Claude writes organized knowledge here
      ├── 📄 master_index.md   ← Master list of all wikis
      ├── 📁 ai-agents/        ← One folder per topic wiki
      │    └── 📄 index.md
      └── 📁 rag-systems/      ← Another topic wiki
           └── 📄 index.md
```

You can create these folders manually in your file system, or open Claude Code
in the vault directory and prompt it:

```
Create the following folder structure in this directory:
- raw/ (empty folder)
- wiki/ with a master_index.md file
- claude.md at the root
```

Each wiki folder under `wiki/` represents one topic you're researching.
The `master_index.md` is a running list of all topics with links to each wiki's index.

---

## Step 3: Write the `claude.md` Rules File

`claude.md` sits at the vault root and tells Claude Code how to operate in this folder.
Without it, Claude will make many redundant tool calls trying to find its bearings.

A minimal `claude.md` should cover:

```markdown
# Knowledge Base Rules

## Structure
- raw/           ← Source files. Never modify.
- wiki/          ← My output. I create and update files here.
- master_index.md ← I keep this updated with all wiki entries.

## How to navigate
- Always read master_index.md first when answering a question.
- Use [[wiki-link]] format for all internal links.
- Each wiki folder has its own index.md listing its pages.

## How to create a wiki
1. Read all relevant files in raw/
2. Extract key concepts, entities, and relationships
3. Create linked Markdown pages in wiki/<topic>/
4. Update the topic's index.md
5. Add the topic to master_index.md

## File naming
- Lowercase, hyphens only
- Descriptive slugs: ai-agents-overview.md, not doc1.md
```

This is the minimum. The more precise your rules, the more consistent Claude's output.

---

## Step 4: Install the Obsidian Web Clipper

The Web Clipper is a browser extension that converts any web page to Markdown
and saves it directly into your vault with one click.

1. Go to **obsidian.md/clipper** and install the Chrome (or Firefox/Safari) extension
2. Right-click the extension icon → **Options**
3. Under **Default Template**, find **Note Location**
4. Change it from `clippings` to `raw`

```
┌─────────────────────────────────────────┐
│ Web Clipper Options                     │
│                                         │
│ Default Template                        │
│ Note Location: [ raw ]  ← change this   │
│                                         │
│ [ Save Settings ]                       │
└─────────────────────────────────────────┘
```

Now every page you clip lands directly in `raw/` — ready for Claude to ingest.

**Recommended: add a content template**

In the Web Clipper's template settings, add this frontmatter so Claude knows
the source URL and date for every clipped note:

```
---
clipped_from: {{url}}
date_clipped: {{date}}
title: "{{title}}"
---

{{content}}
```

---

## Step 5: Install "Local Images Plus"

By default, Web Clipper leaves images as remote URLs — they break if the source page
changes. **Local Images Plus** downloads images locally when you clip.

1. Open Obsidian → Settings (gear icon, bottom left)
2. Community Plugins → Browse
3. Search **Local Images Plus**
4. Install, enable, and make sure the toggle is ON

```
┌─────────────────────────────────────────┐
│ Community Plugins                       │
│                                         │
│ Search: [ Local Images Plus ]           │
│                                         │
│ 📦 Local Images Plus                    │
│    Status: [ ON ]  ← ensure enabled     │
└─────────────────────────────────────────┘
```

---

## Step 6: Generate a Wiki with Claude Code

Once you have content in `raw/`, open Claude Code in your vault directory and prompt it:

```
Let's create a wiki about [your topic]. I've added some source articles
to the raw folder. Read through them and generate a structured wiki
in wiki/[topic]/, then update master_index.md.
```

Claude will:
1. Read the source files in `raw/`
2. Extract key concepts, entities, and relationships
3. Write cross-linked Markdown pages into `wiki/[topic]/`
4. Create an `index.md` for that topic
5. Update `master_index.md`

You can also ask Claude to pull in its own knowledge:

```
Create a wiki about RAG systems. Use what's in raw/ and supplement
with your own knowledge. Link everything together.
```

---

## Step 7: Ask Questions

Once the wiki exists, query it conversationally:

```
What are the main tradeoffs between RAG approaches?
How does [concept A] relate to [concept B]?
Summarize everything we know about [topic].
```

Claude reads `master_index.md` to orient itself, pulls the relevant wiki pages,
and gives a cited answer.

---

## Tips

- **Dump freely, organize later.** Clip anything that looks relevant into `raw/`. You don't need to clean it up before ingesting — Claude handles that.
- **One wiki per session works well.** Focused ingests produce tighter pages.
- **Ask for links.** Explicitly prompt Claude to cross-link pages — it makes the graph view in Obsidian useful.
- **Obsidian Graph View** (Ctrl/Cmd + G) visualizes the connection network. It gets interesting fast once you have 20+ linked pages.
- **`claude.md` is a living document.** Refine the rules as you see what Claude produces. If pages are inconsistent, the fix is almost always in the rules file.

---

## What's Next

This setup works well for personal research and topic-specific knowledge bases.
As your needs grow, you'll start hitting limits:

- Flat topic folders don't distinguish between types of knowledge (facts vs. analysis vs. source provenance)
- No conflict detection when sources disagree
- No trust hierarchy when older and newer sources contradict each other
- No structured ingest workflow — quality depends on prompting each time

The next step is evolving `claude.md` from a navigation guide into a full schema —
defining typed entity pages, ingest workflows, conflict resolution rules,
and a document trust hierarchy. That's where the system goes from
a personal research tool to a team-grade knowledge base.
