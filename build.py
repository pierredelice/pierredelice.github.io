#!/usr/bin/env python3
"""
Static-site generator for pierredelice.github.io.

Usage:
    python3 build.py            # process photo + regenerate index.html
    python3 build.py --no-photo # regenerate HTML only (skip photo processing)

Content lives in content.py. This script turns it into a fully static
index.html (all sections pre-rendered). assets/js/main.js only handles
behavior (theme toggle, mobile nav, scroll-spy) — no content.
"""
from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

import content as C

ROOT = Path(__file__).resolve().parent
IMG_DIR = ROOT / "assets" / "img"
PROFILE_OUT = IMG_DIR / "profile.jpg"
PROFILE_SIZE = 640  # output square size in px


# ----------------------------------------------------------------------
# Photo processing
# ----------------------------------------------------------------------
def process_photo() -> bool:
    """Auto-crop the white border, square-crop around the subject, and save."""
    src = Path(C.PROFILE["photo_source"]).expanduser()
    if not src.exists():
        print(f"  ! photo source not found: {src} — keeping existing avatar")
        return False

    try:
        from PIL import Image, ImageChops, ImageOps
    except ImportError:
        print("  ! Pillow not installed (pip install Pillow) — skipping photo")
        return False

    im = Image.open(src)
    im = ImageOps.exif_transpose(im).convert("RGB")

    # 1) Trim uniform (near-white) border by diffing against a white canvas.
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    # Amplify so faint off-white pixels still count, then get the bounding box.
    bbox = ImageChops.add(diff, diff, 2.0, -28).getbbox()
    if bbox:
        im = im.crop(bbox)

    # 2) Pad to a square (centered) so nothing important gets cut, then add a
    #    small breathing-room margin around the subject.
    w, h = im.size
    side = max(w, h)
    margin = int(side * 0.12)
    canvas = Image.new("RGB", (side + margin * 2, side + margin * 2), (255, 255, 255))
    canvas.paste(im, ((canvas.width - w) // 2, (canvas.height - h) // 2))

    # 3) Resize to the target and save.
    out = canvas.resize((PROFILE_SIZE, PROFILE_SIZE), Image.LANCZOS)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    out.save(PROFILE_OUT, "JPEG", quality=88, optimize=True)
    print(f"  ✓ photo → {PROFILE_OUT.relative_to(ROOT)} ({PROFILE_SIZE}px)")
    return True


# ----------------------------------------------------------------------
# HTML helpers
# ----------------------------------------------------------------------
def esc(s: str) -> str:
    return html.escape(s, quote=True)


# Icons keyed by name; only rendered when the profile field is set.
ICONS = {
    "email": '<path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm1.4 2L12 12.5 19.6 7H4.4zM20 8.3l-8 5.9-8-5.9V17h16V8.3z"/>',
    "linkedin": '<path d="M6.94 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0zM3 8.9h3.9V21H3V8.9zM9.4 8.9h3.7v1.65h.05c.52-.98 1.8-2.02 3.7-2.02 3.95 0 4.68 2.6 4.68 5.98V21h-3.9v-5.36c0-1.28-.02-2.92-1.78-2.92-1.78 0-2.05 1.39-2.05 2.83V21H9.4V8.9z"/>',
    "orcid": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM8.2 7.4a.95.95 0 1 1 0-1.9.95.95 0 0 1 0 1.9zM7.3 9h1.8v8.5H7.3V9zm3.5 0h3.4c3.24 0 4.66 2.32 4.66 4.25 0 2.1-1.64 4.25-4.64 4.25H10.8V9zm1.8 1.63v5.24h1.44c2.05 0 2.52-1.56 2.52-2.62 0-1.73-1.1-2.62-2.56-2.62H12.6z"/>',
    "scholar": '<path d="M12 3L1 9l11 6 9-4.9V16h2V9L12 3zM5 13.2V17c0 1.66 3.13 3 7 3s7-1.34 7-3v-3.8l-7 3.82-7-3.82z"/>',
    "github": '<path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.53 2.87 8.37 6.85 9.73.5.1.68-.22.68-.49l-.01-1.7c-2.79.62-3.38-1.38-3.38-1.38-.46-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.62.07-.62 1 .07 1.53 1.06 1.53 1.06.9 1.57 2.36 1.12 2.94.85.09-.66.35-1.12.63-1.38-2.23-.26-4.57-1.14-4.57-5.08 0-1.12.39-2.04 1.03-2.76-.1-.26-.45-1.3.1-2.72 0 0 .84-.28 2.75 1.05a9.4 9.4 0 0 1 5 0c1.91-1.33 2.75-1.05 2.75-1.05.55 1.42.2 2.46.1 2.72.64.72 1.03 1.64 1.03 2.76 0 3.95-2.34 4.82-4.57 5.07.36.32.68.94.68 1.9l-.01 2.82c0 .27.18.6.69.49A10.02 10.02 0 0 0 22 12.25C22 6.58 17.52 2 12 2z"/>',
}


def social_links() -> str:
    p = C.PROFILE
    entries = [
        ("email", f'mailto:{p["email"]}', "Email"),
        ("linkedin", p.get("linkedin"), "LinkedIn"),
        ("orcid", p.get("orcid") and f'https://orcid.org/{p["orcid"]}', "ORCID"),
        ("scholar", p.get("scholar"), "Google Scholar"),
        ("github", p.get("github"), "GitHub"),
    ]
    out = []
    for key, url, label in entries:
        if not url:
            continue
        ext = "" if key == "email" else ' target="_blank" rel="noopener"'
        out.append(
            f'<li><a href="{esc(url)}"{ext} title="{label}" aria-label="{label}">'
            f'<svg viewBox="0 0 24 24">{ICONS[key]}</svg></a></li>'
        )
    return "\n            ".join(out)


# ----------------------------------------------------------------------
# Section renderers
# ----------------------------------------------------------------------
def render_foundations() -> str:
    return "\n            ".join(f'<div class="fact">{f}</div>' for f in C.FOUNDATIONS)


def render_interests() -> str:
    return "\n            ".join(f"<li>{esc(i)}</li>" for i in C.RESEARCH_INTERESTS)


def render_education() -> str:
    rows = []
    for e in C.EDUCATION:
        rows.append(
            '<li><span><span class="edu__deg">{deg}</span><br>'
            '<span class="edu__inst">{inst}</span></span>'
            '<span class="edu__year">{year}</span></li>'.format(
                deg=esc(e["degree"]), inst=esc(e["institution"]), year=esc(e["year"])
            )
        )
    return "\n            ".join(rows)


def render_skills() -> str:
    cards = []
    for g in C.SKILL_GROUPS:
        items = "".join(f"<li>{esc(i)}</li>" for i in g["items"])
        cards.append(
            f'<div class="skill-card"><h3>{esc(g["label"])}</h3><ul>{items}</ul></div>'
        )
    return "\n        ".join(cards)


def render_timeline() -> str:
    items = []
    for x in C.EXPERIENCE:
        bullets = "".join(f"<li>{esc(b)}</li>" for b in x["bullets"])
        items.append(
            '<div class="tl-item">'
            f'<div class="tl-head"><span class="tl-role">{esc(x["role"])}</span>'
            f'<span class="tl-dates">{esc(x["dates"])}</span></div>'
            f'<div class="tl-org">{esc(x["org"])} '
            f'<span class="tl-loc">· {esc(x["loc"])}</span></div>'
            f"<ul>{bullets}</ul></div>"
        )
    return "\n        ".join(items)


def render_projects() -> str:
    cards = []
    for p in C.PROJECTS:
        tags = "".join(f"<span>{esc(t)}</span>" for t in p["tags"])
        cards.append(
            '<article class="card">'
            f'<h3>{esc(p["title"])}</h3><p>{esc(p["text"])}</p>'
            f'<div class="card__tags">{tags}</div></article>'
        )
    return "\n        ".join(cards)


def render_publications() -> str:
    items = []
    for p in C.PUBLICATIONS:
        cite = f'<span class="pub-title">{esc(p["cite"])}</span>'
        if p.get("doi"):
            doi = esc(p["doi"])
            cite += (
                f' <a href="https://doi.org/{doi}" target="_blank" '
                f'rel="noopener">DOI: {doi}</a>'
            )
        items.append(f"<li>{cite}</li>")
    return "\n        ".join(items)


def render_list(items) -> str:
    return "\n          ".join(f"<li>{esc(i) if '<' not in i else i}</li>" for i in items)


def render_about() -> str:
    parts = []
    for i, para in enumerate(C.ABOUT):
        cls = ' class="lede"' if i == 0 else ""
        parts.append(f"<p{cls}>{para}</p>")
    return "\n          ".join(parts)


# ----------------------------------------------------------------------
# Page template
# ----------------------------------------------------------------------
def build_html() -> str:
    p = C.PROFILE
    return TEMPLATE.format(
        name=esc(p["name"]),
        role=esc(p["role"]),
        affiliation=esc(p["affiliation"]),
        location=esc(p["location"]),
        location_short=esc(p["location_short"]),
        languages=esc(p["languages"]),
        cvu=esc(p["cvu"]),
        email=esc(p["email"]),
        linkedin=esc(p.get("linkedin") or ""),
        orcid=esc(p["orcid"]),
        cv_pdf=esc(p["cv_pdf"]),
        social=social_links(),
        about=render_about(),
        foundations=render_foundations(),
        interests=render_interests(),
        education=render_education(),
        skills=render_skills(),
        timeline=render_timeline(),
        projects=render_projects(),
        publications=render_publications(),
        honors=render_list(C.HONORS),
        training=render_list(C.TRAINING),
        contact_intro=esc(C.CONTACT_INTRO),
    )


TEMPLATE = """<!DOCTYPE html>
<!-- This file is GENERATED by build.py from content.py. Do not edit by hand. -->
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — AI Engineer &amp; NLP Researcher</title>
  <meta name="description" content="{name} — AI Engineer, NLP Researcher, and Data Scientist. Ph.D. in Language and Knowledge Engineering with 15+ years applying machine learning, statistical modeling, and evidence systems to public, health, education, and economic decisions." />
  <meta name="author" content="{name}" />
  <meta property="og:title" content="{name} — AI Engineer &amp; NLP Researcher" />
  <meta property="og:description" content="AI Engineer, NLP Researcher, and Data Scientist. LLM evaluation, conversational AI, Spanish-language NLP, and applied data science for the public sector." />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="assets/img/profile.jpg" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="assets/css/style.css" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%231F4E5F'/%3E%3Ctext x='50' y='68' font-size='52' font-family='Georgia,serif' fill='white' text-anchor='middle'%3EPD%3C/text%3E%3C/svg%3E" />
</head>
<body>
  <header class="nav" id="nav">
    <div class="nav__inner">
      <a href="#home" class="nav__brand">Pierre A. Delice</a>
      <button class="nav__toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav__links" id="navLinks">
        <a href="#about">About</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Research</a>
        <a href="#publications">Publications</a>
        <a href="#honors">Honors</a>
        <a href="#contact">Contact</a>
        <a href="{cv_pdf}" class="nav__cv" target="_blank" rel="noopener">CV</a>
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode" title="Toggle theme">
          <svg class="theme-toggle__sun" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M19.1 4.9l-1.8 1.8M6.7 17.3l-1.8 1.8"/></svg>
          <svg class="theme-toggle__moon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.6 6.6 0 0 0 9.8 9.8z"/></svg>
        </button>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero" id="home">
      <div class="hero__inner" id="about">
        <aside class="hero__card">
          <div class="avatar" aria-label="{name}">
            <img src="assets/img/profile.jpg" alt="{name}" />
          </div>
          <h1 class="hero__name">{name}</h1>
          <p class="hero__role">{role}</p>
          <p class="hero__affil">{affiliation}</p>

          <ul class="social">
            {social}
          </ul>

          <a href="{cv_pdf}" class="btn btn--block" target="_blank" rel="noopener">Download CV (PDF)</a>

          <ul class="hero__meta">
            <li><span>Location</span> {location_short}</li>
            <li><span>Languages</span> {languages}</li>
            <li><span>CVU</span> {cvu}</li>
          </ul>
        </aside>

        <div class="hero__body">
          <h2 class="section__title">About</h2>
          {about}

          <div class="foundations" id="foundations">
            {foundations}
          </div>

          <h3 class="subsection__title">Research Interests</h3>
          <ul class="pill-list">
            {interests}
          </ul>

          <h3 class="subsection__title">Education</h3>
          <ul class="edu" id="education">
            {education}
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--tint" id="skills">
      <div class="wrap">
        <h2 class="section__title section__title--center">Technical Skills</h2>
        <div class="skills-grid" id="skillsGrid">
        {skills}
        </div>
      </div>
    </section>

    <section class="section" id="experience">
      <div class="wrap">
        <h2 class="section__title section__title--center">Professional Experience</h2>
        <div class="timeline" id="timeline">
        {timeline}
        </div>
      </div>
    </section>

    <section class="section section--tint" id="projects">
      <div class="wrap">
        <h2 class="section__title section__title--center">Selected Research &amp; Projects</h2>
        <div class="cards" id="projectCards">
        {projects}
        </div>
      </div>
    </section>

    <section class="section" id="publications">
      <div class="wrap">
        <h2 class="section__title section__title--center">Selected Publications</h2>
        <ol class="pubs" id="pubsList">
        {publications}
        </ol>
      </div>
    </section>

    <section class="section section--tint" id="honors">
      <div class="wrap wrap--split">
        <div>
          <h2 class="section__title">Honors &amp; Service</h2>
          <ul class="checklist" id="honorsList">
          {honors}
          </ul>
        </div>
        <div>
          <h2 class="section__title">Training</h2>
          <ul class="checklist" id="trainingList">
          {training}
          </ul>
        </div>
      </div>
    </section>

    <section class="section" id="contact">
      <div class="wrap contact">
        <h2 class="section__title section__title--center">Contact</h2>
        <p class="contact__lede">{contact_intro}</p>
        <div class="contact__grid">
          <a class="contact__item" href="mailto:{email}">
            <span class="contact__label">Email</span>
            <span class="contact__value">{email}</span>
          </a>
          <a class="contact__item" href="{linkedin}" target="_blank" rel="noopener">
            <span class="contact__label">LinkedIn</span>
            <span class="contact__value">linkedin.com/in/padelice</span>
          </a>
          <a class="contact__item" href="https://orcid.org/{orcid}" target="_blank" rel="noopener">
            <span class="contact__label">ORCID</span>
            <span class="contact__value">{orcid}</span>
          </a>
          <div class="contact__item">
            <span class="contact__label">Location</span>
            <span class="contact__value">{location}</span>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="wrap">
      <p>&copy; <span id="year"></span> {name} · Built with Python · Hosted on GitHub Pages</p>
    </div>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Build pierredelice.github.io")
    ap.add_argument("--no-photo", action="store_true", help="skip photo processing")
    args = ap.parse_args()

    print("Building site…")
    if not args.no_photo:
        process_photo()

    (ROOT / "index.html").write_text(build_html(), encoding="utf-8")
    print("  ✓ index.html generated")
    print("Done. Preview:  python3 -m http.server 8000")
    return 0


if __name__ == "__main__":
    sys.exit(main())
