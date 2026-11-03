#!/usr/bin/env python3
"""Import an explicitly supplied copy of the existing BIRL publication page."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path

class BibliographyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.heading = None
        self.text = ''
        self.in_item = False
        self.links = []
        self.category = 'Under Review'
        self.year = ''
        self.records = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'div' and 'entry-content' in attrs.get('class', '').split():
            self.active = True
        if not self.active:
            return
        if tag in ('h2', 'h3', 'h4', 'h5', 'h6'):
            self.heading, self.text = tag, ''
        if tag == 'li':
            self.in_item, self.text, self.links = True, '', []
        if self.in_item and tag == 'a' and attrs.get('href', '').startswith(('https://', 'http://')):
            self.links.append(attrs['href'])

    def handle_data(self, data):
        if self.active and (self.heading or self.in_item):
            self.text += data

    def handle_endtag(self, tag):
        if tag == self.heading:
            value = ' '.join(self.text.split())
            if value == 'Share this:':
                self.active = False
            elif re.fullmatch(r'\d{4}(?:-\d{4})?', value):
                self.year = value
            elif value:
                self.category, self.year = value, ''
            self.heading, self.text = None, ''
        if tag == 'li' and self.in_item:
            citation = ' '.join(self.text.split())
            if self.active and citation:
                match = re.search(r'\b(?:19|20)\d{2}\b', citation)
                year = self.year or (match.group(0) if match else '')
                if self.category == 'Under Review':
                    year = ''
                self.records.append(dict(id='publication-' + str(len(self.records) + 1),
                    year=year, category=self.category, citation=citation, links=self.links))
            self.in_item = False
        if tag == 'article':
            self.active = False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('html', type=Path)
    parser.add_argument('--checked', required=True, help='Date on which source was read, YYYY-MM-DD')
    args = parser.parse_args()
    importer = BibliographyParser()
    importer.feed(args.html.read_text(encoding='utf-8'))
    if len(importer.records) < 100:
        raise SystemExit('Unexpected source structure: refusing to replace the bibliography')
    output = Path(__file__).resolve().parent.parent / 'content/publications.json'
    output.write_text(json.dumps(dict(source='https://birlab.org/publications/',
        checked=args.checked, records=importer.records), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Imported', len(importer.records), 'publication records')
