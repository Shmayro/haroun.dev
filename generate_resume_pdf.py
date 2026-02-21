# generate_resume_pdf.py
# Generates: Haroun_Resume_Final_v6.pdf (clickable links, same as provided)

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import BaseDocTemplate, Paragraph, Spacer, Frame, PageTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Resume content (as used in Haroun_Resume_Final_v6.pdf)
summary = (
    "Results-driven Senior Software Engineer with 8+ years of experience in full-stack development, "
    "technical leadership, and cloud-native solutions. Proven expertise in designing, building, and optimizing "
    "enterprise-scale applications with Java, Kotlin, Spring Boot, and Angular. Strong background in DevOps, "
    "Kubernetes, and AWS, combined with mentoring and code quality leadership. Enthusiastic about AI/ML, "
    "process mining, and performance engineering, with a strong ability to bridge technical depth and business needs."
)

skills = [
    ["Backend:", "Java, Kotlin, Spring Boot (Web/Data/Cloud/Security), Hibernate"],
    ["Frontend:", "Angular (12+), Vue.js, TypeScript, JavaScript"],
    ["Cloud/DevOps:", "Kubernetes, Helm, Docker, AWS, Jenkins, GitHub Actions"],
    ["Databases:", "PostgreSQL, Oracle, MySQL, MongoDB"],
    ["Testing & Performance:", "Gatling, JUnit 5, Selenium, Cypress"],
    ["Other:", "R, Python, BPMN, Process Mining, AI/ML (enthusiast)"],
]

experience = [
    (
        "Bonitasoft – R&D Runtime Full Stack Engineer",
        "Sept 2021 – Present | Grenoble, France",
        [
            "Led development and optimization of Bonita runtimes for scalability and performance.",
            "Designed and implemented a real-time monitoring dashboard for applications, processes, and license management.",
            "Built a performance testing solution with Gatling, Scala, Docker, AWS.",
            "Conducted R&D on data mining, process mining, and BPMN model generation.",
            "Ensured code quality through reviews, mentoring, and technical leadership.",
            "Exploring and prototyping next-generation AI-powered solutions by leveraging LangGraph and LightRAG for intelligent business workflow automation and agent-based process orchestration.",
        ],
    ),
    (
        "Meritis (BNP Paribas) – Full Stack Java/Angular Consultant",
        "Feb 2020 – Sept 2021 | Aix-en-Provence, France",
        [
            "Developed a Spring Boot API for enterprise data aggregation (KYC).",
            "Served as Tech Lead on 3 projects, overseeing delivery quality and CI/CD pipelines.",
            "Implemented automated delivery pipelines with Jenkins to reduce deployment costs.",
            "Mentored new hires and conducted code reviews.",
        ],
    ),
    (
        "SmartTrade Technologies – Software Engineer (Java/JEE)",
        "Apr 2017 – Jan 2020 | Aix-en-Provence, France",
        [
            "Developed a cloud supervision tool for SmartTrade platforms.",
            "Built a QA automation framework for functional UI testing integrated into CI/CD.",
            "Created a Docker-based deployment platform for SmartTrade environments.",
            "Designed Jira REST API-based dashboards for release tracking.",
        ],
    ),
    (
        "Freelance & Early Experience",
        "2013–2016",
        [
            "Built web/mobile applications for SMEs and organizations (management apps, WordPress sites).",
            "Developed academic projects (career platforms, event booking, GIS wildfire simulation).",
        ],
    ),
]

education = [
    "Master’s in Software Reliability, Security & Integration – Aix-Marseille Univ. (2017)",
    "Master’s in Computer Science – Aix-Marseille Univ. (2016)",
    "Bachelor in Software Engineering – High-Tech School, Rabat (2015)",
    "Advanced Diploma in Software Development – ISTA Fès (2013)",
    "High School Diploma in Physics-Chemistry – Fès, Morocco (2011)",
]

languages = "English (professional), French (fluent), Arabic (native)"
interests = "Technology, music, chess, video games, tennis"


def build_resume_with_links(output_pdf_path: str) -> None:
    doc = BaseDocTemplate(
        output_pdf_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
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

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 20, id="normal")
    template = PageTemplate(id="resume", frames=frame)
    doc.addPageTemplates([template])

    story = []

    # Header with visible + clickable links
    story.append(Paragraph("Haroun EL ALAMI", title_style))
    story.append(Paragraph("Senior Full Stack Software Engineer | Tech Lead", subtitle_style))
    story.append(
        Paragraph(
            "Marseille, France | <a href='mailto:me@haroun.dev'>me@haroun.dev</a> | +33 6 42 20 17 50",
            normal,
        )
    )
    story.append(
        Paragraph(
            "<a href='https://linkedin.com/in/harounelalami'>linkedin.com/in/harounelalami</a> | "
            "<a href='https://haroun.dev'>haroun.dev</a> | "
            "<a href='https://github.com/Shmayro'>github.com/Shmayro</a>",
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
    projects = [
        (
            "dockerify-android – Dockerized Android Emulator (2024)",
            "Developed a Docker-based Android emulator supporting multiple CPU architectures (x86, arm64 planned), "
            "with ADB integration and scrcpy-web for browser-based real-time control. "
            "The project has gained strong community traction with 350+ stars and 29 forks on GitHub. "
            "Source: <a href='https://github.com/Shmayro/dockerify-android'>GitHub</a>",
        ),
        (
            "Getjobs – Job Search Engine (2018)",
            "Designed and developed a career platform with job search and CV builder using Vue.js, Laravel, and REST APIs.",
        ),
        (
            "PyTank – Educational Python Game (2015)",
            "Built a gamified learning platform to teach Python through algorithmic tank battles.",
        ),
        (
            "YHEventApp – Event Booking Web App (2015)",
            "Implemented a system to manage event registrations and visualizations with PHP, MySQL, and Chart.js.",
        ),
        (
            "University Management System (2014)",
            "Created an application for academic management (students, schedules, grades) with automated timetable generation.",
        ),
    ]
    for title, desc in projects:
        story.append(Paragraph(f"<b>{title}</b>", normal))
        story.append(Paragraph(desc, normal))
        story.append(Spacer(1, 4))

    # Education
    story.append(Paragraph("Education", section_style))
    for edu in education:
        story.append(Paragraph(f"• {edu}", normal))

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
    build_resume_with_links("Haroun_Resume_Final_v6.pdf")
