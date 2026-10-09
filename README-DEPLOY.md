# Webuild: going live

Main address: https://www.webuild.org.in (with www). GA4 Measurement ID: G-YB61EN7J5C (already built in).
Rebuild any time:  python3 build.py --deploy --ga G-YB61EN7J5C --domain https://www.webuild.org.in
Output: `dist/` and `../webuild-site-deploy.zip`.

## 1. Put the site online (pick ONE host)

### A. GitHub Pages (what we are using)
1. Create a repository and push the CONTENTS of `dist/` to its main branch (index.html at the top level).
   `CNAME` (www.webuild.org.in) and `.nojekyll` are already in the package.
2. Repository Settings > Pages > Deploy from a branch > main / (root). Custom domain: www.webuild.org.in. Tick "Enforce HTTPS" once it is available.
3. At your domain registrar's DNS:
   - CNAME record: host `www`, value `<your-github-username>.github.io`
   - Apex (webuild.org.in) A records to GitHub Pages: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (check GitHub's current list in their Pages docs).
   GitHub then redirects webuild.org.in to www.webuild.org.in and http to https by itself.
4. `.htaccess` is ignored by GitHub Pages. That is fine, GitHub does the redirects.

### B. Apache / cPanel hosting
Upload the zip contents to `public_html` and turn on the free SSL. The included `.htaccess` sends http and non-www to https://www.webuild.org.in with a 301.
Nginx: return 301 https://www.webuild.org.in$request_uri; for http and for webuild.org.in.

## 2. Check the redirects (each must end at https://www.webuild.org.in/ and return 200)
  curl -sIL http://webuild.org.in | grep -iE "HTTP|location"
  curl -sIL http://www.webuild.org.in | grep -iE "HTTP|location"
  curl -sIL https://webuild.org.in | grep -iE "HTTP|location"
  curl -sIL https://www.webuild.org.in/hi/ | grep -iE "HTTP|location"

## 3. Google Search Console
1. Add a Domain property: webuild.org.in (covers www and non-www). Verify with the DNS TXT record Google gives you.
2. Sitemaps > add `sitemap.xml` > Submit (https://www.webuild.org.in/sitemap.xml).
3. URL Inspection: https://www.webuild.org.in/ and https://www.webuild.org.in/hi/ > Request indexing.

## 4. Speed (PageSpeed Insights)
Run https://pagespeed.web.dev for https://www.webuild.org.in/ and /hi/ on Mobile, then fill in:
| Date | URL | Performance | LCP | INP | CLS |
|------|-----|-------------|-----|-----|-----|
|      |     |             |     |     |     |
Google "good" targets: LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less. INP and field data only appear once the page has real visitors.
Local lab test (not PageSpeed): single-file build 3,989 KB and about 20 s to load; deploy build 559 KB and about 3 s; CLS 0.000 on both (emulated slow 4G, 4x CPU slowdown).

## 5. GA4
The Measurement ID G-YB61EN7J5C is already in the pages. Events sent: `phone_click`, `whatsapp_click`, `form_submit`, `generate_lead`.
To mark the key event: analytics.google.com > Admin > Data display > Events > find `generate_lead` > switch on "Mark as key event".
(If `generate_lead` is not listed yet, tap the form once on the live site, wait a few hours, then refresh the list. In some accounts the menu is Admin > Events.)
Check with Reports > Realtime or Admin > DebugView.

## 6. Notes
- Payment schedule in the FAQ and in the planner now match: 1% token, 15% foundation, per floor 20% slab and 10% brickwork (shown equally split across floors), 10% electrical, 10% plumbing, 10% interiors, balance on completion with 2% held 45 days.
- One H1 per page. Title and description are your English text; the Hindi ones are a translation to be reviewed.
