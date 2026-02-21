#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# Generate the PDF; the Python script prints the versioned filename
PDF_NAME=$(python resume/generate_resume_pdf.py)

# Copy versioned PDF into static/ for SvelteKit
cp "${PDF_NAME}" "static/${PDF_NAME}"

echo "PDF generated: static/${PDF_NAME}"
