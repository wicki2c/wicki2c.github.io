# Personal information pages

Static public information only. Publish **only `site/`** to GitHub Pages at
https://wicki2c.github.io/ after independent PR review. No dependencies or build.
Do not upload private application code, OAuth credentials or mail/calendar content.

Local preview: `python3 -m http.server 8765 --directory site`.

Hosting: configure Pages for GitHub Actions artifact publishing, not branch/Jekyll
publishing. Use only the existing Ops-assigned self-hosted pool; no GitHub-hosted
runners or paid fallback. Runner assignment and the minimal publishing workflow
are pending Ops confirmation. Do not treat proposed URLs as live until HTTP checks pass.

Search Console: Chad adds the URL-prefix property `https://wicki2c.github.io/`
and downloads its HTML verification file. Add the exact supplied filename/content
under `site/` through a reviewed PR; deploy and check its root URL returns 200
without login or redirect. Chad then clicks Verify. Keep the file permanently.
Never use the Domain property (it requires DNS control of github.io).

The privacy text describes the authorised personal-only workflow, not a runtime
audit. Before using it in Branding, Chief/Ops must confirm it matches the actual
assistant processing, retention and model-provider settings; amend discrepancies
rather than claiming that read-only OAuth alone guarantees privacy.
