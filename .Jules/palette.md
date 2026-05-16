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

## 2026-05-16 - [Visual Parity & Semantic Scaffolding]
**Learning:** Keyboard users often miss out on visual cues designed for mouse users (like hover-triggered gradients or translations). Synchronizing 'group-hover' effects with 'group-focus-visible' ensures visual parity. Additionally, small semantic changes like adding a '<main>' tag and correctly targeting skip links provide high-impact accessibility wins in static sites.
**Action:** Always pair 'group-hover' with 'group-focus-visible' for interactive containers and ensure a semantic '<main>' element exists for skip-link targets.
