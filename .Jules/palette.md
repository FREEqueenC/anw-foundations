## 2026-05-10 - [Global Accessibility & Security Audit]
**Learning:** In static single-page landing pages, common UX oversights include missing skip-to-content links, lack of focus indicators for keyboard users, and missing security attributes on external links. Standardizing these across the app immediately elevates its professional feel and accessibility.
**Action:** Always check for 'target="_blank"' links without 'rel="noopener noreferrer"', verify 'focus-visible' states on all interactive elements, and ensure icon-only buttons have descriptive ARIA labels.
## 2026-05-12 - [Micro-interactions and Informational Focus]
**Learning:** For informational cards that lack direct links, adding 'tabindex="0"' allows keyboard users to 'discover' them via tabbing, triggering hover-state visual cues. Pairing this with 'aria-live' for action feedback (like copy-to-clipboard) ensures a rich, accessible experience.
**Action:** Use 'tabindex="0"' for key informational nodes and 'aria-live="polite"' for temporary UI feedback messages.

## 2026-04-15 - [Robust Micro-Interactions & Placeholder UX]
**Learning:** For "Coming Soon" features, using `href="javascript:void(0)"` with `cursor-default` prevents disruptive page jumps while allowing the use of `title` and `aria-label` to manage user expectations. Additionally, UI feedback scripts (like copy-to-clipboard) should extract data dynamically from the DOM and include timeout management to prevent state conflicts during rapid interactions.
**Action:** Implement placeholder links with `javascript:void(0)` and ensure micro-interaction scripts are robust against rapid clicks and maintainable via dynamic data extraction.

## 2026-05-15 - [Script Consolidation in Static Environments]
**Learning:** In a project with multiple micro-interactions (smooth scroll, clipboard utilities) but no build step, consolidating all JavaScript into a single, well-structured IIFE prevents global namespace pollution and allows for shared state management (like timeout IDs for UI feedback).
**Action:** For static sites, merge disparate script blocks into a cohesive utility script to improve maintainability and interaction consistency.

## 2026-05-17 - [Accessible & High-Performance Progress Indicators]
**Learning:** When implementing scroll progress bars, use `requestAnimationFrame` with a throttling flag and `{ passive: true }` scroll listeners to ensure 60FPS performance. Accessibility is crucial: always include `role="progressbar"` and keep `aria-valuenow` synchronized with the visual width.
**Action:** Prioritize performance and ARIA synchronization for all dynamic UI indicators to ensure a smooth, inclusive experience.

## 2026-05-24 - [Programmatic Focus Management for Single Page Apps]
**Learning:** In static single-page sites, standard anchor links often fail to move keyboard focus even when they scroll the viewport. Implementing a manual focus-management script—using temporary `tabindex="-1"` for non-interactive targets and explicitly focusing the "Skip Link" on "Back to Top" actions—ensures that the visual and logical positions of the user stay synchronized.
**Action:** Always pair smooth-scroll animations with programmatic `.focus()` calls to the target element (or skip link for top-of-page navigation) to maintain keyboard accessibility.
