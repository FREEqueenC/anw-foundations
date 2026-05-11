## 2026-05-10 - [Global Accessibility & Security Audit]
**Learning:** In static single-page landing pages, common UX oversights include missing skip-to-content links, lack of focus indicators for keyboard users, and missing security attributes on external links. Standardizing these across the app immediately elevates its professional feel and accessibility.
**Action:** Always check for 'target="_blank"' links without 'rel="noopener noreferrer"', verify 'focus-visible' states on all interactive elements, and ensure icon-only buttons have descriptive ARIA labels.

## 2026-04-15 - [Robust Micro-Interactions & Placeholder UX]
**Learning:** For "Coming Soon" features, using `href="javascript:void(0)"` with `cursor-default` prevents disruptive page jumps while allowing the use of `title` and `aria-label` to manage user expectations. Additionally, UI feedback scripts (like copy-to-clipboard) should extract data dynamically from the DOM and include timeout management to prevent state conflicts during rapid interactions.
**Action:** Implement placeholder links with `javascript:void(0)` and ensure micro-interaction scripts are robust against rapid clicks and maintainable via dynamic data extraction.
