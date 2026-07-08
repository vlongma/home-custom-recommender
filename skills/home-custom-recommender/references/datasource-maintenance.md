# Data Source Maintenance

Use this reference when the creator provides new PDFs, spreadsheets, screenshots, web links, social posts, or notes to add to the vetted vendor database.

## Source types

- Use `vendor` records for concrete merchants with enough details to recommend.
- Use `external_note` records for articles, posts, screenshots, comments, rating rubrics, complaints, or partial leads that should inform later verification but are not yet complete vendor rows.

## Required source tracking

Every row should preserve:

- `source_name`
- `source_type`
- `source_path_or_url`
- `source_author`
- `source_date`
- `source_page_or_rows`
- `source_confidence`
- `raw_text`

Never flatten away the source. Recommendations must be traceable.

## Skill-ready fields

Maintain these fields so `scripts/rank_vendors.py` and future recommendation flows can use the data directly:

- `vendor_name`
- `service_area`
- `scope`
- `budget_positioning`
- `design_style`
- `materials`
- `environmental_standard`
- `typical_timeline`
- `strengths`
- `caveats`
- `source_notes` or `creator_comment`

## Normalization rules

Preserve original wording in detailed fields, then add normalized tags. For example, keep the exact board-material list, but also fill `materials` and `environmental_standard` with searchable terms.

If the source only gives a contact person or door-store number, leave `vendor_name` blank and put the original label in `vendor_label`. Do not invent a brand name.

If the source is a social post with images that cannot be fully extracted, create an `external_note` record and ask for screenshots or original files when exact table data is needed.

## Quality checks

Before treating a new row as recommendation-ready, check:

- City and district are clear.
- Scope is specific enough to match user needs.
- Budget positioning or starting price is present.
- Materials, hardware, or process data are present.
- At least one strength and one caveat/consultation reminder are recorded.
- Source and raw text are preserved.

