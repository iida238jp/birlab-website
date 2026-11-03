# Updating the website

The content is plain UTF-8 JSON. English and Japanese pages are built from the same records, so a layout change applies to both languages.

## Typical AI-assisted requests

- “Add this confirmed paper and DOI to the bibliography, preserving the citation supplied by the publisher. Build and validate the site; show the changed record for review.”
- “Add this member with the supplied role and affiliation. Update both language views, keeping their name in its preferred spelling. Do not infer an email address.”
- “Replace the homepage news item with this announcement, including the actual event date and source. Write the English and Japanese versions.”
- “Add this project with the supplied image and credit. State its actual status; do not describe archived work as ongoing.”

Use a separate branch, provide sources, and review the result before merging. A safe update should usually change JSON only.

## Add a publication

Append or insert a record in `content/publications.json`:

```json
{
  "id": "unique-stable-id",
  "year": "2026",
  "category": "Journal Papers",
  "citation": "Exact confirmed citation, including status if applicable.",
  "links": ["https://doi.org/CONFIRMED-DOI"]
}
```

Use an empty year if unknown. Use an existing category so it has a Japanese label. Published paper titles remain in their original language. Only add real DOI or publisher URLs; a paper without a confirmed link may have an empty `links` array. Preserve IDs after publication because they are fragment links.

To deliberately reimport the old website, first save a reviewed copy of its HTML, then run:

```sh
python3 scripts/import_publications.py /path/to/publications.html --checked YYYY-MM-DD
```

This replaces the bibliography and regenerates sequential IDs; it is a migration tool, not a routine update command. Review the entire diff, reconcile curated corrections, and preserve IDs before committing. No automatic fetching or publishing takes place.

## Add people, research, or images

`people.json` stores a source URL, check date, role translations, and members grouped by campus. Update the check date only when the underlying source has been checked. New roles need both `en` and `ja` labels.

`research.json` pairs the English and Japanese text for every theme and project. A project needs a stable ID, image, bilingual alt text, source URL, and both language fields. Update the homepage selection in `build.py` if its two highlighted projects should change.

Add image files to `assets/` and record their source URL, description, credit, retrieval date, pixel width, and pixel height in `assets/sources.json`. The builder uses this metadata for stable image dimensions. Retain original attribution and verify rights for any newly introduced material.

## Review and deploy later

1. Run the build and validator in the README.
2. Review both languages; check links, keyboard use, narrow screen layout, and any affected filters.
3. Open a review pull request. Its workflow provides a downloadable `birl-review-preview` artifact.
4. After explicit deployment authorization, upload only the contents of `dist/` to the chosen staging or production host. This branch intentionally has no automatic deployment.

Before replacing BIRLab.org, decide the hosting/domain plan and preserve the legacy WordPress URLs and archive. Add production canonical URLs and a sitemap once the final origin is confirmed; do not point preview metadata at a production page. Preserve external archive URLs until an approved migration makes local replacements available.
