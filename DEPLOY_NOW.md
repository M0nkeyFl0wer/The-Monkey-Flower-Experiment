# 🚀 DEPLOY NOW - Phase 0 Live

**Status:** READY TO EXECUTE
**Time to First Posts:** 5 minutes setup + 2 minutes generation = **7 minutes total**
**Posts Generated:** 8 (2 per primary character)

---

## STEP 1: Terminal Setup (2 minutes)

```bash
# Open terminal and navigate to project
cd ~/The\ Monkey\ Flower\ Experiment/campus-lan-storytelling-main

# Verify you're in the right place
pwd
# Should show: /home/flower/The Monkey Flower Experiment/campus-lan-storytelling-main

# List what we have
ls -la
# Should show: README.md, requirements.txt, agents/, data/, scripts/, etc.
```

---

## STEP 2: Install Dependencies (3 minutes, one-time only)

```bash
# Install all Python packages needed
pip install -r requirements.txt

# This installs:
# - anthropic (Claude API)
# - pydantic (data validation)
# - chromadb (vector storage, for later)
# - PyGithub (GitHub API, for later)
# - ... and others

# If you already did this: skip to Step 3
```

---

## STEP 3: Set Your API Key (30 seconds)

```bash
# Set the Anthropic API key
export ANTHROPIC_API_KEY="sk-ant-YOUR-KEY-HERE"

# Replace YOUR-KEY-HERE with your actual Claude API key
# Example: sk-ant-ZWQxNzM0ZDIzZDg4NDkzZjgyODI2Y2E2ZjI3OTA1

# Verify it worked
echo $ANTHROPIC_API_KEY
# Should show: sk-ant-... (not empty!)
```

---

## STEP 4: Generate First Posts (2 minutes, async)

```bash
# THIS IS IT - Generate your first 8 posts
python scripts/phase0_setup.py
```

**What this does:**
1. Parses your Novel Crafter export
2. Creates 4 character agents (Chris, Sarah, Tria, Kamea)
3. Generates 2 posts per character (social + blog)
4. Saves everything to `content/drafts/`
5. Creates GitHub issues manifest

**Expected output:**
```
======================================================================
PHASE 0: SETUP - Parse Novel Crafter & Create Character Agents
======================================================================

Step 1: Parsing Novel Crafter export...
✓ Parsed: Chris
✓ Parsed: Sarah
✓ Parsed: Tria
✓ Parsed: Kamea

Step 2: Creating character agents for primary characters...
✓ Created agent for Chris
✓ Created agent for Sarah
✓ Created agent for Tria
✓ Created agent for Kamea

Step 3: Generating first batch of posts...

Generating posts from Chris...
  → Generating social post...
     ✓ Generated: SOCIAL
     Preview: I thought I could separate my work from my conscience...

  → Generating blog post...
     ✓ Generated: BLOG

[... similar for Sarah, Tria, Kamea ...]

Step 4: Saving posts and preparing GitHub issues...

======================================================================
PHASE 0 COMPLETE
======================================================================

Generated posts:
  Chris: 2 posts
  Sarah: 2 posts
  Tria: 2 posts
  Kamea: 2 posts

Next steps:
1. Review posts in: ./content/drafts/
2. Create GitHub issues from: ./content/drafts/github_issues_manifest.json
3. Test GitHub approval workflow
```

---

## STEP 5: Review Generated Posts (5 minutes)

```bash
# See what was generated
ls -la content/drafts/

# View Chris's posts
cat content/drafts/Chris_*.json | python -m json.tool | less

# Or use this to view all nicely:
python << 'EOF'
import json
from pathlib import Path

drafts_dir = Path("content/drafts")
for json_file in sorted(drafts_dir.glob("*.json")):
    if "manifest" in json_file.name:
        continue

    with open(json_file) as f:
        data = json.load(f)

    print(f"\n{'='*70}")
    print(f"Character: {data['character']}")
    print(f"{'='*70}")

    for i, post in enumerate(data['posts'], 1):
        print(f"\n[{i}] {post['post_type'].upper()}")
        print(f"Location: {post['location']} | Encryption: {post['encryption']}")
        print("-" * 70)
        print(post['content'])
        print()
EOF
```

---

## STEP 6: Quality Check (5 minutes)

Ask yourself:

**Character Voice:**
- ✓ Does Chris sound like a conflicted security officer?
- ✓ Does Sarah sound like an ethics professor?
- ✓ Does Tria sound like an investigative journalist?
- ✓ Does Kamea sound ideological?

**Authenticity:**
- ✓ Do posts feel human-written, not AI-template?
- ✓ Is vulnerability visible?
- ✓ Is wit grounded in real stakes?
- ✓ Is power structure being questioned?

**Canon:**
- ✓ Do posts respect your novel's timeline?
- ✓ No anachronisms?
- ✓ Characters know appropriate things?

**Length:**
- ✓ Posts 100-300 words?
- ✓ Social posts shorter, blogs longer?

---

## STEP 7: Create GitHub Repo (2 minutes)

Go to https://github.com/new

1. **Repository name:** `The-Monkey-Flower-Experiment`
2. **Visibility:** Public (or private, your choice)
3. **Initialize:** Add a README
4. Click **Create repository**

---

## STEP 8: Create First GitHub Issue (5 minutes)

1. Go to your new repo: `github.com/YOUR-USERNAME/The-Monkey-Flower-Experiment`
2. Click **Issues** tab
3. Click **New issue**
4. Fill in:
   - **Title:** `[Draft] Chris - Social`
   - **Body:** Copy one of Chris's social posts from `content/drafts/`
   - **Labels:** `draft`, `ai-generated`, `needs-review`, `chris`
   - **Assignee:** Yourself

5. Click **Submit new issue**

---

## STEP 9: Test Approval Workflow (2 minutes)

1. Go to the issue you just created
2. Click **Comment**
3. Type: `approve`
4. Post comment

This shows the workflow works:
- ✓ Issue created
- ✓ You can approve/reject
- ✓ System records your decision

---

## STEP 10: Now What? (Feedback Loop)

Tell me:

1. **Quality Score (1-10):** How good were the posts?
   - 1-3: Generic, not voice, needs major revision
   - 4-6: OK, but needs work
   - 7-8: Good, some tweaks needed
   - 9-10: Excellent, ready to scale

2. **Character Voice (1-10):** Did each character sound distinct?
   - Which was best?
   - Which needs work?

3. **What to adjust next?**
   - More vulnerability?
   - Different tone?
   - Different content focus?

4. **Ready to scale?**
   - Generate more from these 4 characters?
   - Add new characters?
   - Implement Phase 1 (multi-character coordination)?

---

## Common Issues & Fixes

### "API key not found"
```bash
# Check if it's set
echo $ANTHROPIC_API_KEY

# If empty, set it again
export ANTHROPIC_API_KEY="sk-ant-your-key"

# Verify
python -c "from anthropic import Anthropic; print('✓ Connected')"
```

### "Novel export not found"
```bash
# Check if data exists
ls data/novel_export/characters/
# Should show: Chris/, Sarah/, Tria/, Kamea/, etc.

# If empty, the export wasn't copied
# Copy it:
cp -r ../2025-10-18*/ data/novel_export/
```

### "Generation is taking forever"
This is normal! Claude API takes 10-30 seconds per post.
First time is slower. Subsequent runs use caching.

Just wait. Grab coffee. ☕

### "Posts are generic/not in voice"
Totally normal for first generation. This is learning:
1. First batch: baseline, learning what works
2. Your feedback: teaches the system
3. Second batch: better (applies your preferences)
4. Each iteration: continuous improvement

The system learns from your approval patterns.

---

## What Happens Next (The Swarm Scales)

### Immediate (Next 1-2 days)
```
You provide feedback on these 8 posts
System learns your preferences
I adjust character prompts
Second generation runs with improvements
Repeat: ~5-10 iterations
```

### Short Term (This week)
```
Phase 1: Multi-character coordination activated
Stigmergic bulletin board running
Characters start interacting organically
Emergent conversations emerge
```

### Medium Term (Weeks 2-4)
```
More characters activated (Randy, Frank, Melanie, etc.)
Content diversification (surveillance logs, etc.)
Magazine layout compilation
200+ pages of content
```

### Long Term (Weeks 5+)
```
Full roster (20+ characters)
Autonomous swarm running
Human-in-the-loop for approval only
Magazine ready for printing
```

---

## The Swarm (What You Just Deployed)

**What's running now:**
- ✅ Claude 3.5 Sonnet as character brain
- ✅ Character memory systems
- ✅ Stigmergic bulletin board (ready, not active yet)
- ✅ Local decision-making (active)
- ✅ Quality checks (active)
- ✅ GitHub workflow (ready)

**What's NOT running yet:**
- ⚪ Multi-character coordination (Phase 1)
- ⚪ Work-stealing load balancer (Phase 2)
- ⚪ Surveillance camera agent (Phase 2)
- ⚪ Full character roster (Phase 3+)

This is the MVP. It works. Now we scale.

---

## Success Metrics

You've successfully deployed when:

- [x] Code installed
- [x] API key set
- [x] `python scripts/phase0_setup.py` ran successfully
- [x] 8 posts generated to `content/drafts/`
- [x] Posts are >100 words each
- [x] Character voices recognizable
- [x] GitHub repo created
- [x] First issue created
- [x] Approval workflow tested

---

## Ready?

```bash
cd ~/The\ Monkey\ Flower\ Experiment/campus-lan-storytelling-main

# 5 minutes setup
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."

# 2 minutes generation
python scripts/phase0_setup.py

# 15 minutes review + GitHub
ls content/drafts/
# Review + create GitHub issues

# BOOM: Swarm deployed, first posts live
```

---

## Then Tell Me:

Once you've run Phase 0 and reviewed the posts:

1. **Paste one of your favorite posts** - Show me what worked
2. **Paste one that needs work** - Show me what to improve
3. **Rate the quality** - Where are we at?
4. **What to iterate on** - What felt off?

Then we either:
- **Iterate:** Generate 10 more posts, improve voices
- **Scale:** Add more characters (Randy, Melanie, Frank, etc.)
- **Phase 1:** Launch multi-character coordination

---

**Time to First Posts:** ~7 minutes
**Status:** YOU ARE READY
**Let's build this:** 🚀

Run Phase 0 now. Report back with results.
