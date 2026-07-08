---
name: home-custom-recommender
description: Recommend suitable whole-home customization, cabinet, storage, or interior design vendors from a creator-maintained vetted spreadsheet. Use when a user wants help choosing a reliable full-home custom furniture/design company, avoiding low-price traps or false advertising, matching vendors by city/region, budget, style, materials, project scope, timeline, and service preference, or turning a vetted vendor table into personalized recommendations. Ask detailed questions first, filter and score the spreadsheet, then perform a fresh web check for recent public information before giving a balanced recommendation.
---

# Home Custom Recommender

## Overview

Use the creator's vetted vendor spreadsheet as the trusted candidate pool. The goal is not to prove that one vendor is universally best; the goal is to identify which vetted vendors fit this specific renovation case, then check recent public signals before recommending.

## Workflow

1. Use the bundled official vendor table at `assets/default-vendors.csv` unless the creator/maintainer explicitly provides a newer official data file. Do not ask ordinary end users to replace the table.
2. If the user provides new raw sources for the creator's database, read `references/datasource-maintenance.md` and normalize them into the shared schema before recommending.
3. Read `references/interview-guide.md` before interviewing the user. Ask questions in small batches, but be thorough enough to understand region, project scope, budget, style, materials, timeline, service expectations, and dealbreakers.
4. Read `references/table-schema.md` when mapping the spreadsheet's columns. Normalize obvious Chinese column aliases instead of forcing an exact schema.
5. Read `references/recommendation-rubric.md` before ranking and writing the final answer.
6. Filter hard mismatches first: no service coverage, unavailable project type, budget far outside fit, timeline impossible, or explicit dealbreakers.
7. Score the remaining candidates by fit. Use `scripts/rank_vendors.py` when the table is available as CSV and the user's answers can be summarized as JSON; otherwise score manually with the rubric.
8. Shortlist 2-5 candidates. Before finalizing, use an available web-search/browsing skill or tool, such as `firecrawl-search` when available, to check recent public information for each shortlisted vendor.
9. Recommend 1-3 vendors. Explain fit, tradeoffs, what to verify in consultation, and why other plausible candidates were not the top match.

## Interview Rules

Do not jump straight to recommendations from city and budget alone. Ask follow-up questions when the user's answer is vague, contradictory, or too broad.

Required minimum before ranking:

- City plus district or nearby city acceptance.
- New build, second-hand renovation, partial renovation, or existing-home upgrade.
- Home size, room count, and whether drawings/measurements exist.
- Customization scope, such as kitchen cabinets, wardrobes, whole-house cabinets, storage planning, wood doors, wall panels, or design-only service.
- Budget range for custom cabinetry/design separately from total renovation budget.
- Top priorities and hard dealbreakers.
- Preferred style and tolerance for design experimentation.
- Materials/environmental expectations and household constraints, such as children, elderly family members, pets, allergies, or urgent move-in.
- Timeline and acceptable communication/service model.

## Spreadsheet Handling

Treat the bundled table as the curated official candidate pool. Prefer rows with clear source notes, recent verification dates, service area, strengths, caveats, and budget positioning.

If a row has `record_type=external_note`, use it as background/source context only. Do not recommend it as a merchant. If a row has `record_type=vendor`, it may enter the recommendation pool even when some fields are blank; handle low-confidence rows with extra verification and cautious language.

If spreadsheet cells contain qualitative notes, preserve nuance. For example, "strong design but slower communication" is not a negative for every user; it matters more for users with tight timelines or low tolerance for follow-up.

Do not expose private contact information or unpublished notes unless the user explicitly says the table is meant for that recipient.

## Recent Web Check

For each shortlisted vendor, search recent public sources before final recommendation. Look for:

- Official site, social accounts, showroom/store updates, and current service area.
- Recent reviews, disputes, complaint posts, or delivery/install issues.
- Business status signals when available, such as name changes, abnormal operation notices, litigation, or closure.
- Whether negative reports are credible, repeated, recent, and relevant to the user's project.

Do not overreact to a single vague complaint. Do downgrade candidates for repeated recent complaints about the exact risk the user cares about, such as delays, add-on charges, design non-responsiveness, installation quality, or after-sales avoidance.

## Final Answer Shape

Write in Chinese unless the user asks otherwise. Be frank and useful:

- Lead with the best-fit recommendation.
- Give 1-2 alternatives when useful.
- Explain "why this fits you" and "what to watch."
- Include consultation questions the user should ask the vendor.
- Make clear that the table is already pre-vetted, so the distinction is fit and recent risk, not absolute safety guarantees.
