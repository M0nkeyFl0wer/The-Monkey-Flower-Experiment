#!/bin/bash
# Sync Campus LAN Storytelling project to Seshat server
# Prevents orphaned files and ensures all drafts are captured
#
# Usage: bash scripts/sync_to_seshat.sh
# Run this daily or before ending a work session

set -e  # Exit on error

SESHAT_USER="m0nkey-fl0wer"
SESHAT_HOST="seshat.noosworx.com"
SESHAT_PORT="8888"
SESHAT_PATH="/home/${SESHAT_USER}/projects/campus-lan-storytelling"

LOCAL_PROJECT="."

echo "==========================================================================="
echo "Syncing Campus LAN Storytelling to Seshat"
echo "==========================================================================="
echo ""

# Create destination directory on Seshat if it doesn't exist
echo "Step 1: Ensuring Seshat directory exists..."
ssh -p${SESHAT_PORT} ${SESHAT_USER}@${SESHAT_HOST} "mkdir -p ${SESHAT_PATH}"

# Sync all project files to Seshat
echo "Step 2: Syncing project files..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    --exclude='.git' \
    --exclude='__pycache__' \
    --exclude='.pytest_cache' \
    --exclude='*.pyc' \
    --exclude='.venv' \
    --exclude='venv' \
    ${LOCAL_PROJECT} \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PATH}/

echo "Step 3: Syncing content drafts specifically..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    content/drafts/ \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PATH}/content/drafts/

echo "Step 4: Syncing approved posts..."
rsync -avz -e "ssh -p ${SESHAT_PORT}" \
    content/approved/ \
    ${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PATH}/content/approved/

# Create timestamped backup
echo "Step 5: Creating timestamped backup on Seshat..."
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ssh -p${SESHAT_PORT} ${SESHAT_USER}@${SESHAT_HOST} \
    "cp -r ${SESHAT_PATH} ${SESHAT_PATH}_backup_${TIMESTAMP}"

# List what's on Seshat
echo ""
echo "Step 6: Verification - Files on Seshat:"
ssh -p${SESHAT_PORT} ${SESHAT_USER}@${SESHAT_HOST} \
    "du -sh ${SESHAT_PATH}/* 2>/dev/null | tail -20"

echo ""
echo "==========================================================================="
echo "✓ Sync Complete!"
echo "==========================================================================="
echo "Remote path: ssh://${SESHAT_USER}@${SESHAT_HOST}:${SESHAT_PORT}${SESHAT_PATH}"
echo "Backup:     ${SESHAT_PATH}_backup_${TIMESTAMP}"
echo ""
