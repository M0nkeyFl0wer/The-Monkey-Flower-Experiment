#!/bin/bash
# Capture all work from Seshat back to local machine
# Ensures no drafts or experiments are left orphaned on server
#
# Usage: bash scripts/capture_from_seshat.sh
# Run this at end of day to bring all Seshat work back to local

set -e

SESHAT_USER="m0nkey-fl0wer"
SESHAT_HOST="seshat.noosworx.com"
SESHAT_PORT="8888"
SESHAT_PROJECT="/home/${SESHAT_USER}/projects/campus-lan-storytelling"

LOCAL_ARCHIVE="./archive/seshat_captures"

echo "==========================================================================="
echo "Capturing Work from Seshat"
echo "==========================================================================="
echo ""

# Create archive directory
mkdir -p "${LOCAL_ARCHIVE}"

# Create timestamped capture
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
CAPTURE_DIR="${LOCAL_ARCHIVE}/capture_${TIMESTAMP}"
mkdir -p "${CAPTURE_DIR}"

echo "Step 1: Downloading all content drafts..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PROJECT}/content/drafts/ \
    "${CAPTURE_DIR}/drafts/"

echo "Step 2: Downloading approved posts..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PROJECT}/content/approved/ \
    "${CAPTURE_DIR}/approved/"

echo "Step 3: Downloading any published content..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PROJECT}/content/published/ \
    "${CAPTURE_DIR}/published/" 2>/dev/null || true

echo "Step 4: Downloading character state/memory..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PROJECT}/memory/ \
    "${CAPTURE_DIR}/memory/" 2>/dev/null || true

echo "Step 5: Capturing any logs or debug files..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    --include="*.log" --include="*.txt" --exclude="*" \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PROJECT}/ \
    "${CAPTURE_DIR}/" 2>/dev/null || true

# Create manifest
echo ""
echo "Step 6: Creating capture manifest..."
cat > "${CAPTURE_DIR}/MANIFEST.md" << EOF
# Seshat Capture - ${TIMESTAMP}

Captured from: ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PROJECT}

## Contents
$(du -sh "${CAPTURE_DIR}"/* | sed 's/^\t/- /' || echo "- See subdirectories below")

## Subdirectories
$(find "${CAPTURE_DIR}" -maxdepth 1 -type d ! -name . | while read dir; do
    echo "- $(basename "$dir"): $(find "$dir" -type f | wc -l) files"
done)

## Files Summary
- Drafts: $(find "${CAPTURE_DIR}/drafts" -type f 2>/dev/null | wc -l) files
- Approved: $(find "${CAPTURE_DIR}/approved" -type f 2>/dev/null | wc -l) files
- Published: $(find "${CAPTURE_DIR}/published" -type f 2>/dev/null | wc -l) files

## Timestamp
- Captured: $(date)
- Archive Path: ${LOCAL_ARCHIVE}/capture_${TIMESTAMP}

## Action Items
1. Review captured content in ./archive/seshat_captures/
2. Move any important drafts to ./content/drafts/
3. Archive this capture for historical reference
4. Check if any files need human review
EOF

echo "✓ Manifest created: ${CAPTURE_DIR}/MANIFEST.md"

# List what was captured
echo ""
echo "==========================================================================="
echo "✓ Capture Complete!"
echo "==========================================================================="
echo "Captured to: ${CAPTURE_DIR}/"
echo ""
echo "Contents:"
find "${CAPTURE_DIR}" -type f | head -20
if [ $(find "${CAPTURE_DIR}" -type f | wc -l) -gt 20 ]; then
    echo "... and $(( $(find "${CAPTURE_DIR}" -type f | wc -l) - 20 )) more files"
fi

echo ""
echo "Total captured: $(du -sh "${CAPTURE_DIR}" | cut -f1)"
echo ""
echo "Next steps:"
echo "1. Review: ls -R ${LOCAL_ARCHIVE}/capture_${TIMESTAMP}/"
echo "2. Extract important files: cp -r ${LOCAL_ARCHIVE}/capture_${TIMESTAMP}/drafts/* ./content/drafts/"
echo "3. Git commit: git add -A && git commit -m 'Capture from Seshat ${TIMESTAMP}'"
echo ""
