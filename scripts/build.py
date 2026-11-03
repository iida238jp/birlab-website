#!/usr/bin/env python3
"""Build ten portable, fully rendered pages using only Python's standard library."""
import argparse
import html
import json
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ('home', 'research', 'people', 'publications', 'join')
SLUGS = {'home': '', 'research': 'research', 'people': 'people', 'publications': 'publications', 'join': 'join'}

def read(name):
    return json.loads((ROOT / 'content' / (name + '.json')).read_text(encoding='utf-8'))

def esc(value):
    return html.escape(str(value), quote=True)

SITE, RESEARCH, PEOPLE, PUBLICATIONS = (read(n) for n in ('site', 'research', 'people', 'publications'))
ASSETS = {a['file']: a for a in json.loads((ROOT/'assets/sources.json').read_text(encoding='utf-8'))}

class Page:
    def __init__(self, lang, page):
        self.lang, self.page = lang, page
        self.words = SITE[lang]
        self.directory = Path('ja' if lang == 'ja' else '') / SLUGS[page]

    def t(self, key):
        return esc(self.words[key])

    def path(self, target):
        # Relative paths also work under GitHub project Pages and in a downloaded preview.
        result = os.path.relpath(str(target) or '.', str(self.directory) or '.').replace(os.sep, '/')
        return result if result != '.' else './'

    def url(self, page, lang=None):
        target = Path('ja' if (lang or self.lang) == 'ja' else '') / SLUGS[page] / 'index.html'
        return self.path(target)

    def link(self, href, label, css='text-link'):
        return '<a class="{}" href="{}">{} <span aria-hidden="true">↗</span></a>'.format(css, esc(href), label)

    def button(self, page, key):
        return self.link(self.url(page), self.t(key), 'button')

    def image(self, file, alt, css='', eager=False):
        asset = ASSETS[file]
        loading = 'fetchpriority="high"' if eager or file == 'birl-logo.png' else 'loading="lazy"'
        return '<img class="{}" src="{}" alt="{}" width="{}" height="{}" {} decoding="async">'.format(esc(css), esc(self.path(Path('assets') / file)), esc(alt), asset['width'], asset['height'], loading)

    def section_head(self, label, title, link=''):
        return '<div class="section-head"><div><p class="eyebrow">{}</p><h2>{}</h2></div>{}</div>'.format(self.t(label), self.t(title), link)

    def intro(self, label, title, text):
        return '<section class="page-intro"><div class="wrap"><p class="eyebrow">{}</p><h1>{}</h1><p class="lead">{}</p></div></section>'.format(self.t(label), self.t(title), self.t(text))

    def themes(self):
        result = []
        for theme in RESEARCH['themes']:
            d = theme[self.lang]
            result.append('<article class="theme" id="{}"><span class="theme-number">{}</span><h3>{}</h3><p class="question">{}</p><p>{}</p></article>'.format(theme['id'], theme['number'], esc(d['title']), esc(d['question']), esc(d['text'])))
        return '<div class="themes">' + ''.join(result) + '</div>'

    def project(self, project, compact=False):
        d = project[self.lang]
        picture = self.image(project['image'], project['alt'][self.lang])
        if compact:
            href = self.url('research') + '#' + project['id']
            return '<article class="project-tile"><a class="image-link" href="{}">{}</a><p class="eyebrow">{}</p><h3><a href="{}">{}</a></h3><p>{}</p>{}</article>'.format(href, picture, esc(d['tag']), href, esc(d['title']), esc(d['text']), self.link(href, self.t('readProject')))
        return '<article class="project-row" id="{}"><figure>{}<figcaption>{}</figcaption></figure><div><p class="eyebrow">{}</p><h3>{}</h3><p>{}</p>{}</div></article>'.format(project['id'], picture, self.t('imageCredit'), esc(d['tag']), esc(d['title']), esc(d['text']), self.link(project['source'], self.t('archiveResearch')))

    def closing(self):
        return '<section class="closing"><div class="wrap"><p class="eyebrow">BIRL / BIO-INSPIRED ROBOTICS LABORATORY</p><h2>{}</h2><p>{}</p>{}</div></section>'.format(self.t('closingTitle'), self.t('closingText'), self.button('join', 'closingLink'))

    def community(self):
        return '<figure class="community-photo">{}<figcaption>{}</figcaption></figure>'.format(self.image('community.jpg', self.words['communityCaption']), self.t('communityCaption'))

    def home(self):
        lines = self.words['heroLines']
        heading = '<br>'.join('<span{}>{}</span>'.format(' class="accent-word"' if i == 1 else '', esc(line)) for i, line in enumerate(lines))
        hero = '<section class="hero"><div class="hero-copy"><p class="eyebrow">{}</p><h1>{}</h1><p class="hero-intro">{}</p><div class="hero-actions">{}{}</div><p class="hero-affiliation">{}</p></div><figure class="hero-figure">{}<figcaption><span>01 / BIRL IN MOTION</span><p>{}</p></figcaption></figure></section>'.format(self.t('heroLabel'), heading, self.t('heroIntro'), self.button('research','explore'), self.link(self.url('people'),self.t('meet')), self.t('affiliation'), self.image('robotic-hand.jpg', RESEARCH['projects'][0]['alt'][self.lang], eager=True), self.t('heroCaption'))
        vision = '<section class="section wrap vision"><p class="eyebrow">{}</p><div><h2>{}</h2><p class="lead">{}</p>{}</div></section>'.format(self.t('visionLabel'), self.t('visionTitle'), self.t('visionText'), self.link(self.url('research')+'#embodied-intelligence', self.t('visionLink')))
        themes = '<section class="section section-tint"><div class="wrap">{}{}</div></section>'.format(self.section_head('themeLabel', 'themeTitle'), self.themes())
        projects = '<section class="section wrap">{}<div class="project-tiles">{}</div></section>'.format(self.section_head('selectedLabel','selectedTitle', self.link(self.url('research'), self.t('allResearch'))), ''.join(self.project(p,True) for p in RESEARCH['projects'][:2]))
        news = '<section class="section wrap news">{}<article><time datetime="2025-10-01">{}</time><h3>{}</h3><p>{}</p>{}</article></section>'.format(self.section_head('newsLabel','newsTitle'),self.t('newsDate'),self.t('newsHeadline'),self.t('newsText'),self.link('https://birlab.org/news/',self.t('newsLink')))
        return hero + vision + themes + projects + news + self.closing()

    def research(self):
        return self.intro('researchLabel','researchTitle','researchIntro') + '<section class="section wrap vision"><p class="eyebrow">{}</p><div><h2>{}</h2><p class="lead">{}</p></div></section><section class="section-tint section"><div class="wrap">{}</div></section><section class="section wrap">{}<p class="section-note">{}</p><div class="projects">{}</div></section>'.format(self.t('questionLabel'),self.t('questionTitle'),self.t('questionText'),self.themes(),self.section_head('projectsLabel','projectsTitle'),self.t('projectsNote'),''.join(self.project(p) for p in RESEARCH['projects'])) + self.closing()

    def people(self):
        pi = PEOPLE['pi']
        lead = '<section class="section wrap pi"><div class="pi-monogram" aria-hidden="true">FI<span>BIRL / PI</span></div><div><p class="eyebrow">{}</p><h2>{}</h2><p class="lead">{}</p>{}</div></section>'.format(self.t('piLabel'),esc(pi['name']),self.t('piText'),self.link(pi['profile'],self.t('profile')))
        locations = []
        for loc in ('tokyo','cambridge'):
            groups = []
            for role, translations in PEOPLE['roles'].items():
                members = [m for m in PEOPLE['members'] if m['location']==loc and m['role']==role]
                if members:
                    groups.append('<div class="people-group"><h4>{}</h4><ul>{}</ul></div>'.format(esc(translations[self.lang]),''.join('<li>'+esc(m['name'])+'</li>' for m in members)))
            locations.append('<article class="location-list"><p class="eyebrow">{}</p><h3>{}</h3>{}</article>'.format('JP / TOKYO' if loc=='tokyo' else 'UK / CAMBRIDGE',self.t(loc),''.join(groups)))
        directory = '<section class="section section-tint"><div class="wrap">{}<p class="section-note">{}</p><div class="directory">{}</div></div></section>'.format(self.section_head('directoryLabel','directoryTitle'),self.t('directoryNote'),''.join(locations))
        history = '<section class="section wrap">{}<div class="history-copy"><h2>{}</h2><div><p>{}</p>{}</div></div></section>'.format(self.community(),self.t('alumniTitle'),self.t('alumniText'),self.link('https://birlab.org/members/',self.t('alumniLink')))
        return self.intro('peopleLabel','peopleTitle','peopleIntro') + lead + directory + history + self.closing()

    def publications(self):
        records = PUBLICATIONS['records']
        years = sorted({r['year'] for r in records if r['year']}, reverse=True)
        categories = list(dict.fromkeys(r['category'] for r in records))
        labels = {'Under Review':'査読中','Journal Papers':'学術誌論文','Book Chapters':'書籍の章','Reviewed Conference Papers':'査読付き国際会議論文','Workshop Contributions and Others':'ワークショップ・その他','Thesis / Project Reports':'学位論文・プロジェクト報告'}
        def category(value): return labels.get(value,value) if self.lang=='ja' else value
        controls = '<form class="publication-filters" id="publication-filters" role="search"><div class="search-control"><label for="publication-search">{}</label><input id="publication-search" type="search" placeholder="{}" autocomplete="off"></div><div><label for="publication-year">{}</label><select id="publication-year"><option value="">{}</option>{}</select></div><div><label for="publication-type">{}</label><select id="publication-type"><option value="">{}</option>{}</select></div><button type="reset" class="reset">{}</button></form>'.format(self.t('searchLabel'),self.t('searchPlaceholder'),self.t('yearLabel'),self.t('allYears'),''.join('<option>'+esc(y)+'</option>' for y in years),self.t('typeLabel'),self.t('allTypes'),''.join('<option value="{}">{}</option>'.format(esc(c),esc(category(c))) for c in categories),self.t('reset'))
        rows = []
        for r in records:
            links = ''.join(self.link(u,self.t('paper') + (' '+str(i+1) if len(r['links'])>1 else ''), 'paper-link') for i,u in enumerate(r['links']))
            rows.append('<li class="publication" id="{}" data-year="{}" data-type="{}"><div class="publication-meta"><span>{}</span><span>{}</span></div><div><p>{}</p><div class="paper-links">{}</div></div></li>'.format(esc(r['id']),esc(r['year']),esc(r['category']),esc(r['year']) if r['year'] else self.t('undated'),esc(category(r['category'])),esc(r['citation']),links))
        contents = '<section class="section wrap publications-section"><div class="bibliography-note"><p>{}</p>{}</div>{}<noscript><p>{}</p></noscript><p class="result-count" role="status" aria-live="polite" aria-atomic="true"><span id="result-count">{}</span> / {} {}</p><p id="no-results" hidden>{}</p><ol class="publication-list">{}</ol></section>'.format(self.t('publicationNote'),self.link(PUBLICATIONS['source'],self.t('originalBibliography')),controls,('Filtering requires JavaScript; the complete bibliography is shown below.' if self.lang=='en' else '絞り込みにはJavaScriptが必要です。文献一覧は下にすべて表示されています。'),len(records),len(records),self.t('showing'),self.t('noResults'),''.join(rows))
        return self.intro('publicationsLabel','publicationsTitle','publicationsIntro') + contents

    def join(self):
        pi=PEOPLE['pi']
        paths = '<section class="section wrap join-paths"><article><p class="eyebrow">01 / RESEARCH</p><h2>{}</h2><p>{}</p></article><article><p class="eyebrow">02 / COLLABORATION</p><h2>{}</h2><p>{}</p></article></section>'.format(self.t('studentsTitle'),self.t('studentsText'),self.t('collaborateTitle'),self.t('collaborateText'))
        contact = '<section class="section contact-callout"><div class="wrap"><h2>{}</h2><p class="lead">{}</p>{}</div></section>'.format(self.t('contactTitle'),self.t('contactText'),self.link('https://birlab.org/contact/#contact-form-2',self.t('contactForm'),'button'))
        locations = '<section class="section wrap directory contact-locations"><article><p class="eyebrow">JP / TOKYO</p><h2>{}</h2><p>{}<br>{}</p><a class="email" href="mailto:{}">{}</a><p>{}</p>{}</article><article><p class="eyebrow">UK / CAMBRIDGE</p><h2>{}</h2><p>{}<br>Trumpington Street<br>Cambridge CB2 1PZ, United Kingdom</p><a class="email" href="mailto:{}">{}</a><p>{}</p>{}</article></section>'.format(self.t('tokyo'),self.t('tokyoDept'),self.t('tokyo'),esc(pi['tokyoEmail']),esc(pi['tokyoEmail']),self.t('tokyoVisit'),self.link('https://www.pe.t.u-tokyo.ac.jp/',self.t('deptLink')),self.t('cambridge'),self.t('cambridgeDept'),esc(pi['cambridgeEmail']),esc(pi['cambridgeEmail']),self.t('cambridgeVisit'),self.link('https://map.cam.ac.uk/Department+of+Engineering',self.t('map')))
        return self.intro('joinLabel','joinTitle','joinIntro')+paths+contact+locations

    def render(self):
        other = 'ja' if self.lang=='en' else 'en'
        nav = ''.join('<a href="{}" {}>{}</a>'.format(self.url(p),'aria-current="page"' if p==self.page else '',esc(self.words['nav'][i])) for i,p in enumerate(PAGES))
        language = '<a class="language-switch" href="{}" lang="{}" hreflang="{}" aria-label="{}">{}</a>'.format(self.url(self.page,other),other,other,self.t('languageLabel'),'日本語' if other=='ja' else 'EN')
        header = '<a class="skip-link" href="#main">{}</a><header class="site-header"><div class="header-inner"><a class="brand" href="{}" aria-label="BIRL — {}">{}<span>{}</span></a><button class="menu-toggle" aria-expanded="false" aria-controls="primary-nav" data-open="{}" data-close="{}">{}</button><nav id="primary-nav" aria-label="{}">{}</nav>{}</div></header>'.format(self.t('skip'),self.url('home'),esc(self.words['nav'][0]),self.image('birl-logo.png','BIRL'),self.t('tagline'),self.t('menu'),self.t('close'),self.t('menu'),'Primary navigation' if self.lang=='en' else 'メインナビゲーション',nav,language)
        footer = '<footer class="site-footer"><div class="wrap"><div class="footer-top"><div><a class="footer-brand" href="{}">BIRL</a><p>{}</p><p>{}</p></div><div><p class="eyebrow">{}</p>{}{}{}</div></div><div class="footer-bottom"><span>© {} BIRL · {}</span><span>{}</span></div></div></footer>'.format(self.url('home'),self.t('footerText'),self.t('affiliation'),self.t('archiveLabel'),self.link('https://birlab.org/',self.t('archive')),self.link('https://birlab.org/resources/',self.t('resources')),self.link('https://www.youtube.com/channel/UCssbO6gQLdwC2T3ZNkAo1wA',self.t('youtube')),PUBLICATIONS['checked'][:4],self.t('copyright'),self.t('tagline'))
        title=(self.words['heroTitle'] if self.page=='home' else self.words['nav'][PAGES.index(self.page)])+' | BIRL'
        desc=self.words[{'home':'heroIntro','research':'researchIntro','people':'peopleIntro','publications':'publicationsIntro','join':'joinIntro'}[self.page]]
        return '<!doctype html>\n<html lang="{}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{}"><meta name="color-scheme" content="light"><meta name="theme-color" content="#173c34"><title>{}</title><link rel="icon" href="{}" type="image/svg+xml"><link rel="stylesheet" href="{}"><link rel="alternate" hreflang="en" href="{}"><link rel="alternate" hreflang="ja" href="{}"><script src="{}" defer></script></head><body class="page-{}">{}<main id="main">{}</main>{}</body></html>\n'.format(self.lang,esc(desc),esc(title),self.path('assets/favicon.svg'),self.path('style.css'),self.url(self.page,'en'),self.url(self.page,'ja'),self.path('site.js'),self.page,header,getattr(self,self.page)(),footer)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=ROOT/'dist')
    args=parser.parse_args()
    output=args.output.resolve()
    if output == ROOT or output in ROOT.parents:
        raise SystemExit('Choose a dedicated output folder, not the source directory')
    output.mkdir(parents=True,exist_ok=True)
    for lang in SITE:
        for name in PAGES:
            page=Page(lang,name)
            path=output/page.directory/'index.html'
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(page.render(),encoding='utf-8')
    shutil.copytree(ROOT/'assets',output/'assets',dirs_exist_ok=True)
    for name in ('style.css','site.js'):
        shutil.copy2(ROOT/'static'/name,output/name)
    (output/'.nojekyll').touch()
    print('Built 10 pages in',output)
