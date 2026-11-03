# BIRL redesign review

## Direction and implementation

The starting repository contained an English single-page prototype with three research themes, placeholder contact details, and no image library. It had no GitHub Pages site enabled when inspected on 3 November 2026.

The redesign keeps the green palette and “Understanding Intelligence Through the Body” supporting message, with “Bio-Inspired Robotics Laboratory” as the main homepage headline, introduces documentary imagery from the existing website, and presents Home plus five menu destinations in English and Japanese: Research, People, Publication, Community, and Join. It uses large editorial typography, dark green section introductions, quiet surfaces, and lime accents. Both languages share layouts and data.

Home introduces the embodied intelligence perspective, three connected research themes, two project examples, the Tokyo branch announcement, and a route into collaboration. Research explains the body–brain–environment relationship and retains five representative project examples. People contains the PI and 15 directory entries grouped by campus, and a link to Community. Publications retains 431 source entries with search, year, and type filters, an accessible result count, reset, and an empty state. Community brings together the historically labelled reunion image, alumni archive, and news/events links. Join uses published PI emails, university information, and the existing enquiry form.

No contact submission backend, analytics, accounts, automatic content generation, or deployment integration has been added. The original prototype is retained in `docs/prototype/`.

## Preservation and sources

All sources were read on 3 November 2026:

- https://github.com/iida238jp/birlab-website — original prototype, base commit `887ed30`.
- https://birlab.org/ — institutional description, Tokyo announcement, robotic-hand photograph, and BIRL logo.
- https://birlab.org/research/ — representative projects and research images.
- https://birlab.org/members/ — PI, campus groups, roles, public email components, historical reunion image, and full alumni archive.
- https://birlab.org/publications/ — the 431 imported bibliography records and their supplied links.
- https://birlab.org/contact/ — Cambridge address, visitor directions, and working enquiry form target.

Seven existing image assets are stored locally (six photographs/research images plus the logo); provenance and dimensions are in `assets/sources.json`. Existing rights remain with the original creators. The BIRL logo is retained; no institutional crests or invented endorsements are added. The original website, research archive, news/events, resources, alumni, and YouTube channel remain linked.

The prototype’s unverified `info@birlab.org` address and unsubstantiated project-specific claims have been removed from the new site. The archived prototype still documents the starting state.

## Editorial limits before production

The bibliography is a faithful migration of source entries, not an independent verification of every publication. It includes source duplicates, spelling/encoding issues, status changes, and year disagreements. For example, some journal items are grouped under one year while citing another; older journal records have a source group of `1999-2011`. These have not been silently rewritten. Undated conference/report entries get a search year from the first year in the citation where available. Review and correct these records against publisher sources before treating them as a definitive scholarly database.

Member roles follow the existing directory, whose freshness has not been independently confirmed. The Japanese prose is a new translation for editorial review; names and paper titles retain their original spelling. The Tokyo street address and current vacancies have not been invented. Archived project examples are explicitly labelled, rather than presented as a current funded-project list. The group photograph is labelled December 2023, not presented as a current team portrait.

This redesign does not replace the deep WordPress project, event, alumni, media, or resource archives. A future domain migration needs a URL-by-URL redirect/archive plan. Confirm the bilingual copy, membership, institutional wording, image attribution, contact routing, and host configuration before production deployment.

## Verification

The dependency-free validator checks twelve rendered pages, five primary navigation links visible on both desktop and mobile, one current-page link, one H1 and main landmark, reciprocal page-preserving language switches, local files and fragments, image descriptions, complete bibliography output, translated content keys, and removal of the placeholder email. Browser checks cover representative desktop and narrow mobile views and search/filter/reset interactions. A separate verification report accompanies the delivered preview.
