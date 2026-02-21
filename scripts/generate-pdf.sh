#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# Allow skipping PDF generation (e.g., in Docker build stage where Python is unavailable)
if [[ "${SKIP_PDF:-}" == "1" ]]; then
  echo "SKIP_PDF=1 — skipping PDF generation"
  exit 0
fi

# Python controls filename and writes directly to static/
PDF_PATH=$(python resume/generate_resume_pdf.py --output-dir static)

echo "PDF generated: ${PDF_PATH}"
