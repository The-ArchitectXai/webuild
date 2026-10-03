# Webuild site template

Add a project:
1. Put photos (JPG, ~1000px wide) in `content/images/`.
2. In `content/content.json`, copy a block in `projects` and edit:
   {"name": "...", "cat": "home|com|inst", "label": "interiors", "note": "...", "photos": ["file1.jpg", "file2.jpg"]}
   The first photo is the cover; more photos open as a gallery. Leave `photos` empty for a placeholder card.
3. Run `python3 build.py` -> regenerates `../webuild-homepage-v2.html`.

New filter tab: add `["key","Label"]` to `categories`, then use that key as `cat`.
Cover photos for the "What we do" cards and commercial categories are the `services` and `commercial_categories` lists (same order as on the page).
