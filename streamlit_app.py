"""Digital resume of Harsha Vardhan Marothu (Streamlit)."""

from html import escape

import streamlit as st

import resume_data as R
from resume_pdf import build_pdf, qr_svg

P = R.PROFILE

st.set_page_config(
    page_title=f"{P['name']} | Resume",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed",
)


@st.cache_data(show_spinner=False)
def pdf_bytes() -> bytes:
    return build_pdf()


@st.cache_data(show_spinner=False)
def qr_markup() -> str:
    return qr_svg(R.RESUME_URL, 128)


def html(markup: str) -> None:
    """Render raw HTML. Lines are flattened so Markdown never treats them as code."""
    flat = "".join(line.strip() for line in markup.splitlines())
    st.markdown(flat, unsafe_allow_html=True)


def link(url: str, label: str, cls: str = "") -> str:
    return f'<a class="{cls}" href="{escape(url)}" target="_blank" rel="noopener">{escape(label)}</a>'


# ---------------------------------------------------------------- styles
html(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root{--navy:#0B2545;--navy2:#13315C;--teal:#0F766E;--teal-l:#14B8A6;--ink:#1F2937;--muted:#5B6472;--line:#E2E8F0;--soft:#F1F5F9;--bg:#F6F8FB;}
html,body,.stApp{background:var(--bg)!important;}
.stApp, .stApp *{font-family:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;}
#MainMenu, footer, header[data-testid="stHeader"]{display:none!important;}
.block-container{max-width:880px!important;padding:1.6rem 1rem 3rem!important;}
.stMarkdown p{margin:0;}
div[data-testid="stVerticalBlock"]{gap:0.9rem;}
.hero{position:relative;overflow:hidden;background:linear-gradient(135deg,var(--navy) 0%,var(--navy2) 62%,#0E5A62 100%);color:#fff;border-radius:20px;padding:34px 34px 28px;box-shadow:0 10px 30px rgba(11,37,69,.18);}
.hero:after{content:"";position:absolute;right:-80px;top:-80px;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(20,184,166,.35),rgba(20,184,166,0) 70%);}
.hero .eyebrow{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:#99F6E4;font-weight:600;}
.hero h1{font-size:2.35rem;line-height:1.1;margin:.35rem 0 .45rem;font-weight:800;letter-spacing:-.01em;color:#fff;padding:0;}
.hero .headline{font-size:1.02rem;color:#E2E8F0;font-weight:500;}
.hero .tagline{font-size:.92rem;color:#94A3B8;margin-top:.2rem;}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px;position:relative;z-index:1;}
.chip{display:inline-flex;align-items:center;gap:6px;padding:7px 12px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);color:#F8FAFC!important;font-size:.84rem;text-decoration:none!important;}
a.chip:hover{background:rgba(20,184,166,.25);border-color:rgba(153,246,228,.5);}
.hero{margin-bottom:10px;}.card{margin:4px 0 6px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 24px;box-shadow:0 1px 2px rgba(15,23,42,.04);}
.sec-title{display:flex;align-items:center;gap:10px;font-size:.8rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);margin-bottom:14px;}
.sec-title:before{content:"";width:4px;height:16px;border-radius:2px;background:var(--teal);}
.body{color:var(--ink);font-size:.97rem;line-height:1.65;}
.proj-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.proj{border:1px solid var(--line);border-radius:14px;padding:18px;background:linear-gradient(180deg,#fff, #FBFDFE);display:flex;flex-direction:column;}
.proj .tag{align-self:flex-start;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);background:#E6F6F4;padding:4px 9px;border-radius:999px;}
.proj h3{font-size:1.08rem;margin:.6rem 0 .35rem;color:var(--navy);font-weight:700;padding:0;}
.proj .desc{color:var(--ink);font-size:.9rem;line-height:1.55;}
.proj .detail{color:var(--muted);font-size:.84rem;line-height:1.5;margin-top:.45rem;}
.tech{display:flex;flex-wrap:wrap;gap:6px;margin:.8rem 0 .9rem;}
.tech span{font-size:.74rem;color:var(--navy);background:var(--soft);border:1px solid var(--line);padding:3px 8px;border-radius:6px;}
.btns{display:flex;gap:8px;margin-top:auto;flex-wrap:wrap;}
.btn{font-size:.82rem;font-weight:600;padding:8px 13px;border-radius:9px;text-decoration:none!important;}
.btn.primary{background:var(--navy);color:#fff!important;}
.btn.primary:hover{background:var(--teal);}
.btn.ghost{border:1px solid var(--line);color:var(--navy)!important;background:#fff;}
.btn.ghost:hover{border-color:var(--teal);color:var(--teal)!important;}
.tl-item{position:relative;padding-left:20px;}
.tl-item + .tl-item{margin-top:16px;}
.tl-item:before{content:"";position:absolute;left:0;top:7px;width:9px;height:9px;border-radius:50%;background:var(--teal);box-shadow:0 0 0 4px #E6F6F4;}
.tl-head{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:baseline;}
.tl-title{font-weight:700;color:var(--navy);font-size:1rem;}
.tl-date{font-size:.82rem;color:var(--muted);white-space:nowrap;}
.tl-sub{color:var(--muted);font-size:.9rem;margin-top:2px;}
.tl-note{color:var(--teal);font-weight:600;}
.tl-list{margin:.5rem 0 0;padding-left:1.1rem;color:var(--ink);font-size:.92rem;line-height:1.6;}
.tl-list li{margin:.2rem 0;}
.skill-row{display:grid;grid-template-columns:130px 1fr;gap:10px;align-items:start;}
.skill-row + .skill-row{margin-top:12px;}
.skill-label{font-weight:600;color:var(--navy);font-size:.88rem;padding-top:4px;}
.skill-chips{display:flex;flex-wrap:wrap;gap:6px;}
.skill-chips span{font-size:.82rem;color:var(--ink);background:var(--soft);border:1px solid var(--line);padding:4px 10px;border-radius:999px;}
.lang + .lang{margin-top:14px;}
.lang-head{display:flex;justify-content:space-between;font-size:.9rem;}
.lang-name{font-weight:600;color:var(--navy);}
.lang-level{color:var(--muted);font-size:.84rem;}
.bar{height:7px;background:var(--soft);border-radius:999px;margin-top:6px;overflow:hidden;}
.bar i{display:block;height:100%;border-radius:999px;background:linear-gradient(90deg,var(--teal),var(--teal-l));}
.share{display:flex;gap:22px;align-items:center;}
.share .qr{flex:0 0 auto;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px;line-height:0;}
.share .qr svg{width:116px;height:116px;}
.share h4{margin:0 0 .3rem;color:var(--navy);font-size:1rem;font-weight:700;padding:0;}
.share p{color:var(--muted)!important;font-size:.88rem;line-height:1.5;}
.share a{color:var(--teal)!important;font-weight:600;}
.foot{text-align:center;color:#94A3B8;font-size:.78rem;margin-top:.4rem;}
div[data-testid="stDownloadButton"] button, div[data-testid="stLinkButton"] a{width:100%;border-radius:12px!important;padding:.7rem 1rem!important;font-weight:600!important;}
div[data-testid="stDownloadButton"] button{background:var(--teal)!important;color:#fff!important;border:1px solid var(--teal)!important;}
div[data-testid="stDownloadButton"] button:hover{background:#0B5F58!important;border-color:#0B5F58!important;}
div[data-testid="stDownloadButton"] button p, div[data-testid="stLinkButton"] a p{font-weight:600!important;}
div[data-testid="stLinkButton"] a{background:#fff!important;color:var(--navy)!important;border:1px solid var(--line)!important;}
div[data-testid="stLinkButton"] a:hover{border-color:var(--teal)!important;color:var(--teal)!important;}
@media (max-width:640px){
.hero{padding:26px 20px 22px;border-radius:16px;}
.hero h1{font-size:1.75rem;}
.card{padding:18px 16px;}
.proj-grid{grid-template-columns:1fr;}
.skill-row{grid-template-columns:1fr;gap:6px;}
.share{flex-direction:column;align-items:flex-start;}
}
</style>
"""
)

# ---------------------------------------------------------------- hero
chips = "".join(
    [
        f'<span class="chip">📍 {escape(P["location"])}</span>',
        f'<a class="chip" href="mailto:{escape(P["email"])}">✉️ {escape(P["email"])}</a>',
        f'<a class="chip" href="{P["phone_link"]}">📞 {escape(P["phone"])}</a>',
        f'<a class="chip" href="{escape(P["linkedin"])}" target="_blank" rel="noopener">💼 LinkedIn</a>',
        f'<a class="chip" href="{escape(P["portfolio"])}" target="_blank" rel="noopener">🎬 Portfolio</a>',
    ]
)
html(
    f"""
<div class="hero">
<div class="eyebrow">Digital Resume</div>
<h1>{escape(P["name"])}</h1>
<div class="headline">{escape(P["headline"])}</div>
<div class="tagline">{escape(P["tagline"])}</div>
<div class="chips">{chips}</div>
</div>
"""
)

c1, c2 = st.columns(2)
with c1:
    st.download_button(
        "⬇️  Download PDF Resume",
        data=pdf_bytes(),
        file_name=R.PDF_FILE_NAME,
        mime="application/pdf",
        on_click="ignore",
        width="stretch",
    )
with c2:
    st.link_button("Connect on LinkedIn  ↗", P["linkedin"], width="stretch")

# ---------------------------------------------------------------- summary
html(
    f"""
<div class="card">
<div class="sec-title">About</div>
<div class="body">{escape(R.SUMMARY)}</div>
</div>
"""
)

# ---------------------------------------------------------------- projects
proj_cards = ""
for pr in R.PROJECTS:
    tech = "".join(f"<span>{escape(t)}</span>" for t in pr["tech"])
    proj_cards += f"""
<div class="proj">
<span class="tag">{escape(pr["category"])}</span>
<h3>{escape(pr["name"])}</h3>
<div class="desc">{escape(pr["description"])}</div>
<div class="detail">{escape(pr["detail"])}</div>
<div class="tech">{tech}</div>
<div class="btns">{link(pr["url"], "Open live app ↗", "btn primary")}{link(pr["source"], "Source code", "btn ghost")}</div>
</div>
"""
html(f'<div class="card"><div class="sec-title">Projects</div><div class="proj-grid">{proj_cards}</div></div>')

# ---------------------------------------------------------------- experience
exp_items = ""
for ex in R.EXPERIENCE:
    points = "".join(f"<li>{escape(p)}</li>" for p in ex["points"])
    exp_items += f"""
<div class="tl-item">
<div class="tl-head"><span class="tl-title">{escape(ex["role"])}</span><span class="tl-date">{escape(ex["dates"])}</span></div>
<div class="tl-sub">{escape(ex["org"])}</div>
<ul class="tl-list">{points}</ul>
</div>
"""
html(f'<div class="card"><div class="sec-title">Experience</div>{exp_items}</div>')

# ---------------------------------------------------------------- education
edu_items = ""
for e in R.EDUCATION:
    note = f' · <span class="tl-note">{escape(e["note"])}</span>' if e["note"] else ""
    edu_items += f"""
<div class="tl-item">
<div class="tl-head"><span class="tl-title">{escape(e["degree"])}</span><span class="tl-date">{escape(e["dates"])}</span></div>
<div class="tl-sub">{escape(e["school"])}{note}</div>
</div>
"""
html(f'<div class="card"><div class="sec-title">Education</div>{edu_items}</div>')

# ---------------------------------------------------------------- skills
skill_rows = ""
for label, items in R.SKILLS:
    chips_html = "".join(f"<span>{escape(i)}</span>" for i in items)
    skill_rows += f'<div class="skill-row"><div class="skill-label">{escape(label)}</div><div class="skill-chips">{chips_html}</div></div>'
html(f'<div class="card"><div class="sec-title">Skills</div>{skill_rows}</div>')

# ---------------------------------------------------------------- languages
langs = ""
for l in R.LANGUAGES:
    pct = int(l["level"] / 5 * 100)
    langs += f"""
<div class="lang">
<div class="lang-head"><span class="lang-name">{escape(l["name"])}</span><span class="lang-level">{escape(l["level_text"])}</span></div>
<div class="bar"><i style="width:{pct}%"></i></div>
</div>
"""
html(f'<div class="card"><div class="sec-title">Languages</div>{langs}</div>')

# ---------------------------------------------------------------- share
html(
    f"""
<div class="card share">
<div class="qr">{qr_markup()}</div>
<div>
<h4>Share this resume</h4>
<p>Scan the QR code to open this page on a phone, or share the link:<br>{link(R.RESUME_URL, R.RESUME_URL_LABEL)}</p>
<p style="margin-top:.5rem">Reach me at {f'<a href="mailto:{escape(P["email"])}">{escape(P["email"])}</a>'} · {escape(P["phone"])}</p>
</div>
</div>
<div class="foot">© {escape(P["name"])} · Built with Python &amp; Streamlit</div>
"""
)
