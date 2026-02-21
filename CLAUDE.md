# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Maintaining This File

**Keep this file up to date.** After any change that affects the information below, update it in the same session:

- Edit in place — replace outdated info, don't append.
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
- **SvelteKit site** — main project at repo root, deployed to haroun.dev. Currently a resume page, will grow with new features.
- **Resume data & PDF generation** — `resume/` subfolder. Python/ReportLab produces the PDF during Docker build.

## Repository Structure

```
src/                        # SvelteKit app (Svelte 5 + TypeScript)
  routes/+page.svelte       # Resume page
  routes/+page.server.ts    # Loads resume-data.json + discovers PDF filename
  lib/types.ts              # TypeScript interfaces for resume data
static/                     # Static assets (generated PDFs land here, gitignored)
resume/
  resume-data.json          # Single source of truth for all resume content
  generate_resume_pdf.py    # Reads resume-data.json → PDF via ReportLab
  legacy/                   # Old HTML generator kept for reference
scripts/
  generate-pdf.sh           # Runs PDF generator, supports SKIP_PDF=1
svelte.config.js            # adapter-node
package.json                # bun
Dockerfile                  # Multi-stage: python→bun build→bun runtime
```

## Development

```bash
bun install                 # Install dependencies
bun run dev                 # Dev server (localhost:5173)
bun run build               # Build (auto-generates PDF via prebuild hook)
bun run generate:pdf        # Generate PDF only
docker build -t haroun-dev . && docker run -p 3000:3000 haroun-dev  # Docker
```

## Architecture Notes

- **resume-data.json** is the single source of truth — consumed by both the PDF script and SvelteKit page. No content duplication.
- **PDF generation**: `resume/generate_resume_pdf.py --output-dir static` produces date-versioned PDFs (`Haroun_EL_ALAMI_CV-DDMMYYYY.pdf`). The server load function scans `static/` for the latest one.
- **Docker build**: 3-stage (Python PDF gen → bun build → bun runtime on port 3000). The `prebuild` hook is skipped in Docker via `SKIP_PDF=1` since the PDF is already generated in stage 1.
- **SvelteKit adapter**: `adapter-node` for Docker/self-hosted deployment.
- **bun** is the package manager and runtime.
