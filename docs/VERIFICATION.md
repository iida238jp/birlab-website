# Verification — 3 November 2026

The redesign was checked before any production deployment.

| Check | Result |
| --- | --- |
| Build using Python 3.8 standard library | Pass — ten static HTML pages |
| English/Japanese content keys and research field pairs | Pass |
| Five navigation links, one current-page marker, one H1/main per page | Pass |
| Reciprocal language switches preserving the page | Pass |
| Local file and fragment references | Pass — 194 checked |
| Bibliography completeness | Pass — 431 entries in each language |
| Descriptive image alternatives and no placeholder email in generated pages | Pass |
| Desktop browser layout | Pass — all ten pages checked at 1440px; no horizontal overflow or observed failed images |
| Narrow browser layout | Pass — all ten pages checked at 319px; Publications title sizing corrected and rechecked at 319px |
| English combined search/type/year filters | Pass — “soft” + 2025 + Journal Papers returns three matching entries |
| Search empty state and reset | Pass — nonexistent query produces an empty state; reset restores 431 entries |
| Japanese search/reset | Pass — “morphologies” returns one entry; reset restores 431 |
| Language switching from Publications | Pass — reaches the corresponding Japanese Publications page |
| Mobile menu and Escape key | Pass — menu expands, links appear, Escape closes it |
| Console errors during final interaction checks | None observed |
| Git whitespace check | Pass |

This is structural and representative browser verification, not a full accessibility certification or a manual check of hundreds of external legacy paper links. Bibliography status/year discrepancies and source encoding issues are retained and documented in `REDESIGN.md`; the Japanese text and current team details need editorial review before production.

## Headline and menu revision

The homepage headline is now “Bio-Inspired Robotics Laboratory”, with the embodied-intelligence statement as supporting copy. Five always-visible primary links lead to Research, People, Publication, Community, and Join. The homepage also has a prominent five-link directory, and the BIRL logo links home. Community has paired English/Japanese pages. The validator now covers twelve pages and 238 local references. The collapsible mobile menu from the original preview has been replaced by visible navigation.

Revision verification: the twelve-page build and 238 local references pass. The revised English homepage and both Community pages were checked in the browser, including the five visible menu links and reciprocal language switch. Publication search and reset still return the expected one result and full 431-entry list. The browser viewport override did not reliably apply the requested phone size during this revision; narrow mobile rendering of the new always-visible menu still needs a visual check.
