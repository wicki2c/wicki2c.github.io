"""Dependency-free checks for the public static pages."""
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1] / 'site'

class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag not in ('script', 'form', 'iframe'), tag
        if tag == 'title':
            self.title = True
        if tag in ('a', 'link'):
            self.links.append(attrs.get('href', ''))

for page in ROOT.rglob('*.html'):
    check = Check()
    check.feed(page.read_text())
    assert check.title, page
    for url in check.links:
        if url.startswith('/'):
            target = ROOT / url.lstrip('/')
            if url.endswith('/'):
                target /= 'index.html'
            assert target.exists(), (page, url)
    print('PASS', page.relative_to(ROOT), 'title, static markup, local links')
privacy = (ROOT / 'jarvis/privacy/index.html').read_text()
assert 'gmail.readonly' in privacy and 'calendar.readonly' in privacy
print('PASS read-only scope disclosures')
