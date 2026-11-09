import os, re, sys, glob, posixpath
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
ROOT, OUT = sys.argv[1], sys.argv[2]
BS = chr(92)

class C(MarkdownConverter):
    def convert_img(self, el, text, **kw):
        return '![%s](%s)' % (el.get('aria-label') or el.get('alt') or '', el.get('src', ''))
    def convert_iframe(self, el, text, **kw):
        src = el.get('src') or el.get('data-src') or ''
        m = re.search(r'drive\.google\.com/file/d/([^/]+)/preview', src)
        if m: src = 'https://drive.google.com/file/d/%s/view' % m.group(1)
        m = re.search(r'youtube\.com/embed/([\w-]+)', src)
        if m: src = 'https://www.youtube.com/watch?v=' + m.group(1)
        lbl = re.sub(r'^Drive, ', '', (el.get('aria-label') or el.get('title') or 'Embedded content').strip())
        return '\n\n[%s](%s)\n\n' % (lbl, src) if src else ''

def convert(path):
    rel = os.path.relpath(path, ROOT).replace(BS, '/')
    s = BeautifulSoup(open(path, encoding='utf8').read(), 'html.parser')
    title = (s.title.string or '').replace('Setup & Cleanup Info - ', '').strip() or 'Home'
    for t in s.find_all(['script', 'style', 'svg', 'nav', 'header', 'footer', 'noscript']): t.decompose()
    for t in s.select('[aria-label="Copy heading link"],.j10yRb'): t.decompose()
    for t in s.find_all('img', src=re.compile(r'gstatic\.com/images/icons')): t.decompose()
    secs = [x for x in s.find_all('section') if not x.find_parent('section')]
    html = ''.join(str(x) for x in secs)
    sub = BeautifulSoup(html, 'html.parser')
    here = posixpath.dirname(rel)
    for a in sub.find_all('a', href=True):
        h = a['href']
        if not re.match(r'^(https?:|mailto:|#)', h) and h.endswith('.html'):
            a['href'] = h[:-5] + '.md'
        elif not re.match(r'^(https?:|mailto:|#)', h):
            pass
    root_prefix = posixpath.relpath('.', here or '.')
    for im in sub.find_all('img'):
        src = im.get('src', '')
        if src.startswith('http'): continue
        # html pages use paths relative to the page; md lives in markdown/<here>/ so add one level
        im['src'] = '../' + src
    md = C(heading_style='ATX', bullets='-').convert_soup(sub)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    md = re.sub(r'^#{1,2} ' + re.escape(title) + r'[ \t]*\n+', '', md, count=1)
    return rel, title, md

pages = []
for p in sorted(glob.glob(ROOT + '/**/*.html', recursive=True)):
    if os.path.basename(p) in ('login.html',) or '/.git/' in p.replace(BS, '/'): continue
    pages.append(convert(p))
for rel, title, md in pages:
    out = os.path.join(OUT, rel[:-5] + '.md')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    depth = rel.count('/')
    open(out, 'w', encoding='utf8', newline='\n').write('# %s\n\n%s\n' % (title, md))
    print(rel, len(md))
