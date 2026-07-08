# Data

This folder contains a public-friendly copy of the official vendor dataset.

- `whole-home-customization-vendors.public.csv`: official data copy for GitHub preview.
- `whole-home-customization-vendors.public.json`: same records for programmatic use.
- `whole-home-customization-vendors.public.xlsx`: spreadsheet version for maintainer review.

The installed skill uses `skills/home-custom-recommender/assets/default-vendors.csv` as its bundled official table. Ordinary users should not replace the table; they should update by downloading the latest release.

Use `record_type=vendor` for merchants that should enter the recommendation pool.

Use `record_type=external_note` for search pages, posts, screenshots, comments, or partial evidence that should be preserved but not directly recommended as a merchant.
