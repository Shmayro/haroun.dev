# generate_resume_html_and_zip.py
# Generates: Haroun_Resume.html, Haroun_Resume.pdf, Haroun_Resume_Package.zip
# HTML contains a Download PDF button pointing to ./Haroun_Resume.pdf

import os, shutil, zipfile
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, "Haroun_Resume.html")
pdf_src = os.path.join(base_dir, "Haroun_Resume_Final_v6.pdf")
pdf_dst = os.path.join(base_dir, "Haroun_Resume.pdf")
zip_path = os.path.join(base_dir, "Haroun_Resume_Package.zip")

# Copy the PDF to a friendly name expected by the HTML
if os.path.exists(pdf_src):
    shutil.copyfile(pdf_src, pdf_dst)
else:
    # fallback to any other known name (optional safety)
    for cand in [
        os.path.join(base_dir, "Haroun_Resume_Final_v5.pdf"),
        os.path.join(base_dir, "Haroun_Resume_Final_v4.pdf"),
        os.path.join(base_dir, "Haroun_Resume_Final_v3.pdf"),
        os.path.join(base_dir, "Haroun_Resume_Final_v2.pdf"),
        os.path.join(base_dir, "Haroun_Resume_Final.pdf"),
    ]:
        if os.path.exists(cand):
            shutil.copyfile(cand, pdf_dst)
            break

last_updated = datetime.now().strftime("%B %d, %Y")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Haroun EL ALAMI — Résumé</title>
<style>
  :root {{
    --accent: #2874A6;
    --text: #1f2937;
    --muted: #6b7280;
    --bg: #ffffff;
    --chip: #eef6fc;
    --rule: #e5e7eb;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{
    margin: 0;
    padding: 0;
    background: var(--bg);
    color: var(--text);
    font: 15px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell,
           "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif;
  }}
  .page {{
    max-width: 860px;
    margin: 24px auto 64px;
    padding: 28px 24px;
  }}
  header {{ text-align: center; }}
  h1 {{ margin: 0 0 6px; font-size: 32px; letter-spacing: 0.3px; color: #2E4053; }}
  .subtitle {{ margin: 0 0 16px; font-size: 16px; color: #34495E; }}
  .meta {{ margin: 6px 0; color: var(--muted); }}
  .meta a {{ color: var(--text); text-decoration: none; border-bottom: 1px solid #d1d5db; }}
  .meta a:hover {{ color: var(--accent); border-color: var(--accent); }}
  .cta {{
    display: inline-block;
    margin-top: 16px;
    background: var(--accent);
    color: #fff;
    padding: 10px 16px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: 600;
  }}
  .cta:hover {{ filter: brightness(1.05); }}
  section {{ margin-top: 30px; }}
  h2 {{
    margin: 0 0 10px;
    font-size: 18px;
    color: var(--accent);
    border-bottom: 1px solid var(--rule);
    padding-bottom: 6px;
  }}
  .item {{ margin: 12px 0; }}
  .role {{ font-weight: 700; }}
  .when, .where {{ color: var(--muted); font-style: italic; }}
  ul {{ margin: 8px 0 0 18px; }}
  li {{ margin: 4px 0; }}
  .skills dt {{ font-weight: 700; }}
  .skills dd {{ margin: 2px 0 10px 0; }}
  footer {{ margin-top: 36px; text-align: right; color: var(--muted); font-size: 13px; }}
  .chip {{ display:inline-block; background: var(--chip); color: #0b5394; padding: 2px 8px; border-radius: 999px; font-size: 12px; margin-left: 6px; }}
  @media print {{
    .cta {{ display: none; }}
    .page {{ margin: 0; padding: 0; }}
  }}
</style>
</head>
<body>
  <div class="page">
    <header>
      <h1>Haroun EL ALAMI</h1>
      <p class="subtitle">Senior Full Stack Software Engineer | Tech Lead</p>
      <p class="meta">Marseille, France · <a href="mailto:me@haroun.dev">me@haroun.dev</a> · +33 6 42 20 17 50</p>
      <p class="meta">
        <a href="https://linkedin.com/in/harounelalami">linkedin.com/in/harounelalami</a> ·
        <a href="https://haroun.dev">haroun.dev</a> ·
        <a href="https://github.com/Shmayro">github.com/Shmayro</a>
      </p>
      <a class="cta" href="./Haroun_Resume.pdf" download="Haroun_EL_ALAMI_Resume.pdf">⬇︎ Download PDF</a>
    </header>

    <section>
      <h2>Professional Summary</h2>
      <p>
        Results-driven Senior Software Engineer with 8+ years of experience in full‑stack development, technical leadership,
        and cloud‑native solutions. Proven expertise in designing, building, and optimizing enterprise applications with
        <strong>Java, Kotlin, Spring Boot, and Angular</strong>. Strong background in <strong>DevOps, Kubernetes, AWS</strong>,
        combined with mentoring and code quality leadership. Enthusiastic about <strong>AI/ML, process mining, and performance engineering</strong>,
        with the ability to bridge technical depth and business needs.
      </p>
    </section>

    <section>
      <h2>Core Skills</h2>
      <dl class="skills">
        <dt>Backend</dt><dd>Java, Kotlin, Spring Boot (Web/Data/Cloud/Security), Hibernate</dd>
        <dt>Frontend</dt><dd>Angular (12+), Vue.js, TypeScript, JavaScript</dd>
        <dt>Cloud & DevOps</dt><dd>Kubernetes, Helm, Docker, AWS, Jenkins, GitHub Actions</dd>
        <dt>Databases</dt><dd>PostgreSQL, Oracle, MySQL, MongoDB</dd>
        <dt>Testing & Performance</dt><dd>Gatling, JUnit 5, Selenium, Cypress</dd>
        <dt>Other</dt><dd>R, Python, BPMN, Process Mining, AI/ML (enthusiast)</dd>
      </dl>
    </section>

    <section>
      <h2>Professional Experience</h2>

      <div class="item">
        <div class="role">Bonitasoft — R&amp;D Runtime Full Stack Engineer <span class="chip">Sep 2021 – Present</span></div>
        <div class="when where">Grenoble, France</div>
        <ul>
          <li>Led development and optimization of Bonita runtimes for scalability and performance.</li>
          <li>Designed and implemented a real‑time monitoring dashboard for applications, processes, and license management.</li>
          <li>Built a performance testing solution with Gatling, Scala, Docker, AWS.</li>
          <li>Conducted R&amp;D on data mining, process mining, and BPMN model generation.</li>
          <li>Ensured code quality through reviews, mentoring, and technical leadership.</li>
          <li>Exploring and prototyping next‑generation AI‑powered solutions by leveraging LangGraph and LightRAG for intelligent business workflow automation and agent‑based process orchestration.</li>
        </ul>
      </div>

      <div class="item">
        <div class="role">Meritis (BNP Paribas) — Full Stack Java/Angular Consultant <span class="chip">Feb 2020 – Sep 2021</span></div>
        <div class="when where">Aix‑en‑Provence, France</div>
        <ul>
          <li>Developed a Spring Boot API for enterprise data aggregation (KYC).</li>
          <li>Served as Tech Lead on 3 projects, overseeing delivery quality and CI/CD pipelines.</li>
          <li>Implemented automated delivery pipelines with Jenkins to reduce deployment costs.</li>
          <li>Mentored new hires and conducted code reviews.</li>
        </ul>
      </div>

      <div class="item">
        <div class="role">SmartTrade Technologies — Software Engineer (Java/JEE) <span class="chip">Apr 2017 – Jan 2020</span></div>
        <div class="when where">Aix‑en‑Provence, France</div>
        <ul>
          <li>Developed a cloud supervision tool for SmartTrade platforms.</li>
          <li>Built a QA automation framework for functional UI testing integrated into CI/CD.</li>
          <li>Created a Docker‑based deployment platform for SmartTrade environments.</li>
          <li>Designed Jira REST API‑based dashboards for release tracking.</li>
        </ul>
      </div>

      <div class="item">
        <div class="role">Freelance & Early Experience <span class="chip">2013 – 2016</span></div>
        <ul>
          <li>Built web/mobile applications for SMEs and organizations (management apps, WordPress sites).</li>
          <li>Developed academic projects (career platforms, event booking, GIS wildfire simulation).</li>
        </ul>
      </div>
    </section>

    <section>
      <h2>Personal Projects</h2>

      <div class="item">
        <div class="role">dockerify‑android — Dockerized Android Emulator <span class="chip">2024</span></div>
        <p>
          Developed a Docker‑based Android emulator supporting multiple CPU architectures (x86, arm64 planned),
          with ADB integration and scrcpy‑web for browser‑based real‑time control.
          The project has gained strong community traction with 350+ stars and 29 forks on GitHub.
          <a href="https://github.com/Shmayro/dockerify-android">github.com/Shmayro/dockerify-android</a>
        </p>
      </div>

      <div class="item">
        <div class="role">Getjobs — Job Search Engine <span class="chip">2018</span></div>
        <p>Designed and developed a career platform with job search and CV builder using Vue.js, Laravel, and REST APIs.</p>
      </div>

      <div class="item">
        <div class="role">PyTank — Educational Python Game <span class="chip">2015</span></div>
        <p>Built a gamified learning platform to teach Python through algorithmic tank battles.</p>
      </div>

      <div class="item">
        <div class="role">YHEventApp — Event Booking Web App <span class="chip">2015</span></div>
        <p>Implemented a system to manage event registrations and visualizations with PHP, MySQL, and Chart.js.</p>
      </div>

      <div class="item">
        <div class="role">University Management System <span class="chip">2014</span></div>
        <p>Created an application for academic management (students, schedules, grades) with automated timetable generation.</p>
      </div>
    </section>

    <section>
      <h2>Education</h2>
      <ul>
        <li>Master’s in Software Reliability, Security & Integration — Aix‑Marseille University (2017)</li>
        <li>Master’s in Computer Science — Aix‑Marseille University (2016)</li>
        <li>Bachelor in Software Engineering — High‑Tech School, Rabat (2015)</li>
        <li>Advanced Diploma in Software Development — ISTA Fès (2013)</li>
        <li>High School Diploma in Physics‑Chemistry — Fès, Morocco (2011)</li>
      </ul>
    </section>

    <section>
      <h2>Languages</h2>
      <p>English (professional), French (fluent), Arabic (native)</p>
    </section>

    <section>
      <h2>Interests</h2>
      <p>Technology, music, chess, video games, tennis</p>
    </section>

    <footer>Last updated: {last_updated}</footer>
  </div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(html_path, arcname="Haroun_Resume.html")
    if os.path.exists(pdf_dst):
        z.write(pdf_dst, arcname="Haroun_Resume.pdf")

print("Generated:", html_path, pdf_dst, zip_path)
