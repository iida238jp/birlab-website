# BIRL website redesign

A bilingual redesign of the Bio-Inspired Robotics Laboratory website, based on the original prototype in this repository and content retained from [BIRLab.org](https://birlab.org/). The homepage headline is **Bio-Inspired Robotics Laboratory**, with **Understanding Intelligence Through the Body** as its supporting message.

This branch is for review. It does not deploy, change the domain, or replace the live WordPress site.

## Preview

Python 3.8+ is the only build requirement. No packages, accounts, API keys, or external fonts are needed.

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:8000/` for English or `http://127.0.0.1:8000/ja/` for Japanese. A downloaded `dist` preview also works by opening its `index.html` directly. Only publication filtering needs JavaScript; content and navigation remain available without it.

## Five menu destinations and Home

| Page | English | Japanese |
| --- | --- | --- |
| Home | `/` | `/ja/` |
| Research | `/research/` | `/ja/research/` |
| People | `/people/` | `/ja/people/` |
| Publications | `/publications/` | `/ja/publications/` |
| Community | `/community/` | `/ja/community/` |
| Join | `/join/` | `/ja/join/` |

The language switch preserves the page. Paths are relative, so the output also works under a GitHub project subdirectory.

## Easy updates

| Change | Edit |
| --- | --- |
| General copy, navigation, homepage news | `content/site.json` (paired `en` / `ja` entries) |
| Research themes and project examples | `content/research.json` |
| Members, roles, PI contacts | `content/people.json` |
| Bibliography | `content/publications.json` |
| Photographs and provenance | `assets/` and `assets/sources.json` |
| Layout | `scripts/build.py` |
| Appearance and interactions | `static/style.css`, `static/site.js` |

Build and validate after each edit. The GitHub check runs the same steps and uploads a downloadable preview; it has no deployment permissions or deployment step. See [the update guide](docs/UPDATING.md) for examples and [the redesign review](docs/REDESIGN.md) for scope, verification, and pre-deployment decisions.

The original three-file prototype is retained in `docs/prototype/` and Git history. The generated `dist/` folder is intentionally untracked.
