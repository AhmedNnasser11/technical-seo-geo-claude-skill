# 🔍 Technical SEO & GEO — Claude Code Skill

> **An automated auditor skill for Claude Code** that performs comprehensive Technical SEO, Accessibility, Structured Data, and Generative Engine Optimization (GEO) audits on any website, page, or codebase.

Give Claude this skill and it will analyze your code or website against **60+ rules** sourced from official standards (Google, W3C, WCAG, Schema.org) and industry best practices, then produce a scored audit report with prioritized, actionable fixes.

---

## ⚡ Quick Start

1. **Add the skill** — Copy this folder into your Claude Code custom skills directory (e.g. `.claude/skills/`).
2. **Ask Claude to audit** — Open your project and ask:
   ```
   Audit this website for technical SEO, accessibility, and GEO readiness.
   ```
3. **Get a scored report** — Claude returns an executive summary with scores, issues grouped by severity, and a prioritized remediation plan.

---

## 🎯 What It Does

When given a website, page, or codebase, the skill instructs Claude to assess:

| # | Area | Description |
|---|------|-------------|
| 1 | **SEO Structure & Indexability** | Crawlable links, robots.txt, sitemaps, canonical tags |
| 2 | **Semantic HTML** | Document outline, landmarks, heading hierarchy |
| 3 | **Accessibility** | WCAG compliance, keyboard support, ARIA, form labels, alt text |
| 4 | **Metadata** | Titles, meta descriptions, robots directives |
| 5 | **Open Graph** | OG tags and social sharing metadata |
| 6 | **Structured Data** | JSON-LD, schema.org validation, product/breadcrumb/FAQ markup |
| 7 | **Internal Linking** | Anchor text, breadcrumbs, crawl depth, orphan pages |
| 8 | **Core Web Vitals** | LCP, INP, CLS, and performance risks |
| 9 | **E-commerce SEO** | Product/category pages, faceted navigation, inventory handling |
| 10 | **GEO (Generative Engine Optimization)** | AI extractability, entity clarity, content chunking |
| 11 | **AEO (Answer Engine Optimization)** | Answer-first structure, question-led headings |
| 12 | **LLM Visibility** | Passage extractability, trust signals, citation readiness |
| 13 | **AI Search Optimization** | AI Overviews positioning, brand entity presence |
| 14 | **Next.js SEO** | `generateMetadata`, `sitemap.ts`, `robots.ts`, rendering strategy |

---

## 📊 Output Format

The skill produces a structured audit report:

### Executive Summary
| Score | Description |
|-------|-------------|
| **Overall Score** | 0–100 composite |
| **SEO Score** | Indexability, metadata, linking |
| **Accessibility Score** | WCAG, keyboard, ARIA |
| **Performance Score** | Core Web Vitals |
| **GEO Score** | Generative Engine readiness |
| **AEO Score** | Answer Engine readiness |
| **LLM Visibility Score** | AI extractability & trust |

### Issue Reports
Every issue includes:
- **Category** — Which audit area it belongs to
- **Severity** — Critical / High / Medium / Low / Opportunity
- **Classification** — Official Standard, Industry Best Practice, Emerging GEO Practice, or Experimental
- **Why It Matters** — Impact explanation
- **Fix** — Concrete remediation steps
- **Example** — Code or content example

### Remediation Priority
1. 🔴 **Critical** — Blocks indexing, accessibility, or rendering
2. 🟠 **High** — Affects ranking, snippets, or AI visibility
3. 🟡 **Medium** — Structural and performance improvements
4. 🔵 **Low** — Polish and refinements
5. ⚪ **Opportunity** — Experimental GEO/AEO ideas

---

## 📁 Skill File Map

| File | Coverage |
|------|----------|
| [`SKILL.md`](SKILL.md) | Core skill definition, operating principles, and output format |
| [`semantic-html.md`](semantic-html.md) | Document structure, landmarks, headings, forms |
| [`accessibility.md`](accessibility.md) | Labels, keyboard, focus, ARIA, WCAG rules |
| [`metadata.md`](metadata.md) | Titles, meta descriptions, robots directives |
| [`open-graph.md`](open-graph.md) | OG tags and social metadata |
| [`schema.md`](schema.md) | Structured data rules and validation (JSON-LD, Product, Breadcrumb, FAQ) |
| [`sitemap.md`](sitemap.md) | Sitemap.xml strategy and coverage |
| [`robots.md`](robots.md) | robots.txt crawl control and indexability |
| [`canonical.md`](canonical.md) | Canonicalization and duplicate URL handling |
| [`internal-links.md`](internal-links.md) | Crawlable links, anchor text, breadcrumbs |
| [`core-web-vitals.md`](core-web-vitals.md) | LCP, INP, CLS, and performance logic |
| [`nextjs-seo.md`](nextjs-seo.md) | Next.js metadata, routing, sitemap/robots, rendering |
| [`ecommerce-seo.md`](ecommerce-seo.md) | Product/category pages, facets, inventory handling |
| [`geo.md`](geo.md) | Generative Engine Optimization practices |
| [`aeo.md`](aeo.md) | Answer Engine content patterns |
| [`llm-visibility.md`](llm-visibility.md) | Extractability, citation readiness, entity clarity |
| [`ai-search.md`](ai-search.md) | AI Overviews and AI search positioning |
| [`audit-checklist.md`](audit-checklist.md) | Step-by-step audit checklist |

---

## 🏛️ Source Authority Hierarchy

The skill follows a strict source hierarchy — it does **not** invent rules beyond its research base:

1. **Google / W3C / WHATWG / WCAG / Schema.org / Next.js** — Official standards
2. **MDN** — Trusted reference documentation
3. **Industry sources** (Lumar, Ahrefs, etc.) — Best practices
4. **GEO / AI research** — Emerging and experimental

Every finding is classified into one of:
- ✅ **Official Standard** — Backed by Google, W3C, WCAG, or Schema.org
- 📘 **Industry Best Practice** — Widely accepted by the SEO community
- 🧪 **Emerging GEO Practice** — Promising but not standardized
- 🔬 **Experimental** — Speculative, clearly labeled as such

---

## 💡 Example Usage

```
# Full audit
Audit my Next.js e-commerce site for SEO, accessibility, and GEO readiness.

# Targeted audit
Check the structured data and metadata on my product pages.

# GEO-focused
How GEO-ready is my content? Check entity clarity, content chunking, and LLM visibility.

# Accessibility check
Run an accessibility audit on my checkout flow.
```

---

## ⚠️ Important Notes

- **GEO/AEO practices are clearly labeled** — Emerging and experimental findings are never presented as guaranteed ranking factors.
- **Scoring starts at 100** and subtracts for confirmed issues. Opportunity items do not reduce score unless they also create a concrete SEO or accessibility problem.
- **The skill deduplicates** overlapping rules across files before flagging issues, so you won't see redundant findings.

---

## 📄 License

This skill is open-source and free to use. Feel free to fork, modify, and share.
# technical-seo-geo-claude-skill
