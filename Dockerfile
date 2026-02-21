# ─── Stage 1: Generate resume PDF ────────────────────────────────────────────
FROM python:3.13-slim AS pdf

WORKDIR /app
COPY resume/ resume/
RUN pip install --no-cache-dir reportlab \
 && mkdir -p static \
 && python resume/generate_resume_pdf.py --output-dir static

# ─── Stage 2: Build SvelteKit app ───────────────────────────────────────────
FROM oven/bun:1 AS build

WORKDIR /app

# Install dependencies first (cache layer)
# --ignore-scripts avoids running "prepare" (svelte-kit sync) before source is present
COPY package.json bun.lock ./
RUN bun install --frozen-lockfile --ignore-scripts

# Copy source
COPY . .

# Bring in the generated PDF (overwrites any existing one from host)
COPY --from=pdf /app/static/*.pdf static/

# Sync SvelteKit generated types, then build
RUN bunx svelte-kit sync \
 && SKIP_PDF=1 bun run build

# ─── Stage 3: Runtime (adapter-node) ────────────────────────────────────────
FROM oven/bun:1-slim AS runtime

WORKDIR /app

# Copy the built output and runtime data files
COPY --from=build /app/build build/
COPY --from=build /app/package.json .
COPY --from=build /app/resume/resume-data.json resume/resume-data.json
COPY --from=build /app/static/ static/

# adapter-node listens on 0.0.0.0:3000 by default
ENV NODE_ENV=production
ENV PORT=3000
ENV HOST=0.0.0.0

EXPOSE 3000

CMD ["bun", "build/index.js"]
