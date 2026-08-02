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

## 2026-05-20 - [Accessible Smooth Scrolling & Focus Management]
**Learning:** In single-page applications using smooth scroll, visual movement must be paired with programmatic focus management. Without explicitly moving focus (using `element.focus()` and `tabindex="-1"`), keyboard and screen reader users remain at the source of the click, losing context and breaking the logical navigation flow.
**Action:** Always synchronize smooth scroll animations with programmatic focus updates to the target element to maintain accessibility parity with visual transitions.

## 2026-06-14 - [Synchronized Visibility and Interactivity for Secondary Actions]
**Learning:** When using Tailwind's `group-hover` to show secondary interactive elements (like copy buttons), relying solely on `opacity` leaves them reachable via keyboard while invisible ("ghost focus"). Using a combination of `invisible`, `pointer-events-none`, and `group-focus-within` ensures these elements are only focusable and interactive when they are visually presented to the user.
**Action:** Always pair visibility transitions with `invisible` and `pointer-events-none`, and ensure they are toggled via `group-focus-within` to maintain keyboard accessibility and prevent a confusing tab order.

## 2026-06-20 - [Accessible Custom Tooltips vs Native Title]
**Learning:** Native `title` attributes are inaccessible via keyboard focus, leaving screen reader and keyboard-only users without important contextual information for icon-only buttons. Replacing them with custom tooltips triggered by `focus-visible` (and hover) ensures critical context is available to all users. When using `aria-label` alongside `aria-describedby` (e.g., for custom tooltips), ensure the tooltip text differs from the label (or provides additional context) to prevent screen readers from redundantly announcing identical strings.
**Action:** Always avoid native `title` attributes on interactive elements. Instead, build custom Tailwind tooltips (using `group-focus-visible:opacity-100` and `group-hover:opacity-100`) linked via `aria-describedby`.

## 2026-07-26 - [Secondary Page Keyboard Accessibility Parity]
**Learning:** Secondary pages often suffer from degraded keyboard accessibility compared to heavily optimized landing pages. Elements like navigation links and project cards frequently miss `focus-visible` styles, leading to a disconnected keyboard navigation experience.
**Action:** Always verify keyboard focus parity across all pages and ensure consistent `focus-visible:ring-*` classes on all interactive elements.

## 2026-07-30 - [Subresource Integrity (SRI) for Third-Party CDNs]
**Learning:** Loading external scripts or stylesheets (like Tailwind CSS or Font Awesome) via CDNs without Subresource Integrity (SRI) attributes creates a significant security vulnerability. If the CDN is compromised, malicious code could be injected and executed on all client browsers. Hardcoding a specific version alongside an SRI hash mitigates this risk by ensuring the browser only executes the script if its content perfectly matches the expected cryptographic hash.
**Action:** Always include `integrity` and `crossorigin="anonymous"` attributes for scripts and stylesheets loaded from third-party CDNs, pinning to a specific version to prevent hash mismatches during minor updates.

## 2026-08-01 - [De-obfuscation and Micro-Interactions]
**Learning:** When implementing micro-interactions that rely on dynamically populated elements (e.g., email de-obfuscation for copy-to-clipboard), ensure the de-obfuscation logic executes on DOM load prior to binding the interaction event listeners to avoid capturing empty or placeholder states.
**Action:** Always verify that dynamic data dependencies are fulfilled before attaching event listeners in utility scripts.
