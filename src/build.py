#!/usr/bin/env python3
"""Static site generator for a-penna.github.io.

Usage:  python3 -m pip install markdown   (once)
        python3 src/build.py

Reads src/content.py, src/legal/**.md, src/icons/*.png, src/site.{css,js}
and writes the public site to the repository root.
"""
import base64, hashlib, html, json, os, re, shutil, subprocess, sys
from pathlib import Path

import markdown

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
sys.path.insert(0, str(SRC))
from content import APPS, APPLE_EULA, DOC_LANGS, EMAIL, GITHUB, LANG_NAMES, SITE_URL, T  # noqa: E402

UI_LANGS = ["en", "it"]
LAZY = ' loading="lazy"'
ON = ' class="on"'


# ---------------------------------------------------------------- helpers
def prefix(lang):
    return "/" if lang == "en" else f"/{lang}/"


def home_url(lang):
    return prefix(lang)


def app_url(app, lang):
    return f"{prefix(lang)}apps/{app['slug']}/"


def esc(s):
    return html.escape(s, quote=True)


def write(path, text):
    p = OUT / path.lstrip("/")
    if path.endswith("/"):
        p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s*\n\s*", "", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    return css.replace(";}", "}")


def build_assets():
    """Copy CSS/JS with a content hash for cache busting; convert icons to WebP."""
    css = minify_css((SRC / "fonts.css").read_text() + "\n" + (SRC / "site.css").read_text())
    js = (SRC / "site.js").read_text()
    (OUT / "assets").mkdir(exist_ok=True)
    (OUT / "assets/site.css").write_text(css)
    (OUT / "assets/site.js").write_text(js)
    icons = OUT / "assets/icons"
    icons.mkdir(parents=True, exist_ok=True)
    for app in APPS:
        src = SRC / "icons" / f"{app['slug']}.png"
        for size in (512, 144):
            dst = icons / f"{app['slug']}-{size}.webp"
            if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
                subprocess.run(["cwebp", "-quiet", "-q", "86", "-resize", str(size), str(size), str(src), "-o", str(dst)], check=True)
    v = lambda s: hashlib.sha1(s.encode()).hexdigest()[:8]
    return {"css": f"/assets/site.css?v={v(css)}", "js": f"/assets/site.js?v={v(js)}"}


def icon(app, size=512):
    return f"/assets/icons/{app['slug']}-{size}.webp"


def legal_docs(app):
    """{('privacy','en'): html, ...} rendered from src/legal/<slug>/<type>-<lang>.md"""
    out = {}
    for f in sorted((SRC / "legal" / app["slug"]).glob("*.md")):
        kind, lang = f.stem.rsplit("-", 1)
        text = f.read_text(encoding="utf-8")
        text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)  # Jekyll front matter
        body = markdown.markdown(text, extensions=["tables", "sane_lists"])
        body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
        out[(kind, lang)] = body
    return out


def split_words(h, start=.15, step=.07):
    """Wrap each word of the headline in .w spans with staggered delays (no JS needed)."""
    parts, i = re.split(r"(<span[^>]*>.*?</span>|<br>)", h), 0
    res = []
    for part in parts:
        if not part:
            continue
        if part == "<br>":
            res.append(part)
        elif part.startswith("<span"):
            res.append(part.replace("<span ", f'<span style="animation-delay:{start + i * step:.2f}s" ', 1).replace('class="', 'class="w ', 1))
            i += 1
        else:
            for tok in re.split(r"(\s+)", part):
                if tok.strip():
                    res.append(f'<span class="w" style="animation-delay:{start + i * step:.2f}s">{tok}</span>')
                    i += 1
                elif tok:
                    res.append(" ")
    return "".join(res)


# ---------------------------------------------------------------- layout
# The only inline script: its hash is whitelisted in the CSP below.
NOJS = "document.documentElement.classList.remove('no-js')"
# GitHub Pages can't send custom headers, so the policy ships as a <meta>.
# Everything is self-hosted: no third-party origins are allowed.
# style-src keeps 'unsafe-inline' for the per-element style="--c:…" attributes.
CSP = ("default-src 'none'; script-src 'self' 'sha256-" + base64.b64encode(hashlib.sha256(NOJS.encode()).digest()).decode() + "'; "
       "style-src 'self' 'unsafe-inline'; img-src 'self'; font-src 'self'; manifest-src 'self'; base-uri 'none'; form-action 'none'")

FAVICON = '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">'


def head(lang, title, desc, path, alt_paths, assets, og_image=None, extra=""):
    t = T[lang]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}{p}">' for l, p in alt_paths.items())
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}{alt_paths["en"]}">'
    og = f'<meta property="og:image" content="{SITE_URL}{og_image}">' if og_image else ""
    return f"""<!doctype html>
<html lang="{t['html_lang']}" class="no-js">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#04050a">
<link rel="canonical" href="{SITE_URL}{path}">{alts}
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{SITE_URL}{path}">{og}
{FAVICON}
<link rel="preload" href="/assets/fonts/Geist-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{assets['css']}">
<script>{NOJS}</script>
<script src="{assets['js']}" defer></script>{extra}
</head>
<body>
<div class="bg" aria-hidden="true"></div><div class="spot" aria-hidden="true"></div>
"""


def nav(lang, other_url, items):
    other = "IT" if lang == "en" else "EN"
    links = "".join(f'<a href="{h}">{esc(l)}</a>' for l, h in items)
    return f'<nav aria-label="Main"><div class="links">{links}<a href="{other_url}" class="mono" hreflang="{other.lower()}" lang="{other.lower()}">{other}</a></div></nav>\n'


def footer(lang):
    t = T[lang]
    return f"""<footer><span>© 2026 Alessandro Penna</span><span><a href="mailto:{EMAIL}">Email</a> · <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a> · <span class="mono">{t['footer_right']}</span></span></footer>
</main>
</body>
</html>
"""


# ---------------------------------------------------------------- home
def home(lang, assets):
    t, n = T[lang], len(APPS)
    term = json.dumps({
        "whoami": t["whoami"], "launching": t["launching"].format(n=n),
        "apps": [{"name": a["name"], "href": app_url(a, lang), "c": a["c2"]} for a in APPS],
    }, ensure_ascii=False)
    dock = "".join(
        f'<a href="{app_url(a, lang)}" style="transition-delay:{i * .08:.2f}s" aria-label="{esc(a["name"])}"><img src="{icon(a, 144)}" width="62" height="62" alt="" decoding="async"></a>'
        for i, a in enumerate(APPS))
    noscript_ls = " ".join(f'<a href="{app_url(a, lang)}" style="color:{a["c2"]}">{esc(a["name"])}</a>' for a in APPS)

    stage = "".join(
        f'<div class="sic{" on" if i == 0 else ""}"><div class="tilt">'
        f'<img src="{icon(a)}" width="512" height="512" alt="{esc(a["name"])}" decoding="async"{LAZY if i else ""}>'
        f'<div class="gloss"></div><div class="refl" aria-hidden="true"><img src="{icon(a)}" alt="" loading="lazy" decoding="async"></div></div></div>'
        for i, a in enumerate(APPS))
    rail = "".join(
        f'<a href="{app_url(a, lang)}"{"" if i else ON} aria-label="{esc(a["name"])}"><img src="{icon(a, 144)}" width="28" height="28" alt="" loading="lazy"></a>'
        for i, a in enumerate(APPS))
    chaps = "".join(f"""
   <article class="chap{' on' if i == 0 else ''}" style="--c:{a['c2']}">
    <span class="idx mono">{i + 1:02d} / {n:02d}</span><span class="cat mono">{esc(a['cat'][lang])}</span>
    <h3><a href="{app_url(a, lang)}">{esc(a['name'])}</a></h3>
    <p>{esc(a['desc'][lang])}</p>
    <div class="chip"><span>{t['iphone']}</span><span>{' · '.join(a['app_langs']) if len(a['app_langs']) > 1 else LANG_NAMES[a['app_langs'][0]]}</span><span>{a['year']}</span></div>
    <div class="acts"><a class="pri" href="{app_url(a, lang)}#privacy">{t['privacy']}</a><a href="{app_url(a, lang)}#terms">{t['terms']}</a><a href="{app_url(a, lang)}#support">{t['support']}</a><a href="{a['appstore']}" target="_blank" rel="noopener">{t['appstore']} ↗</a></div>
   </article>""" for i, a in enumerate(APPS))
    facts = "".join(f'<div class="fact"><span class="n mono">{i + 1:02d}</span><div><h3>{esc(h)}</h3><p>{esc(p)}</p></div></div>' for i, (h, p) in enumerate(t["facts"]))
    other = "it" if lang == "en" else "en"
    return (head(lang, t["title"], t["meta_desc"], home_url(lang), {l: home_url(l) for l in UI_LANGS}, assets)
            + nav(lang, home_url(other), [(t["nav_apps"], "#apps"), (t["nav_about"], "#about"), (t["nav_contact"], "#contact")])
            + f"""<main>
<section class="hero">
 <div>
  <h1>{split_words(t['h1'])}</h1>
  <p class="lead in" style="animation-delay:.75s">{t['lead']}</p>
  <div class="cta in" style="animation-delay:.9s"><a class="btn p" href="#apps">{t['cta_apps']} <span aria-hidden="true">↓</span></a><a class="btn s" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a></div>
 </div>
 <div class="vis in" style="animation-delay:.4s">
  <div class="win" role="img" aria-label="Terminal: whoami, ls ~/apps"><div class="bar" aria-hidden="true"><i></i><i></i><i></i><span class="mono">alessandro — zsh</span></div>
   <div class="tb" id="tb"><span class="p">alessandro@mac</span> <span class="d">~ %</span> <span class="cur"></span><noscript><br>{noscript_ls}</noscript></div></div>
  <div class="dock" id="dock">{dock}</div>
  <script type="application/json" id="term-data">{term}</script>
 </div>
 <div class="scroll mono" aria-hidden="true">{t['scroll']}</div>
</section>

<section id="apps">
 <div class="eyebrow mono rv">{t['pf_eyebrow'].format(n=f'{n:02d}')}</div>
 <h2 class="rv">{t['pf_title']}</h2>
 <div class="pf" id="pf">
  <div class="stage" aria-hidden="true"><div class="show"><span class="snum">01</span>{stage}</div><div class="rail">{rail}</div></div>
  <div>{chaps}
  </div>
 </div>
</section>

<section class="blk about" id="about">
 <div>
  <div class="eyebrow mono rv">{t['about_eyebrow']}</div>
  <div class="stack rv mono"><span>Swift</span><span>SwiftUI</span><span>SwiftData</span><span>StoreKit 2</span><span>SpriteKit</span><span>MapKit</span><span>Vision</span><span>Game Center</span></div>
 </div>
 <div class="facts rv">{facts}</div>
</section>

<section class="contact rv" id="contact">
 <div class="eyebrow mono">{t['contact_eyebrow']}</div>
 <h2>{t['contact_title']}</h2>
 <p>{t['contact_text']}</p>
 <a class="btn p" href="mailto:{EMAIL}">{t['contact_btn']} →</a>
</section>
""" + footer(lang))


# ---------------------------------------------------------------- app page
def app_page(app, lang, assets):
    t = T[lang]
    docs = legal_docs(app)
    priv_langs = [l for l in DOC_LANGS if ("privacy", l) in docs]
    default = lang if lang in priv_langs else priv_langs[0]
    panes = []
    for (kind, l), body in docs.items():
        note = f'<p class="note">{t["only_it"]}</p>' if app["app_langs"] == ["it"] and lang != "it" else ""
        hidden = "" if (kind == "privacy" and l == default) else " hidden"
        panes.append(f'<article class="doc md" data-doc="{kind}-{l}" lang="{l}"{hidden}>{note}{body}</article>')
    if not any(k == "terms" for k, _ in docs):
        panes.append(f'<article class="doc" data-doc="terms" hidden><div class="eula"><p>{esc(t["eula_text"].format(name=app["name"]))}</p>'
                     f'<a class="btn s" href="{APPLE_EULA}" target="_blank" rel="noopener">{t["eula_link"]} ↗</a></div></article>')
    lang_btns = "".join(f'<button type="button" data-l="{l}" aria-selected="{str(l == default).lower()}" title="{LANG_NAMES[l]}">{l}</button>' for l in DOC_LANGS if l in priv_langs or ("terms", l) in docs)
    others = "".join(f'<a href="{app_url(o, lang)}"><img src="{icon(o, 144)}" width="40" height="40" alt="" loading="lazy"><span>{esc(o["name"])}</span></a>' for o in APPS if o is not app)
    langs_chip = " · ".join(app["app_langs"]) if len(app["app_langs"]) > 1 else LANG_NAMES[app["app_langs"][0]]
    other = "it" if lang == "en" else "en"
    title = f"{app['name']} · {t['doc_privacy']} & {t['terms']} — Alessandro"
    desc = app["desc"][lang]
    return (head(lang, title, desc, app_url(app, lang), {l: app_url(app, l) for l in UI_LANGS}, assets, og_image=icon(app))
            + nav(lang, app_url(app, other), [(t["back"], f"{home_url(lang)}#apps"), (t["doc_privacy"], "#privacy"), (t["support"], "#support")])
            + f"""<main style="--c:{app['c2']}">
<section class="ahero">
 <div class="aicon in" style="animation-delay:.1s"><div class="tilt"><img src="{icon(app)}" width="512" height="512" alt="{esc(app['name'])}" fetchpriority="high"><div class="gloss"></div><div class="refl" aria-hidden="true"><img src="{icon(app)}" alt=""></div></div></div>
 <div>
  <a class="crumb mono in" href="{home_url(lang)}#apps">← {t['back']}</a>
  <div class="cat mono in" style="animation-delay:.05s">{esc(app['cat'][lang])}</div>
  <h1 class="in" style="animation-delay:.12s">{esc(app['name'])}</h1>
  <p class="in" style="animation-delay:.2s">{esc(desc)}</p>
  <div class="chip in" style="animation-delay:.28s"><span>{t['iphone']}</span><span>{langs_chip}</span><span>{t['free']}</span></div>
  <div class="cta in" style="animation-delay:.36s"><a class="btn p" href="{app['appstore']}" target="_blank" rel="noopener"> {t['get_app']} ↗</a><a class="btn s" href="#support">{t['support']}</a></div>
 </div>
</section>

<section class="docs" id="docs" data-type="privacy" data-lang="{default}">
 <span id="privacy" class="sr"></span><span id="terms" class="sr"></span>
 <div class="dhead">
  <div class="seg" role="tablist" aria-label="Document"><button type="button" data-t="privacy" aria-selected="true">{t['doc_privacy']}</button><button type="button" data-t="terms" aria-selected="false">{t['doc_terms']}</button></div>
  <div class="seg l" role="tablist" aria-label="{t['doc_lang']}"{' hidden' if len(priv_langs) < 2 else ''}>{lang_btns}</div>
 </div>
 <div class="dbody">{''.join(panes)}</div>
</section>

<section class="sup rv" id="support">
 <div><div class="eyebrow mono">{t['support']}</div><h2>{t['support_title'].format(name=esc(app['name']))}</h2><p>{t['support_text']}</p></div>
 <a class="btn p" href="mailto:{EMAIL}?subject={esc(app['name'])}">{EMAIL}</a>
</section>

<section class="more rv"><div class="eyebrow mono">{t['more_apps']}</div><div class="row">{others}</div></section>
""" + footer(lang))


# ---------------------------------------------------------------- misc pages
def not_found(assets):
    t = T["en"]
    return (head("en", "404 — Alessandro", t["notfound_text"], "/404.html", {l: home_url(l) for l in UI_LANGS}, assets)
            + nav("en", "/it/", [(t["nav_home"], "/")])
            + f"""<main><section class="hero" style="grid-template-columns:1fr;text-align:center;justify-items:center">
<div><div class="win" style="transform:none;margin:0 auto 40px;text-align:left"><div class="bar"><i></i><i></i><i></i><span class="mono">alessandro — zsh</span></div>
<div class="tb" style="min-height:0"><span class="p">alessandro@mac</span> <span class="d">~ %</span> <span class="h">cd ./this-page</span><br><span style="color:#fca5a5">cd: no such file or directory</span><br><span class="p">alessandro@mac</span> <span class="d">~ %</span> <span class="cur"></span></div></div>
<h1 style="font-size:clamp(40px,6vw,72px);margin-bottom:14px">404</h1><p class="lead" style="margin:0 auto 30px">{t['notfound_text']} · {T['it']['notfound_text']}</p>
<a class="btn p" href="/">← Home</a></div></section>""" + footer("en"))


FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="15" fill="#0b0d13"/><path d="M17 22l10 10-10 10" fill="none" stroke="#5eead4" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><rect x="31" y="40" width="16" height="5" rx="2.5" fill="#5eead4"/></svg>"""


def main():
    assets = build_assets()
    (OUT / "assets/favicon.svg").write_text(FAVICON_SVG)
    urls = []
    for lang in UI_LANGS:
        write(home_url(lang), home(lang, assets)); urls.append(home_url(lang))
        for app in APPS:
            write(app_url(app, lang), app_page(app, lang, assets)); urls.append(app_url(app, lang))
    write("/404.html", not_found(assets))
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                     + "".join(f"<url><loc>{SITE_URL}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    (OUT / ".nojekyll").write_text("")
    print(f"built {len(urls)} pages")


if __name__ == "__main__":
    main()
