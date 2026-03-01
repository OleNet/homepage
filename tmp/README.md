# jiaxiang.github.io

A personal static site. No framework. No build step. No CMS.

## Structure

```
/
├── index.html              # About
├── style.css               # All styles
└── content/
    ├── books/
    │   ├── index.html
    │   └── *.html          # Individual book notes
    ├── photography/
    │   ├── index.html
    │   └── *.jpg           # Images placed directly
    └── thinking/
        ├── index.html
        └── *.html          # Individual pieces
```

## Writing workflow

1. Write content in Markdown (optional, for personal record)
2. Create a new `.html` file in the relevant folder using the existing pages as templates
3. Add an entry to the section's `index.html`
4. Commit and push

Markdown front-matter convention (for personal reference):
```yaml
---
title: Title Here
date: 2026-03-01
---
```

## Fonts

Loaded from Google Fonts:
- **EB Garamond** — body, titles (serif, academic)
- **DM Sans** — navigation, dates, labels (sans, structural)

## Hosting

GitHub Pages. No custom domain required, but trivial to add via `CNAME`.

## Philosophy

> A disciplined white space for long-term thinking and visual clarity.
