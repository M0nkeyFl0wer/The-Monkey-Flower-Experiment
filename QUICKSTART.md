# Quick Start Guide - The Monkey Flower Experiment

## First Time Setup (5 minutes)

### 1. Install Python Dependencies
```bash
cd /home/flower/The\ Monkey\ Flower\ Experiment/campus-lan-storytelling-main
pip install -r requirements.txt
```

### 2. Set API Keys
```bash
# Set your Anthropic Claude API key
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Optional: Set GitHub token for API calls (later phases)
export GITHUB_TOKEN="github_pat_your_token_here"
```

### 3. Verify Setup
```bash
python -c "from anthropic import Anthropic; print('✓ Anthropic API working')"
```

## Run Phase 0: Generate First Posts (2 minutes)

```bash
# Generate first batch of posts from Chris, Sarah, Tria, Kamea
python scripts/phase0_setup.py

# This will:
# 1. Parse the Novel Crafter export
# 2. Create character agents
# 3. Generate 2 posts per character (social + blog)
# 4. Save to ./content/drafts/
# 5. Create GitHub issues manifest
```

## Expected Output

You'll see:

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
       Location: general | Encryption: public
       Preview: I thought I could separate my work from my conscience...
  → Generating blog post...
     ✓ Generated: BLOG

[Posts for each character...]

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
4. Proceed to Phase 1: Multi-character coordination
```

## Review Generated Posts

```bash
# View Chris's posts
cat ./content/drafts/Chris_*.json | python -m json.tool | less

# Or view all posts nicely formatted
python << 'EOF'
import json
from pathlib import Path

drafts_dir = Path("./content/drafts")
for json_file in sorted(drafts_dir.glob("*.json")):
    if "manifest" in json_file.name:
        continue

    with open(json_file) as f:
        data = json.load(f)

    print(f"\n{'='*70}")
    print(f"Character: {data['character']}")
    print(f"{'='*70}")

    for i, post in enumerate(data['posts'], 1):
        print(f"\n[{i}] {post['post_type'].upper()} - {post['location']}")
        print(f"Encryption: {post['encryption']}")
        print("-" * 70)
        print(post['content'][:300] + "..." if len(post['content']) > 300 else post['content'])
        print()
EOF
```

## Next Steps (After Review)

### Option A: Create GitHub Issues (Recommended)
```bash
# Use the manifest to create GitHub issues
python scripts/github_publisher.py --create-issues \
    --manifest ./content/drafts/github_issues_manifest.json \
    --repo The-Monkey-Flower-Experiment
```

### Option B: Manual Test on GitHub
1. Go to: https://github.com/your-username/The-Monkey-Flower-Experiment
2. New Issue
3. Copy/paste post content from ./content/drafts/
4. Label: `draft`, `ai-generated`, `needs-review`, character name
5. Assign: @flower (yourself)

### Option C: Edit Posts First
If any posts need editing:
```bash
# Edit the JSON file
nano ./content/drafts/Chris_2025-10-18.json

# Then create issues from edited version
```

## Approval Workflow Test

### 1. Create One Draft Issue
Create one GitHub issue manually with a post you like.

### 2. Test Approval
Comment on the issue: `approve`

### 3. Run Feedback Processor
```bash
python scripts/github_publisher.py --process-approvals \
    --repo The-Monkey-Flower-Experiment
```

This moves the post to `./content/approved/`

## Common Commands

```bash
# Generate posts
python scripts/phase0_setup.py

# View all drafts
ls -lah ./content/drafts/

# Count generated posts
find ./content/drafts -name "*.json" -exec grep -h "total_posts" {} \; | \
    awk -F: '{sum+=$2} END {print "Total posts generated: " sum}'

# Export approved posts
python scripts/archive_approved_posts.py

# Create GitHub issues from manifest
python scripts/github_publisher.py --create-issues \
    --manifest ./content/drafts/github_issues_manifest.json
```

## Troubleshooting

### Issue: "API key not found"
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key"
echo $ANTHROPIC_API_KEY  # Verify it's set
```

### Issue: "Novel Crafter export not found"
Make sure you copied the export:
```bash
ls -la ./data/novel_export/
# Should show: characters/, chats/, other/, etc.
```

### Issue: "Posts are generic/not in character"
This is normal for first generation! The character agents are learning.
- Edit posts and note what makes them better
- This feedback trains the next generation
- Each approved post improves the model context

### Issue: "Generation is slow"
Claude API calls take 10-30 seconds per post. This is normal.
For faster iteration, try Ollama:
```bash
# SSH into Seshat
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com
ollama run qwen2.5:14b
```

Then edit `CharacterAgent` to use local Ollama for quick tests.

## Debug Mode

For detailed logging:
```bash
# Run with debug output
PYTHONUNBUFFERED=1 python scripts/phase0_setup.py 2>&1 | tee setup_log.txt
```

This saves output to `setup_log.txt` for inspection.

## Integration with VSCode

If you want to use Claude Code for refinement:

```bash
# Make scripts executable
chmod +x scripts/*.py

# Open in editor
code .

# Run from VSCode terminal
python scripts/phase0_setup.py
```

## What Happens Next?

Once Phase 0 is working:

1. **Phase 1:** Build coordination between characters
2. **Phase 2:** Add surveillance footage descriptions
3. **Phase 3:** Set up publication workflow
4. **Phase 4:** Scale to full character roster

Each phase builds on the previous. No rush—quality over speed!

---

**Status:** Ready to run `python scripts/phase0_setup.py`

**Time to first posts:** ~2 minutes (after dependencies installed)

**Next review:** After seeing first batch, we iterate on voice + quality
