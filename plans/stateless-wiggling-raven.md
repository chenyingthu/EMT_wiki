# EMT Wiki - LLM Batch Analysis of Source Pages

## Context

All 699 source pages in `wiki/sources/` have frontmatter (title, authors, year, tags, abstract) but all five analysis sections are "待分析" placeholders. The wiki has 6 topic pages, 8 method pages, and 8 model pages already created. Need to fill each source page's 核心贡献/使用的方法/涉及的模型/相关主题/主要发现 sections by analyzing the abstract text.

## Approach

Create `tools/analyze_sources.py` — a Python script that uses the LLM API (DashScope/Anthropic-compatible) to analyze abstracts and write results back to markdown files. Batch processing with checkpoint/resume.

## Steps

### Step 1: Write `tools/analyze_sources.py`

**Core components:**

1. **Tag-to-taxonomy mapping** — maps existing frontmatter tags to wikilinks (e.g., `mmc` → `[[mmc-model]]`, `real-time` → `[[real-time-simulation]]`)
2. **LLM prompt** — sends abstract + tags + taxonomy context, requests JSON output with 5 fields
3. **Markdown writer** — reads source .md file, replaces "待分析" sections with LLM output
4. **Batch orchestrator** — processes 50 files per batch, saves checkpoint to `wiki/sources/.analysis_progress.json`
5. **Retry logic** — exponential backoff on API failures, handles malformed JSON

**Key files to read:**
- `wiki/sources/metadata.json` — abstract text for each paper
- `wiki/topics/*.md`, `wiki/methods/*.md`, `wiki/models/*.md` — existing taxonomy for wikilink validation

### Step 2: Dry-run on 5-10 papers

Run with `--dry-run` flag to preview LLM output without writing. Review quality of contributions, methods, models, topics, findings.

### Step 3: Batch process all 699 papers

Run in batches of 50 with `--batch-size 50 --concurrency 5`:
- Uses checkpoint file to resume from where it left off
- Each batch: read abstract → build prompt → call LLM → parse JSON → update markdown
- Log each batch to `wiki/log.md`

### Step 4: Validate results

Check:
- No "待分析" placeholders remain
- All wikilinks point to existing pages
- Core contributions non-empty
- Key findings non-empty

### Step 5: Update topic/method/model pages with back-references

After source analysis, update each topic/method/model page with a "来源论文" table listing papers that reference it.

## Execution

```bash
# Dry run first
~/anaconda3/bin/python3 tools/analyze_sources.py --dry-run --limit 10

# Full batch processing
~/anaconda3/bin/python3 tools/analyze_sources.py --batch-size 50 --concurrency 5

# Validate
~/anaconda3/bin/python3 tools/validate_analysis.py
```

## Verification

1. Spot-check 10-20 random source pages for quality
2. Run validation script to confirm no placeholders remain
3. Check all wikilinks resolve
4. Update index.md with new counts
5. Append to log.md
