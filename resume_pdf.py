"""Builds the one-page PDF resume (with a QR code to the digital resume)."""

from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.graphics import renderPDF, renderSVG
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

import resume_data as R

NAVY = HexColor("#0B2545")
TEAL = HexColor("#0F766E")
INK = HexColor("#1F2937")
MUTED = HexColor("#5B6472")
RULE = HexColor("#CBD5E1")
SOFT = HexColor("#F1F5F9")

PAGE_W, PAGE_H = A4
MARGIN = 42
CONTENT_W = PAGE_W - 2 * MARGIN


def qr_drawing(value: str, size: float, color=NAVY) -> Drawing:
    widget = QrCodeWidget(value, barLevel="M", barBorder=0)
    widget.barFillColor = color
    widget.barStrokeColor = color
    x0, y0, x1, y1 = widget.getBounds()
    w, h = x1 - x0, y1 - y0
    d = Drawing(size, size, transform=[size / w, 0, 0, size / h, 0, 0])
    d.add(widget)
    return d


def qr_svg(value: str = R.RESUME_URL, size: int = 132) -> str:
    """QR code as an SVG string (used on the website)."""
    svg = renderSVG.drawToString(qr_drawing(value, size))
    start = svg.find("<svg")
    return svg[start:] if start >= 0 else svg


def _style(name, font="Helvetica", size=9.5, leading=13.2, color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading, textColor=color, **kw)


BODY = _style("body")
BODY_MUTED = _style("muted", font="Helvetica-Oblique", size=8.8, leading=12, color=MUTED)
BULLET = _style("bullet", leftIndent=11, bulletIndent=1, bulletFontName="Helvetica-Bold", bulletColor=TEAL)
CONTACT = _style("contact", size=8.8, leading=12.6, color=INK)


def _link(url, label, color="#0F766E"):
    return f'<link href="{escape(url)}" color="{color}">{escape(label)}</link>'


class _Writer:
    def __init__(self, c: canvas.Canvas):
        self.c = c
        self.y = PAGE_H - MARGIN

    def para(self, html, style, x=MARGIN, width=CONTENT_W, space_after=0, bullet=None):
        p = Paragraph(html, style, bulletText=bullet)
        _, h = p.wrap(width, PAGE_H)
        p.drawOn(self.c, x, self.y - h)
        self.y -= h + space_after
        return h

    def section(self, title):
        self.y -= 13
        c = self.c
        c.setFillColor(TEAL)
        c.rect(MARGIN, self.y - 8.2, 3, 10.5, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(MARGIN + 9, self.y - 7, title.upper(), charSpace=1.1)
        tw = stringWidth(title.upper(), "Helvetica-Bold", 10.5) + 1.1 * len(title)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.7)
        c.line(MARGIN + 9 + tw + 8, self.y - 3.5, PAGE_W - MARGIN, self.y - 3.5)
        self.y -= 19

    def entry_head(self, left, right, left_font="Helvetica-Bold", left_size=10.2):
        c = self.c
        c.setFillColor(INK)
        c.setFont(left_font, left_size)
        c.drawString(MARGIN, self.y - left_size, left)
        if right:
            c.setFillColor(MUTED)
            c.setFont("Helvetica", 8.8)
            c.drawRightString(PAGE_W - MARGIN, self.y - left_size + 0.5, right)
        self.y -= left_size + 3.5


def _header(w: _Writer):
    c = w.c
    p = R.PROFILE
    qr_size = 64
    qr_x = PAGE_W - MARGIN - qr_size
    qr_top = PAGE_H - MARGIN + 2

    # Name + headline
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 23)
    c.drawString(MARGIN, PAGE_H - MARGIN - 18, p["name"].upper(), charSpace=0.6)
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(MARGIN, PAGE_H - MARGIN - 35, p["headline"])
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9.2)
    c.drawString(MARGIN, PAGE_H - MARGIN - 48, p["tagline"])

    # Contact block (kept clear of the QR column)
    w.y = PAGE_H - MARGIN - 56
    contact_w = qr_x - MARGIN - 128
    sep = '  <font color="#94A3B8">|</font>  '
    lines = [
        escape(p["location"]) + sep + _link(p["phone_link"], p["phone"], "#1F2937"),
        _link("mailto:" + p["email"], p["email"]) + sep + "LinkedIn: " + _link(p["linkedin"], p["linkedin_label"]),
        "Portfolio: " + _link(p["portfolio"], p["portfolio_label"]),
    ]
    w.para("<br/>".join(lines), CONTACT, width=contact_w + 128)

    # QR code with caption and clickable link right beside it
    renderPDF.draw(qr_drawing(R.RESUME_URL, qr_size), c, qr_x, qr_top - qr_size)
    c.linkURL(R.RESUME_URL, (qr_x, qr_top - qr_size, qr_x + qr_size, qr_top), relative=0, thickness=0)

    # Caption sits beside the lower half of the QR, below the name line
    cap_right = qr_x - 9
    base = qr_top - qr_size + 6
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawRightString(cap_right, base + 24, "DIGITAL RESUME")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.8)
    c.drawRightString(cap_right, base + 12.5, "Scan the QR code or click:")
    label = R.RESUME_URL_LABEL
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawRightString(cap_right, base, label)
    lw = stringWidth(label, "Helvetica-Bold", 8.2)
    c.setStrokeColor(TEAL)
    c.setLineWidth(0.5)
    c.line(cap_right - lw, base - 1.6, cap_right, base - 1.6)
    c.linkURL(R.RESUME_URL, (cap_right - lw, base - 4, cap_right, base + 8), relative=0, thickness=0)

    # Header rule
    w.y = min(w.y, qr_top - qr_size) - 10
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.4)
    c.line(MARGIN, w.y, PAGE_W - MARGIN, w.y)
    w.y -= 2


def build_pdf() -> bytes:
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    c.setTitle(f"{R.PROFILE['name']} – Resume")
    c.setAuthor(R.PROFILE["name"])
    c.setSubject("Resume")
    c.setKeywords("resume, computer science, python, machine learning, 3D")
    c.setFillColor(white)

    w = _Writer(c)
    _header(w)

    # Summary
    w.section("Professional Summary")
    w.para(escape(R.SUMMARY), BODY)

    # Education
    w.section("Education")
    for i, e in enumerate(R.EDUCATION):
        w.entry_head(e["degree"], e["dates"])
        line = escape(e["school"])
        if e["note"]:
            line += f'  <font color="#0F766E">·  {escape(e["note"])}</font>'
        w.para(line, BODY, space_after=7 if i < len(R.EDUCATION) - 1 else 0)

    # Projects
    w.section("Projects")
    for i, pr in enumerate(R.PROJECTS):
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 10.2)
        c.drawString(MARGIN, w.y - 10.2, pr["name"])
        links = "Live app: " + _link(pr["url"], pr["url_label"])
        lp = Paragraph(links, _style("lnk", size=8.8, leading=11, alignment=2))
        _, lh = lp.wrap(260, 40)
        lp.drawOn(c, PAGE_W - MARGIN - 260, w.y - 10.6)
        w.y -= 14
        w.para(escape(pr["description"] + " " + pr["detail"]), BODY, space_after=1.5)
        w.para("Tech: " + escape(", ".join(pr["tech"])), BODY_MUTED,
               space_after=7 if i < len(R.PROJECTS) - 1 else 0)

    # Experience
    w.section("Experience")
    for ex in R.EXPERIENCE:
        w.entry_head(ex["role"], ex["dates"])
        w.para(f'<i>{escape(ex["org"])}</i>', _style("org", size=9, leading=12, color=MUTED), space_after=1.5)
        for pt in ex["points"]:
            w.para(escape(pt), BULLET, bullet="•", space_after=1)

    # Skills
    w.section("Technical & Soft Skills")
    label_w = 92
    for label, items in R.SKILLS:
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 9.3)
        c.drawString(MARGIN, w.y - 9.6, label)
        w.para(escape(",  ".join(items)), BODY, x=MARGIN + label_w, width=CONTENT_W - label_w, space_after=2.5)

    # Languages
    w.section("Languages")
    parts = [f'<b>{escape(l["name"])}</b> <font color="#5B6472">({escape(l["level_text"])})</font>' for l in R.LANGUAGES]
    w.para('<font color="#94A3B8">   |   </font>'.join(parts), BODY)

    c.showPage()
    c.save()
    return buf.getvalue()


if __name__ == "__main__":
    import sys

    out = sys.argv[1] if len(sys.argv) > 1 else R.PDF_FILE_NAME
    with open(out, "wb") as f:
        f.write(build_pdf())
    print("wrote", out)
