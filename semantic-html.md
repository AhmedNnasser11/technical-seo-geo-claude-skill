---

name: semantic-html-skill
description: Semantic HTML only — landmark structure, accessibility, SEO, and LLM readability.
----------------------------------------------------------------------------------------------

# Claude Code Skill: Semantic HTML

## Purpose

Use HTML elements for meaning, not for appearance. Semantic HTML makes structure explicit, improves accessibility, and helps search engines and AI systems identify main content and key sections. It helps indexing and machine readability, but it is not a direct ranking factor. 

## Core rules

Use native semantic elements first. Do not use `<div>` or `<span>` when a semantic element fits. Give headings to sections and articles, use only one `<main>`, avoid redundant ARIA on native semantic elements, and label repeated landmarks such as multiple `<nav>` or `<aside>` regions.  

## Semantic elements to use

### Structural landmarks

`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, and `<footer>` should define the page skeleton. `<main>` holds the unique page content, `<nav>` holds navigation links, `<article>` is a self-contained block, `<section>` groups a thematic part of the page, `<aside>` is tangential content, and `<footer>` is the footer for its nearest ancestor. 

### Content semantics

Use `<figure>` and `<figcaption>` for self-contained media with captions, `<time>` for machine-readable dates and times, `<mark>` for marked or highlighted text, `<address>` for author/contact info, and `<details>` / `<summary>` for disclosure widgets. These elements carry built-in meaning beyond generic containers. 

## Relationship between SEO and large language models

Semantic HTML helps SEO and LLM-based discovery because crawlers and AI systems use structure to find the main content, headings, dates, and other machine-readable signals. Search systems can separate navigation from main content more reliably when semantic landmarks are used, and elements like `<time>` and `<figure>` help content extraction. This is the practical bridge between semantic HTML, answer-engine optimization, and generative search visibility.  

## Do

* Use `<main>` once per page.
* Put a heading at the start of each `<section>` or `<article>`.
* Use `<nav>` for navigation blocks.
* Use `<article>` for standalone content.
* Use `<time datetime="...">` for dates.
* Use `<figure>` + `<figcaption>` for captions.
* Use `<details>` + `<summary>` for collapsible content.
* Add labels when there are multiple landmarks.  

## Avoid

* Do not use semantic tags only for styling.
* Do not add `role="main"` to `<main>` or other redundant ARIA roles.
* Do not use `<aside>` for central content.
* Do not nest `<main>` inside header, nav, footer, or article.
* Do not leave sections unlabeled when a heading is needed.  

## Example

```html
<header>
  <nav aria-label="Primary">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/articles">Articles</a></li>
    </ul>
  </nav>
</header>

<main id="main-content">
  <article>
    <h1>Semantic HTML and AI Search</h1>
    <p>...</p>

    <footer>
      <time datetime="2026-06-18">18 June 2026</time>
      <address>Ahmed Nasser</address>
    </footer>
  </article>

  <aside aria-label="Related links">
    <h2>Related</h2>
    <ul>
      <li><a href="/guide">Guide</a></li>
    </ul>
  </aside>
</main>
```

## Final checklist

* One `<main>` only
* Every `section` or `article` starts with a heading
* Use semantic tags before ARIA
* Label repeated landmarks
* Use machine-readable `<time>`
* Use `<figure>` / `<figcaption>` for captions
* Use `<details>` / `<summary>` for disclosure content
* Keep layout separate from meaning
