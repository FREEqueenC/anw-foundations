## 2026-05-10 - [Global Accessibility & Security Audit]
**Learning:** In static single-page landing pages, common UX oversights include missing skip-to-content links, lack of focus indicators for keyboard users, and missing security attributes on external links. Standardizing these across the app immediately elevates its professional feel and accessibility.
**Action:** Always check for 'target="_blank"' links without 'rel="noopener noreferrer"', verify 'focus-visible' states on all interactive elements, and ensure icon-only buttons have descriptive ARIA labels.
## 2026-05-12 - [Micro-interactions and Informational Focus]
**Learning:** For informational cards that lack direct links, adding 'tabindex="0"' allows keyboard users to 'discover' them via tabbing, triggering hover-state visual cues. Pairing this with 'aria-live' for action feedback (like copy-to-clipboard) ensures a rich, accessible experience.
**Action:** Use 'tabindex="0"' for key informational nodes and 'aria-live="polite"' for temporary UI feedback messages.
