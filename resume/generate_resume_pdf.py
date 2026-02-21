# generate_resume_pdf.py
# Generates a date-versioned resume PDF: Haroun_EL_ALAMI_CV-DDMMYYYY.pdf
#
# Usage:
#   python generate_resume_pdf.py                  # outputs to current dir
#   python generate_resume_pdf.py --output-dir /path/to/dir

import argparse
import json
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import BaseDocTemplate, Paragraph, Spacer, Frame, PageTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Load resume content from JSON
_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_dir, "resume-data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

EN_DASH = "\u2013"

summary = data["summary"]
skills = [[s["category"] + ":", s["items"]] for s in data["skills"]]
experience = [
    (
        f"{e['company']} {EN_DASH} {e['role']}" if e["role"] else e["company"],
        f"{e['period']}" + (f" | {e['location']}" if e.get("location") else ""),
        e["bullets"],
    )
    for e in data["experience"]
]
education = [
    f"{e['degree']} {EN_DASH} {e['school']} ({e['year']})" for e in data["education"]
]
languages = ", ".join(f"{lang['language']} ({lang['level']})" for lang in data["languages"])
interests = ", ".join(data["interests"])


def build_resume_with_links(output_pdf_path: str) -> None:
    doc = BaseDocTemplate(
        output_pdf_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=30,
        bottomMargin=30,
    )
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    normal.fontSize = 10
    normal.leading = 13

    # Custom styles (same as used)
    title_style = ParagraphStyle(
        name="Title",
        fontSize=20,
        leading=24,
        alignment=1,
        textColor=colors.HexColor("#2E4053"),
        spaceAfter=12,
    )
    subtitle_style = ParagraphStyle(
        name="Subtitle",
        fontSize=12,
        leading=14,
        alignment=1,
        textColor=colors.HexColor("#34495E"),
        spaceAfter=20,
    )
    section_style = ParagraphStyle(
        name="Section",
        fontSize=13,
        leading=16,
        spaceBefore=14,
        spaceAfter=6,
        textColor=colors.HexColor("#2874A6"),
    )
    bullet_style = ParagraphStyle(
        name="Bullet",
        fontSize=10,
        leading=13,
        leftIndent=15,
        bulletIndent=5,
    )
    footer_style = ParagraphStyle(
        name="Footer",
        fontSize=8,
        leading=10,
        alignment=2,
        textColor=colors.grey,
    )

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    template = PageTemplate(id="resume", frames=frame)
    doc.addPageTemplates([template])

    story = []

    # Header with visible + clickable links
    story.append(Paragraph(data["name"], title_style))
    story.append(Paragraph(data["title"], subtitle_style))
    story.append(
        Paragraph(
            f"{data['location']} | <a href='mailto:{data['email']}'>{data['email']}</a> | {data['phone']}",
            normal,
        )
    )
    story.append(
        Paragraph(
            f"<a href='https://{data['linkedin']}'>{data['linkedin']}</a> | "
            f"<a href='https://{data['website']}'>{data['website']}</a> | "
            f"<a href='https://{data['github']}'>{data['github']}</a>",
            normal,
        )
    )
    story.append(Spacer(1, 12))

    # Summary
    story.append(Paragraph("Professional Summary", section_style))
    story.append(Paragraph(summary, normal))

    # Skills
    story.append(Paragraph("Core Skills", section_style))
    for cat, desc in skills:
        story.append(Paragraph(f"<b>{cat}</b> {desc}", normal))

    # Experience
    story.append(Paragraph("Professional Experience", section_style))
    for job, date, bullets in experience:
        story.append(Paragraph(f"<b>{job}</b>", normal))
        story.append(Paragraph(f"<i>{date}</i>", normal))
        for b in bullets:
            story.append(Paragraph(b, bullet_style))
        story.append(Spacer(1, 6))

    # Personal Projects (same as v6: dockerify-android included with Source: GitHub)
    story.append(PageBreak())
    story.append(Paragraph("Personal Projects", section_style))
    projects = []
    for p in data["projects"]:
        if p["name"] != p["title"]:
            title = f"{p['name']} {EN_DASH} {p['title']} ({p['year']})"
        else:
            title = f"{p['name']} ({p['year']})"
        desc = p["description"]
        if p.get("url"):
            desc += f" Source: <a href='{p['url']}'>GitHub</a>"
        projects.append((title, desc))
    for title, desc in projects:
        story.append(Paragraph(f"<b>{title}</b>", normal))
        story.append(Paragraph(desc, normal))
        story.append(Spacer(1, 4))

    # Education
    story.append(Paragraph("Education", section_style))
    for edu in education:
        story.append(Paragraph(f"\u2022 {edu}", normal))

    # Languages
    story.append(Paragraph("Languages", section_style))
    story.append(Paragraph(languages, normal))

    # Interests
    story.append(Paragraph("Interests", section_style))
    story.append(Paragraph(interests, normal))

    # Footer with last updated date
    last_updated = datetime.now().strftime("%B %d, %Y")
    story.append(Spacer(1, 20))
    story.append(Paragraph(f"Last updated: {last_updated}", footer_style))

    doc.build(story)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate resume PDF")
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to write the PDF to (default: current directory)",
    )
    args = parser.parse_args()

    date_stamp = datetime.now().strftime("%d%m%Y")
    filename = f"Haroun_EL_ALAMI_CV-{date_stamp}.pdf"
    output_path = os.path.join(args.output_dir, filename)

    os.makedirs(args.output_dir, exist_ok=True)
    build_resume_with_links(output_path)
    print(output_path)
