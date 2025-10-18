# Work Capture Protocol - Campus LAN Storytelling

**Goal:** Ensure no work is orphaned on Seshat or left in limbo between local and remote.

---

## The Problem We're Solving

When working on Seshat server:
- Generated posts might stay on server only
- Character agents might be tuned but changes not synced
- Experiments might be forgotten
- Archives might accumulate with no retrieval plan

**Solution:** Automated capture + explicit sync workflows

---

## Daily Workflow

### Before Working on Seshat
```bash
# 1. Capture any previous day's work
bash scripts/capture_from_seshat.sh

# 2. Sync latest local changes to server
bash scripts/sync_to_seshat.sh

# 3. SSH into Seshat
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com
cd /home/m0nkey-fl0wer/projects/campus-lan-storytelling
```

### After Working on Seshat (Daily Before Logout)
```bash
# 1. Capture all work back to local
exit  # Leave Seshat SSH session
bash scripts/capture_from_seshat.sh

# 2. Review what was captured
ls -la archive/seshat_captures/capture_*/

# 3. Move important work to appropriate folder
cp archive/seshat_captures/capture_*/drafts/*.json content/drafts/

# 4. Commit to git
git add content/drafts/ archive/seshat_captures/
git commit -m "Capture from Seshat work session"
```

---

## Script Reference

### `sync_to_seshat.sh`
**What it does:**
- Pushes local project to Seshat
- Syncs all drafts and approved content
- Creates timestamped backup on server
- Prevents work loss

**When to run:**
- Before starting work on Seshat
- After significant local changes
- Before extended Seshat work session

**Usage:**
```bash
bash scripts/sync_to_seshat.sh
```

### `capture_from_seshat.sh`
**What it does:**
- Downloads all Seshat content to local `archive/seshat_captures/`
- Timestamped folders: `capture_20251018_153000/`
- Creates manifest of what was captured
- Preserves full history

**When to run:**
- Daily at end of work session
- After experimental work on Seshat
- Before any major local changes
- Weekly as backup

**Usage:**
```bash
bash scripts/capture_from_seshat.sh
```

---

## Directory Structure for Captures

```
archive/
└── seshat_captures/
    ├── capture_20251018_150000/
    │   ├── MANIFEST.md              # What was captured
    │   ├── drafts/                  # Generated posts
    │   ├── approved/                # Reviewed posts
    │   ├── published/               # Published posts
    │   └── memory/                  # Character state
    ├── capture_20251018_180000/
    └── ... (daily captures)
```

Each capture is self-contained with manifest.

---

## File Categories

### Always Sync: Generated Content
```
content/drafts/*.json           # Generated posts
content/approved/*.json         # Approved posts
memory/character_state/         # Character memory
```

### Usually Sync: Code Changes
```
agents/**/*.py                  # Character agent code
utils/**/*.py                   # Utility scripts
scripts/**/*.py                 # Generation scripts
```

### Don't Sync: Virtual Environments
```
.venv/                          # Python virtualenv
venv/                           # Python virtualenv
__pycache__/                    # Compiled Python
*.pyc                           # Compiled Python
```

### Archive: Experimental Work
```
archive/seshat_captures/        # Captures from server
archive/experiments/            # Local experiments
```

---

## Protocols by Scenario

### Scenario 1: Quick Generation Run on Seshat

```bash
# 1. SSH into Seshat
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com

# 2. Sync latest code
cd /home/m0nkey-fl0wer/projects/campus-lan-storytelling
git pull origin main  # If using git

# 3. Generate posts
python scripts/phase0_setup.py

# 4. Check results
ls -la content/drafts/

# 5. Exit
exit

# 6. IMPORTANT: Capture work back to local
bash scripts/capture_from_seshat.sh

# 7. Review & commit
git add archive/seshat_captures/
git commit -m "Generation run - $(date +%Y%m%d)"
```

### Scenario 2: Character Voice Tuning Experiment

```bash
# 1. Work on Seshat (tune prompts, generate samples)
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com
cd /home/m0nkey-fl0wer/projects/campus-lan-storytelling

# 2. Edit agent prompts
nano agents/base/character_agent.py

# 3. Test generation with new prompts
python scripts/phase0_setup.py

# 4. Evaluate results
# (review content/drafts/)

# 5. Exit and capture
exit
bash scripts/capture_from_seshat.sh

# 6. If happy with results, sync back to Seshat
bash scripts/sync_to_seshat.sh

# 7. Commit refined code
git add agents/
git commit -m "Refine character agent prompts"
```

### Scenario 3: Multi-Day Seshat Development

**Day 1:**
```bash
# Start with fresh sync
bash scripts/sync_to_seshat.sh

# Work on Seshat
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com
# ... do work ...
exit

# Capture daily work
bash scripts/capture_from_seshat.sh
git add -A && git commit -m "Day 1 work"
```

**Day 2:**
```bash
# Capture any overnight work (probably none, but check)
bash scripts/capture_from_seshat.sh

# Sync latest local changes
bash scripts/sync_to_seshat.sh

# Resume work on Seshat
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com
# ... do work ...
exit

# Capture again
bash scripts/capture_from_seshat.sh
git add -A && git commit -m "Day 2 work"
```

---

## Archive Management

### Weekly Archive Review
```bash
# List all captures from this week
ls -la archive/seshat_captures/ | grep $(date +%Y%m%d_)

# Consolidate if too many captures
mkdir -p archive/weekly_backups/week_42_2025/
mv archive/seshat_captures/capture_2025101[0-7]_* archive/weekly_backups/week_42_2025/
```

### Monthly Archive Cleanup
```bash
# Identify large captures
du -sh archive/seshat_captures/capture_*/ | sort -h | tail -10

# Archive old captures (>2 weeks)
find archive/seshat_captures -type d -name "capture_*" -mtime +14 \
    -exec mv {} archive/old_captures/ \;
```

### Safe Deletion (Only After Review)
```bash
# Never delete without checking contents first
cat archive/seshat_captures/capture_20251001_*/MANIFEST.md

# Move to archive, never delete directly
mv archive/seshat_captures/capture_20251001_* archive/old_captures/
```

---

## Git Integration

### Commit Messages for Captures
```bash
# Include timestamp and summary
git add archive/seshat_captures/capture_20251018_150000/
git commit -m "Seshat capture: 8 posts generated from 4 characters"

# Or link to specific work
git commit -m "Capture Seshat experiments: Chris voice tuning"
```

### `.gitignore` Configuration
```
# Don't commit sensitive files
.env
ANTHROPIC_API_KEY
*.pyc
__pycache__/

# Do commit captures (they're important!)
# archive/seshat_captures/
```

---

## Automation Options (Future)

### Daily Automated Capture
```bash
# Add to crontab (run daily at 9 PM)
# 21 * * * * cd ~/The\ Monkey\ Flower\ Experiment/campus-lan-storytelling-main && bash scripts/capture_from_seshat.sh

# Or via systemd timer
cat > ~/.config/systemd/user/seshat-capture.timer << EOF
[Unit]
Description=Daily Seshat work capture

[Timer]
OnCalendar=daily
OnCalendar=21:00

[Install]
WantedBy=timers.target
EOF
```

### Automatic Sync on SSH Logout
```bash
# In ~/.bash_logout or ~/.zsh_logout
# if [ -n "$SESHAT_CONNECTION" ]; then
#     bash /path/to/scripts/capture_from_seshat.sh
# fi
```

---

## Troubleshooting

### Issue: "Connection refused" to Seshat
```bash
# Check if Seshat is reachable
ssh -p8888 -T m0nkey-fl0wer@seshat.noosworx.com echo "Connected"

# If fails, check your SSH key
ssh-add ~/.ssh/id_rsa  # or appropriate key file
```

### Issue: "Permission denied" during sync
```bash
# Seshat might not exist yet, create it
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com mkdir -p /home/m0nkey-fl0wer/projects
```

### Issue: Too many capture files, disk space?
```bash
# Check size of captures
du -sh archive/seshat_captures/

# Move old captures to external storage
rsync -av archive/seshat_captures/capture_202509*/ /mnt/external/backups/
```

### Issue: Modified files on both local and remote
```bash
# Check diff before syncing
rsync -avnz -e "ssh -p 8888" \
    m0nkey-fl0wer@seshat.noosworx.com:/home/m0nkey-fl0wer/projects/campus-lan-storytelling/content/drafts/ \
    content/drafts/ | head -20

# Then manually resolve conflicts
```

---

## Best Practices

### DO ✅
- Capture work daily (takes <1 minute)
- Use descriptive commit messages
- Archive captures weekly
- Review manifest.md before committing
- Test sync on small file sets first

### DON'T ❌
- Leave Seshat without capturing work
- Ignore sync conflicts
- Delete captures without reviewing
- Assume local and remote are in sync
- Work on same files locally and remotely simultaneously

---

## Verification Checklist

Before considering work "safe":

- [ ] Ran `capture_from_seshat.sh`
- [ ] Reviewed `archive/seshat_captures/capture_*/MANIFEST.md`
- [ ] Git staged new captures: `git add archive/seshat_captures/`
- [ ] Committed with message: `git commit -m "..."`
- [ ] Verified on GitHub: `git log --oneline | head`

---

## Reference

### Quick Commands
```bash
# Sync TO seshat
bash scripts/sync_to_seshat.sh

# Capture FROM seshat
bash scripts/capture_from_seshat.sh

# View captures
ls archive/seshat_captures/capture_*/MANIFEST.md

# Recent captures
ls -lart archive/seshat_captures/ | tail -5

# Check diff
rsync -avn scripts/sync_to_seshat.sh m0nkey-fl0wer@seshat.noosworx.com:
```

---

**Status:** Protocol Active
**Last Updated:** October 18, 2025
**Next Review:** After first Seshat work session
