# Personal information pages

Static public information only. Publish only `docs/` to GitHub Pages at
https://wicki2c.github.io/ after independent PR review. No dependencies or build.
Do not upload private application code, OAuth credentials or mail/calendar content.

Local preview: `python3 -m http.server 8765 --directory docs`.

Hosting: GitHub Pages → Deploy from a branch → `main` → `/docs`.
`.nojekyll` disables Jekyll processing. No build, Actions workflow or runner setup.
Ops approved this public-repo publishing route. After independent review and merge,
enable Pages using:

```sh
gh api -X POST repos/wicki2c/wicki2c.github.io/pages -f 'source[branch]=main' -f 'source[path]=/docs'
```

Everything committed here is public; never add private files. Do not treat proposed
URLs as live until public HTTPS checks pass.

Search Console: Chad adds the URL-prefix property `https://wicki2c.github.io/`
and downloads its HTML verification file. Add the exact supplied filename/content
under `docs/` through a reviewed PR; deploy and check its root URL returns 200
without login or redirect. Chad then clicks Verify. Keep the file permanently.
Never use the Domain property (it requires DNS control of github.io).
