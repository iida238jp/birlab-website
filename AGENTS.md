# Editing the BIRL website

- Work on a review branch. Do not deploy, merge, edit DNS, or overwrite the live WordPress site without the user's explicit instruction.
- Read `docs/REDESIGN.md` and `docs/UPDATING.md` before content changes.
- Treat `content/*.json` as the source of truth. Keep English and Japanese fields paired. Do not edit generated `dist/` files directly.
- Preserve the five primary menu destinations (Research, People, Publication, Community, Join), the separate homepage, and reciprocal language links.
- Verify people, affiliations, dates, contact information, publication details, and opportunities against supplied evidence or primary sources. Keep source URLs. Never invent vacancies, funding, metrics, paper links, or project status.
- Preserve existing image credits and provenance. Do not substitute generated illustrations for documentary research images without a request.
- Keep the site static and dependency-free unless a real requirement calls for a change. Never add credentials, analytics, submission endpoints, or paid services implicitly.
- Run `python3 scripts/build.py` and `python3 scripts/validate.py` after changes. For layout or interaction changes, also check representative desktop and narrow mobile views, both languages, and publication search / filters / reset.
- A check passing verifies structure, not the truth or current status of research claims. Report source uncertainty in the review.
