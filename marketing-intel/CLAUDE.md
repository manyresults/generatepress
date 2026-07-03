# Marketing Intelligence Project

This repo automates weekly Reddit intelligence gathering and monthly newsletter synthesis for MANY Results client domains.

## Structure

- `prompts/` — master prompts for each domain (Part 1: post harvesting, Part 2: analysis)
- `.claude/commands/` — slash commands for weekly runs and monthly newsletter

## Domains

| Key | Domain |
|-----|--------|
| `ai-marketing` | AI & Marketing (ChatGPT subreddits + digital marketing) |
| `paid-media` | Paid Media & PPC (Google/Facebook Ads, PPC, advertising) |
| `web-wordpress` | Web & WordPress (WordPress ecosystem subreddits) |
| `real-estate` | Real Estate (investing, Realtors, mortgages, landlord) |

## Weekly Workflow

Run once per domain each week (Monday recommended):

```bash
claude "/weekly-intel ai-marketing"
claude "/weekly-intel paid-media"
claude "/weekly-intel web-wordpress"
claude "/weekly-intel real-estate"
```

Or headless with JSON output for automation:

```bash
claude -p "/weekly-intel ai-marketing" --output-format json
```

## Monthly Newsletter

Run once per month after all four domains have 4 weeks of entries in Notion:

```bash
claude "/monthly-newsletter"
```

## Notion Setup

Requires Notion MCP connected via:

```bash
claude mcp add notion
```

Two Notion databases are expected:
- **Marketing Intelligence** — weekly intel entries (Title, Domain, Raw Text, Week, page body)
- **Monthly Newsletter** — monthly drafts (Title, Content)

## Output Rules

All analysis output must be:
- Plain text only (no Markdown, emojis, or tables)
- 1,000–3,500 words per weekly report
- Exactly 15 distinct takeaways
- Subreddit attribution preserved on every referenced post
