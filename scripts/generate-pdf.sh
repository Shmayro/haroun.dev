#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# Python controls filename and writes directly to static/
PDF_PATH=$(python resume/generate_resume_pdf.py --output-dir static)

echo "PDF generated: ${PDF_PATH}"
