# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Maintaining This File

**Keep this file up to date.** After any change that affects the information below, update it in the same session:

- Edit in place — replace outdated info, don't append. Remove "current state" notes once migrations are done.
- Never remove: project purpose, maintenance instructions, or skill creation guidelines.

## Creating Project Skills

Create project-specific skills in `.claude/skills/<skill-name>/SKILL.md` when:
- A multi-step workflow will recur (e.g., updating resume data, adding a portfolio section)
- Project-specific knowledge would be lost between sessions

Don't create skills for one-off tasks or simple operations. Use verb-first kebab-case naming. After creating a skill, commit it and update this file if relevant.

Skill frontmatter format:
```yaml
---
name: skill-name
description: Use when [triggering conditions]
---
```

## Project Purpose

Monorepo for **Haroun EL ALAMI**'s portfolio at [haroun.dev](https://github.com/Shmayro/haroun.dev). Contains:
- **SvelteKit site** — main project, deployed to haroun.dev. Starts minimal (resume page), grows with new features.
- **Resume data & PDF generation** — `resume/` subfolder. Python/ReportLab produces the PDF during Docker build.

## Repository Structure (Target)

```
src/                        # SvelteKit app
static/                     # Static assets (generated PDF lands here)
resume/
  resume-data.json          # Single source of truth for resume content
  generate_resume_pdf.py    # Reads resume-data.json → PDF
svelte.config.js
package.json
Dockerfile
```

- **bun** — package manager and runtime
- **Docker** — full build pipeline, including PDF generation as a build step
- **resume-data.json** — consumed by both the PDF script and SvelteKit, no duplication

### Current State (remove once migration is complete)

Only resume generation scripts exist at the root. `generate_resume_pdf.py` will be refactored to read from `resume-data.json` and moved to `resume/`. `generate_resume_html_and_zip.py` is legacy — safe to remove.
