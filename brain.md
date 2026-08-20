# Brain — Skills, MCP Servers & Plugins Config

> Copy this file to any new project root to bootstrap the same AI-assisted workflow.

---

## Quick Setup

1. Copy `opencode.json` into your project root (replace `YOUR_PROJECT_PATH` and `YOUR_GITHUB_TOKEN`)
2. Copy this `brain.md` for reference
3. Run `opencode` — all servers auto-install on first use via `npx`

---

## opencode.json (Copy and Customize)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [
    "@franlol/opencode-md-table-formatter@latest",
    "opencode-firecrawl",
    "opencode-conductor-plugin",
    "opencode-goal-plugin",
    "opencode-supermemory@latest"
  ],
  "command": {
    "goal": {
      "description": "Set a session-scoped goal and auto-continue until complete.",
      "template": "$ARGUMENTS",
      "agent": "build"
    }
  },
  "mcp": {
    "notebooklm": {
      "type": "local",
      "command": ["npx", "-y", "notebooklm-mcp@latest"],
      "enabled": true,
      "environment": {}
    },
    "puppeteer": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-puppeteer"],
      "enabled": true,
      "environment": {}
    },
    "memory": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-memory"],
      "enabled": true,
      "environment": {}
    },
    "filesystem": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "YOUR_PROJECT_PATH"],
      "enabled": true,
      "environment": {}
    },
    "fetch": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-fetch"],
      "enabled": true,
      "environment": {}
    },
    "github": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-github"],
      "enabled": true,
      "environment": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
      }
    },
    "playwright": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-playwright"],
      "enabled": true,
      "environment": {}
    }
  }
}
```

---

## 7 MCP Servers

### 1. notebooklm — Google NotebookLM Research

```json
"command": ["npx", "-y", "notebooklm-mcp@latest"]
```

**What it does:** Query Google NotebookLM notebooks grounded on uploaded sources. Generates Audio Overviews (podcasts).

**First-time setup:**
1. Call `get_health` — if `authenticated=false`, run `setup_auth`
2. Browser opens — log in to Google once
3. Share a NotebookLM notebook URL — `add_notebook` to register

**Key tools:**
- `ask_question` — ask questions grounded on notebook sources
- `add_notebook` — register a notebook by share URL
- `add_source` — ingest URLs or text into a notebook
- `generate_audio` — create podcast-style audio overview
- `list_notebooks` — show all registered notebooks

**Limits:** 50 queries/day (free), 50 sources/notebook, 100 notebooks

---

### 2. puppeteer — Browser Automation and Screenshots

```json
"command": ["npx", "-y", "@modelcontextprotocol/server-puppeteer"]
```

**What it does:** Headless Chrome for screenshots, page testing, JavaScript execution.

**Key tools:**
- `puppeteer_navigate` — open a URL
- `puppeteer_screenshot` — capture page/element screenshots
- `puppeteer_evaluate` — run JavaScript in browser console
- `puppeteer_click` — click elements by CSS selector
- `puppeteer_fill` — fill input fields
- `puppeteer_select` — select dropdown options

**Use cases:**
- QA testing (verify page loads, images render, features work)
- Screenshot documentation
- Automate web interactions

**Tip:** Variables persist between `evaluate` calls — use unique names like `_a`, `_b` to avoid conflicts.

---

### 3. memory — Knowledge Graph Persistence

```json
"command": ["npx", "-y", "@modelcontextprotocol/server-memory"]
```

**What it does:** Persistent entity-relation-observation graph across sessions.

**Key tools:**
- `memory_create_entities` — create nodes (e.g., "Project X", "Tech Stack")
- `memory_create_relations` — link entities (e.g., "Project X" uses "React")
- `memory_add_observations` — add notes to existing entities
- `memory_search_nodes` — search the graph
- `memory_read_graph` — dump entire graph

**Use cases:**
- Track project decisions and conventions
- Store user preferences across sessions
- Build context for complex projects

---

### 4. filesystem — Local File Read/Write

```json
"command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "YOUR_PROJECT_PATH"]
```

**What it does:** Read, write, edit, search files within the allowed project directory.

**Key tools:**
- `filesystem_read_file` / `filesystem_read_text_file` — read files
- `filesystem_write_file` — create/overwrite files
- `filesystem_edit_file` — line-based edits with diff preview
- `filesystem_list_directory` — list files
- `filesystem_search_files` — glob pattern search
- `filesystem_move_file` — rename/move files

**Limitation:** Only accesses the path specified in the command. Change it per project.

---

### 5. fetch — HTTP Requests

```json
"command": ["npx", "-y", "@modelcontextprotocol/server-fetch"]
```

**What it does:** Fetch URLs, download content, make HTTP requests.

**Key tools:**
- `fetch_get` — GET a URL
- `fetch_post` — POST data

**Use cases:**
- Download files from URLs
- Test API endpoints
- Grab web content

---

### 6. github — GitHub API Integration

```json
"command": ["npx", "-y", "@modelcontextprotocol/server-github"],
"environment": { "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN" }
```

**What it does:** Create repos, issues, PRs, push files via GitHub API.

**Setup:** Get a token at https://github.com/settings/tokens (scopes: `repo`, `workflow`)

**Key tools:**
- `github_create_repository` — create new repo
- `github_push_files` — push multiple files in one commit
- `github_create_pull_request` — open PRs
- `github_create_issue` — file issues
- `github_list_issues` / `github_list_pull_requests` — list items

**Note:** For simple `git push`, git credential manager works without this token. This server is for API operations.

---

### 7. playwright — Browser Testing (Alternative)

```json
"command": ["npx", "-y", "@modelcontextprotocol/server-playwright"]
```

**What it does:** Similar to Puppeteer but uses Playwright. More browser engine support (Firefox, WebKit).

**Use when:** You need cross-browser testing or Puppeteer is insufficient.

---

## 5 Plugins

### 1. @franlol/opencode-md-table-formatter

```json
"@franlol/opencode-md-table-formatter@latest"
```

**What it does:** Auto-formats markdown tables with proper alignment when writing `.md` files.

**No config needed.** Just works.

---

### 2. opencode-firecrawl

```json
"opencode-firecrawl"
```

**What it does:** Web search, scraping, crawling, content extraction. The most-used plugin.

**Setup:** Run once: `npx -y firecrawl-cli@latest init --all -k YOUR_API_KEY`
Get free key at https://firecrawl.dev

**Key skills (auto-loaded):**

| Skill | When to use |
|-------|-------------|
| `firecrawl-search` | Search the web, find articles |
| `firecrawl-scrape` | Extract content from a URL |
| `firecrawl-crawl` | Bulk extract from entire sites |
| `firecrawl-map` | Discover all URLs on a site |
| `firecrawl-interact` | Click, fill forms, navigate flows |
| `firecrawl-download` | Download site as local files |
| `firecrawl-parse` | Convert PDF/DOCX to markdown |
| `firecrawl-deep-research` | Intensive analytical reports |
| `firecrawl-research-papers` | Find academic papers |
| `firecrawl-seo-audit` | SEO analysis |
| `firecrawl-monitor` | Track page changes |
| `firecrawl-qa` | QA test a live website |
| `firecrawl-lead-gen` | Generate lead lists |
| `firecrawl-market-research` | Extract market/financial data |

**CLI commands:**
```bash
firecrawl scrape "<url>" --format markdown -o output.md
firecrawl search "query" --format markdown -o results.md
firecrawl crawl "<url>" --format markdown -o ./output/
firecrawl map "<url>" -o urls.md
```

**Credits:** 1,000 free/month. Each scrape ~1-5 credits, search ~2-5 credits.

---

### 3. opencode-conductor-plugin

```json
"opencode-conductor-plugin"
```

**What it does:** Structured workflow: Context -> Spec -> Plan -> Implement.

**Commands:**
- `/conductor:setup` — initialize project structure
- `/conductor:newTrack` — create a feature/bug track
- `/conductor:implement` — execute implementation

**Use when:** You want structured, phased development with specs and plans.

---

### 4. opencode-goal-plugin

```json
"opencode-goal-plugin"
```

**What it does:** Set a session goal with auto-continue until complete.

**Command:** `/goal <objective>`

**Config in opencode.json:**
```json
"command": {
  "goal": {
    "description": "Set a session-scoped goal and auto-continue until complete.",
    "template": "$ARGUMENTS",
    "agent": "build"
  }
}
```

**Use when:** You want the AI to autonomously work through a multi-step task without pausing for confirmation.

---

### 5. opencode-supermemory

```json
"opencode-supermemory@latest"
```

**What it does:** Persistent memory across sessions. Remembers project context, decisions, patterns.

**Setup:** Run once: `npx opencode-supermemory@latest login`

**Key tools:**
- `supermemory add` — store knowledge (project config, preferences, patterns)
- `supermemory search` — find stored memories
- `supermemory profile` — view user profile
- `supermemory list` — recent memories
- `supermemory forget` — remove a memory

**Scope:** `user` (personal) or `project` (project-specific)

---

## Skills Reference (Auto-loaded by Firecrawl)

Skills are auto-injected when you say trigger phrases. Key ones:

| Skill | Trigger phrases |
|-------|-----------------|
| `firecrawl-search` | "search for", "find me", "look up" |
| `firecrawl-scrape` | "scrape", "grab", "fetch this URL" |
| `firecrawl-interact` | "click", "fill form", "log in to" |
| `firecrawl-crawl` | "crawl entire site", "get all pages" |
| `firecrawl-download` | "download the site", "save offline copy" |
| `firecrawl-parse` | "parse this PDF", "convert this document" |
| `firecrawl-deep-research` | "write a report on", "analyze this topic" |
| `firecrawl-qa` | "QA test", "check this website" |
| `firecrawl-seo-audit` | "SEO audit", "check SEO" |
| `firecrawl-monitor` | "monitor this page", "alert me when" |
| `firecrawl-lead-gen` | "find prospects", "generate leads" |

---

## Auth Setup Checklist

For a new project, run these once:

```bash
# 1. Firecrawl (web search/scrape)
npx -y firecrawl-cli@latest init --all -k YOUR_FIRECRAWL_KEY

# 2. Supermemory (persistent memory)
npx opencode-supermemory@latest login

# 3. NotebookLM (Google research) — auto-opens browser
# Just call get_health() then setup_auth() in the session

# 4. GitHub token — paste into opencode.json
# Get at: https://github.com/settings/tokens
```

---

## Workflow Tips

1. Start with `/goal` for multi-step tasks — AI works autonomously
2. Use `firecrawl-search` before building anything — research first
3. Use `firecrawl-scrape` to get exact content from URLs
4. Use `puppeteer` for QA — screenshots, feature testing
5. Use `memory` to track decisions — persist context across sessions
6. Use `conductor` for structured development — spec then plan then build
7. Copy this `brain.md` to every new project for instant context
