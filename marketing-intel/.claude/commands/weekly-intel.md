---
description: Run weekly Reddit intelligence sweep for a domain and log to Notion
argument-hint: [ai-marketing|paid-media|web-wordpress|real-estate]
---

You are running the weekly Marketing Intelligence workflow for domain: $ARGUMENTS

1. Read the master prompt from prompts/$ARGUMENTS.md

2. Execute Part 1 of the master prompt: fetch the top-performing Reddit posts from the listed subreddits using WebFetch or WebSearch. Pull the top 10–12 posts per subreddit from the past week. If a subreddit search comes back thin, fall back to manually browsing r/{subreddit}/top/?t=week. Compile into one clean plaintext list.

3. Execute Part 2 of the master prompt: run the intelligence analysis against the harvested post list. Produce a long-form report with exactly 15 numbered takeaways, a theme analysis section, and a referenced posts list. Plain text only — no Markdown, emojis, or tables.

4. Create a new page in the "Marketing Intelligence" Notion database via the Notion MCP tools:
   - Title: "{Domain Label} — Week of {Monday's date}"
   - Domain: select the matching dropdown value (AI & Marketing / Paid Media & PPC / Web & WordPress / Real Estate)
   - Raw Text: the unformatted synthesis output
   - Week: this week's Monday date
   - Page body: the formatted version with bold section headings and clean spacing, links cleaned up (remove low-value or unnecessary links)

5. Confirm back with the Notion page URL and a 2-sentence summary of the top insight.

Domain label mapping:
- ai-marketing → AI & Marketing
- paid-media → Paid Media & PPC
- web-wordpress → Web & WordPress
- real-estate → Real Estate
