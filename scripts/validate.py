#!/usr/bin/env python3
"""Check source contracts, rendered pages, and every local link before review."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist'
errors = []

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []
        self.h1 = self.main = self.current = self.publications = 0
        self.language = None
        self.lang_switch = None
        self.nav_count = 0
        self.in_nav = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.language = a.get('lang')
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if 'id' in a:
            if a['id'] in self.ids: errors.append('Duplicate id: '+a['id'])
            self.ids.add(a['id'])
        if a.get('aria-current') == 'page': self.current += 1
        if tag == 'nav' and a.get('id') == 'primary-nav': self.in_nav = True
        if tag == 'a' and self.in_nav: self.nav_count += 1
        if 'publication' in a.get('class','').split(): self.publications += 1
        if 'language-switch' in a.get('class','').split(): self.lang_switch = a.get('href')
        if tag == 'img' and not a.get('alt'): errors.append('Image without descriptive alt text')
        for field in ('href','src'):
            if a.get(field): self.references.append(a[field])
    def handle_endtag(self, tag):
        if tag == 'nav': self.in_nav = False

site = json.loads((ROOT/'content/site.json').read_text())
assert set(site) == {'en','ja'}
assert set(site['en']) == set(site['ja']), 'English/Japanese key mismatch'
for language, words in site.items():
    assert len(words['nav']) == 5
    assert all(value for value in words.values()), 'Empty translated string'
research = json.loads((ROOT/'content/research.json').read_text())
for record in research['themes'] + research['projects']:
    assert record['en'].keys() == record['ja'].keys(), 'Unpaired research translation'
pubs = json.loads((ROOT/'content/publications.json').read_text())['records']
assert len({p['id'] for p in pubs}) == len(pubs), 'Repeated publication ID'
for p in pubs:
    assert p['citation'] and p['category']
    assert p['year'] == '' or re.fullmatch(r'\d{4}(?:-\d{4})?',p['year'])

files = sorted(OUT.rglob('*.html'))
assert len(files) == 10, 'Expected exactly 10 generated pages'
documents = {}
for path in files:
    d = Document(); d.feed(path.read_text(encoding='utf-8')); documents[path.resolve()] = d
    if (d.h1,d.main,d.current,d.nav_count) != (1,1,1,5): errors.append(str(path.relative_to(OUT))+': invalid heading, main or five-page navigation')
    if d.language != ('ja' if path.relative_to(OUT).parts[0]=='ja' else 'en'): errors.append('Incorrect document language')
    if 'publications' in path.parts and d.publications != len(pubs): errors.append('Bibliography incomplete')
    if not d.lang_switch: errors.append('Missing language switch')

checked = 0
for path,d in documents.items():
    for reference in d.references:
        u=urlsplit(reference)
        if u.scheme or u.netloc: continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        if target.is_dir(): target=target/'index.html'
        if not target.exists(): errors.append(str(path.relative_to(OUT))+': missing '+reference)
        elif u.fragment and target.suffix=='.html' and u.fragment not in documents[target].ids: errors.append('Missing anchor: '+reference)
        checked+=1
    alternate=(path.parent/d.lang_switch).resolve()
    if alternate in documents:
        back=(alternate.parent/documents[alternate].lang_switch).resolve()
        if back != path: errors.append('Language switch does not preserve page')
for path in files:
    if 'info@birlab.org' in path.read_text(): errors.append('Unverified placeholder email')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: 10 pages; five-page navigation; reciprocal EN/JA links; '+str(checked)+' local references; '+str(len(pubs))+' bibliography entries per language; translated content contracts.')
