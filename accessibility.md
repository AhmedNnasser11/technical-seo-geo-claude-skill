# Accessibility

## Scope

This file covers WCAG-backed and MDN-backed accessibility rules in the report.

## Rules

### 1) Provide an accessible name for every form control
- **Rule name:** Form labels
- **Description:** Use `<label>` elements or equivalent accessible naming so every form control has a clear label.
- **Source URL:** https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Keyboard
- **Source organization:** MDN / Mozilla
- **Source type:** Official accessibility documentation
- **Classification:** Official Standard
- **Severity:** Critical
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Unlabeled form controls are difficult or impossible for assistive technologies to use.
- **Expected impact:** Improved form completion and WCAG alignment.
- **Implementation guidance:** Pair inputs with `<label for>` or wrap the input in the label.
- **Example:** `<label for="email">Email</label><input id="email" type="email">`
- **Exceptions:** None for meaningful form controls.
- **Potential drawbacks:** Minimal.
- **Conflicting opinions:** None in the report.
- **Notes:** The report treats labeled forms as an official standard.

### 2) Make all interactive content keyboard operable
- **Rule name:** Keyboard operability
- **Description:** All clickable or interactive UI must be focusable and usable with a keyboard.
- **Source URL:** https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Keyboard
- **Source organization:** MDN / Mozilla
- **Source type:** Official accessibility documentation
- **Classification:** Official Standard
- **Severity:** Critical
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Keyboard access is required for accessibility and is part of the report’s WCAG-backed guidance.
- **Expected impact:** Better accessibility and fewer blocked interactions.
- **Implementation guidance:** Ensure buttons, links, menus, dialogs, and custom controls can be reached and activated via keyboard.
- **Example:** A custom menu trigger behaves like a real button and responds to Enter and Space.
- **Exceptions:** None for interactive controls.
- **Potential drawbacks:** Custom UI often needs extra engineering.
- **Conflicting opinions:** None in the report.
- **Notes:** The report explicitly warns against non-focusable clickable elements.

### 3) Avoid positive tabindex values
- **Rule name:** Focus order control
- **Description:** Do not use `tabindex` values greater than zero to reorder focus.
- **Source URL:** https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Keyboard
- **Source organization:** MDN / Mozilla
- **Source type:** Official accessibility documentation
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Artificial focus order confuses keyboard users and assistive technology.
- **Expected impact:** More predictable keyboard navigation.
- **Implementation guidance:** Let the DOM order drive focus flow.
- **Example:** Avoid `tabindex="5"` on elements.
- **Exceptions:** The report does not specify any exceptions.
- **Potential drawbacks:** Can require refactoring existing UI.
- **Conflicting opinions:** None in the report.
- **Notes:** Use visible focus styles as part of keyboard usability.

### 4) Use ARIA only when native semantics are not available
- **Rule name:** Native-first ARIA
- **Description:** Prefer native HTML semantics before adding ARIA roles.
- **Source URL:** https://developer.mozilla.org/en-US/blog/aria-accessibility-html-landmark-roles/
- **Source organization:** MDN / Mozilla
- **Source type:** Official accessibility documentation
- **Classification:** Official Standard
- **Severity:** Medium
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Native elements already expose built-in roles and reduce accessibility mistakes.
- **Expected impact:** Cleaner accessibility tree and lower implementation risk.
- **Implementation guidance:** Use ARIA only when a native element cannot express the necessary meaning or behavior.
- **Example:** Prefer `<nav>` over a generic element with `role="navigation"`.
- **Exceptions:** When no semantic element fits the interaction.
- **Potential drawbacks:** Overuse of ARIA can create conflicts.
- **Conflicting opinions:** None in the report.
- **Notes:** The report explicitly references the “first rule of ARIA.”

### 5) Provide alternative text for non-text content
- **Rule name:** Alt text
- **Description:** Provide text alternatives for images and other non-text content, using empty alt text for decorative images.
- **Source URL:** https://www.w3.org/WAI/standards-guidelines/wcag/
- **Source organization:** W3C / WCAG
- **Source type:** Official accessibility standard
- **Classification:** Official Standard
- **Severity:** High
- **Confidence level:** High
- **Evidence strength:** Strong
- **Why it matters:** Users who cannot see the content still need equivalent information.
- **Expected impact:** Better accessibility and content comprehension.
- **Implementation guidance:** Write descriptive alt text only when the image conveys information.
- **Example:** `alt="Black running shoe with white sole"`
- **Exceptions:** Decorative images use empty `alt=""`.
- **Potential drawbacks:** Poorly written alt text can be redundant or noisy.
- **Conflicting opinions:** None in the report.
- **Notes:** The report also connects descriptive alt text to multimodal AI-readiness.
