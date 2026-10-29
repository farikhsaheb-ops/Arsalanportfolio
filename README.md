# Arsalan Warish Portfolio — V3

A responsive, animated portfolio for **Python Programming, Web Designing and Professional Graphic Design**. Built with vanilla HTML, CSS, JavaScript, SVG, Canvas and the Web Animations-style requestAnimationFrame patterns. No framework or runtime library is required.

## Run locally
Open `index.html` in a modern browser, or run a simple static server from this folder, for example `python -m http.server 8000`, then visit `http://localhost:8000`.

## Edit key points and details
At the top of `js/script.js`, edit `SITE_CONFIG`:
- `KEY_POINTS` drives the hero trust row, the compact strip after the technology marquee and the About stat panels. The PDF build script reads the same three key points from this config automatically; `resume.html` is a print-ready static counterpart with matching values.
- `SKILL_LEVELS` is the editable source of skill ratings. The displayed skill cards have matching `data-skill` values in `index.html`; keep those values aligned when changing them.
- `EXPERIENCE` drives the About timeline. Replace placeholder roles, periods and descriptions with verified details only.
- `SOCIAL_LINKS` contains social URLs. Empty URLs intentionally fall back to the contact section instead of pretending a profile exists.
- `CONTACT` controls the email used by the email-copy and enquiry features. Update the WhatsApp URL in the HTML links too if the number changes.
- `TECH_ROTATION` changes the About technology ticker, and `RESUME_URL` is the portfolio URL placeholder.

## Demo code and outputs
- **Hero rose:** `rosePython` in `js/script.js` is valid Python using NumPy and Matplotlib. `ROSE` stores the matching JavaScript canvas parameters (`layers: 7`, `k: 5`, `points: 900`, `rotation: 0.11`, `a: 1.0`). The canvas applies the same polar rose formula and layer scaling as the code. Edit the shared parameters in both places together.
- **Service Python mini-demo:** `drawSpiral()` draws a distinct generative spiral, separate from the rose. The adjacent mini code is illustrative pseudocode, not executed Python.
- **Python Lab – Generative art:** the `LAB.art` Python example describes a radial flower using `r = 0.55 + 0.35*cos(8θ)`; its canvas result uses the same radial pattern.
- **Python Lab – Scraper:** `LAB.scrape` is a demonstration only. Its displayed output table is explicitly labelled simulated data and uses the same three product rows/prices as the visible code.
- **Python Lab – Analysis:** the sample data is `[12, 18, 15, 24, 29, 27]`; the chart displays those six values and the output describes the same series. Browser output is illustrative; it does not run Python in the browser.
- All concept websites and gallery designs are labelled **Concept project**. They do not imply real clients, testimonials or awards.

## Skills
Edit each skill's `data-skill` percentage in `index.html`, and keep `SITE_CONFIG.SKILL_LEVELS` in `js/script.js` aligned. The bars stay at zero until the section is substantially visible, then animate; they reset after the section leaves the viewport completely.

## Gallery designs
Six detailed CSS compositions are located in the gallery markup in `index.html`; the CSS art is under `.art-brand`, `.art-poster`, `.social-set`, `.stationery`, `.package-art` and `.phone-pair`. Replace each card's artwork `div` with an `<img>` later, using `object-fit:cover` and meaningful `alt` text. Gallery filters and lightbox are wired in `js/script.js`.

## Resume
- `resume.html` is the print-styled HTML version and the website preview modal loads it in an iframe.
- `resume.pdf` is a one-page A4, selectable-text PDF generated from ReportLab.
- Edit the single `RESUME_DATA` dictionary in `build_resume.py`, then run `python build_resume.py` to regenerate the PDF.
- Replace `portfolio_url` with the final live URL. The QR code encodes the current placeholder URL. Replace `portfolio_url` with your deployed URL and regenerate the PDF; replace `assets/images/portfolio-qr.png` with a QR generated from that same URL for the HTML resume.
- Education, certifications and specific experience entries are placeholders by design. Do not send the resume externally until you have filled in accurate facts and checked the “5+ Years Experience” and “1000+ Projects” claims.

## Profile photo
Place your real photo at `assets/images/profile.jpg`. The About hologram automatically uses it if the file exists; otherwise the AW emblem remains the fallback. The HTML resume does not require a photo.

## Contact form
The form validates required fields and opens the visitor's email app with a prefilled message. It does not claim to submit to a server. To use a backend form provider, wire the form submit handler in `js/script.js` to your chosen endpoint and configure spam protection.

## SEO and brand assets
`robots.txt`, `sitemap.xml`, `site.webmanifest`, `404.html`, `brand-guide.html`, canonical metadata and structured data are retained. Replace `https://example.com/` in `index.html`, `sitemap.xml`, `build_resume.py` and `resume.html` with the deployed portfolio URL. Logo SVGs and favicon assets are updated to the geometric AW emblem. Social preview image is `assets/images/og-image.png`.

## Motion, responsive and accessibility notes
- Vanilla JS/CSS/SVG/Canvas only; no external animation library.
- Scroll reveals and canvas effects use visibility checks; canvas animation is paused when off-screen.
- `prefers-reduced-motion` disables/shortens motion and shows final states.
- Layout breakpoints support small screens down to 320px. Check your own content and target browsers before publishing.
- All artwork in the gallery is original CSS composition and can be replaced later.

## Before publishing
1. Replace example.com with your real portfolio URL.
2. Add verified social links and experience entries.
3. Confirm the experience/project key-point claims and skill percentages.
4. Fill in education and certifications or remove those placeholders.
5. Add your portrait if desired and test all links on desktop and mobile.
6. Rebuild the PDF after editing `RESUME_DATA`.
