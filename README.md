# The Monkey Flower Experiment - Campus LAN Storytelling System

**Status:** Phase 0 - Setup & First Generation

An AI-powered distributed storytelling system where Claude-based character agents generate magazine-quality social posts, blogs, and editorials that tell the complete narrative of Ben West's novel "Mandate: The Monkey Flower Experiment."

## Quick Start

### Prerequisites
- Python 3.12+
- Anthropic Claude API key (max plan)
- Seshat server access (RTX 4090 + Ollama for experimentation)
- GitHub account for approval workflow

### Installation

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up environment
export ANTHROPIC_API_KEY="your-api-key-here"

# 3. Run Phase 0 setup
python scripts/phase0_setup.py
```

## Project Structure

```
campus-lan-storytelling-main/
├── data/
│   ├── novel_export/              # Novel Crafter export (source of truth)
│   ├── character_codex.json       # Parsed character profiles
│   └── story_timeline.json        # Event chronology
├── agents/
│   ├── base/
│   │   └── character_agent.py     # Claude-based character agent
│   ├── character_agents/          # Individual character implementations
│   └── __init__.py
├── content/
│   ├── drafts/                    # Generated posts awaiting review
│   ├── approved/                  # Approved posts (ready to publish)
│   ├── published/                 # Published to Bluesky/Lens
│   └── rejected/                  # Failed/edited posts + feedback
├── github_integration/            # GitHub API handlers
├── scripts/
│   ├── phase0_setup.py           # Parse Novel Crafter & generate first posts
│   ├── generate_daily.py         # Main generation loop (Phase 1+)
│   └── github_publisher.py       # Create issues & publish
├── utils/
│   └── novel_crafter_parser.py   # Parse Novel Crafter export
└── docs/
    ├── CHARACTER_GUIDE.md         # Character voice & constraints
    ├── WORKFLOW.md                # Daily generation workflow
    └── API_INTEGRATION.md         # GitHub + social media APIs
```

## Phase Overview

### Phase 0: Setup (Current)
- [x] Parse Novel Crafter export into character codex
- [x] Create character agents for primary characters
- [x] Generate first batch of test posts
- [ ] Prepare GitHub issue templates
- [ ] User review & approval workflow test

**Status:** Ready to run `python scripts/phase0_setup.py`

### Phase 1: Multi-Character Coordination
- [ ] Scale to 5-7 primary characters
- [ ] Implement stigmergic bulletin board for coordination
- [ ] Enable emergent cross-character interactions
- [ ] Build daily generation loop with approval workflow

### Phase 2: Content Diversification
- [ ] Add surveillance footage descriptions (camera agent)
- [ ] Implement multiple post types (social, blog, editorial, DM, surveillance)
- [ ] Magazine layout compilation
- [ ] Weekly HTML export

### Phase 3: Publication Pipeline
- [ ] GitHub issue creation + approval workflow
- [ ] Manual copy to Bluesky/Lens (for quality control)
- [ ] Archive management
- [ ] PDF export for printing

### Phase 4: Refinement & Scaling
- [ ] Voice tuning based on human feedback
- [ ] Feedback loops for character consistency improvement
- [ ] Full character roster integration
- [ ] Long-form magazine compilation

## Character Overview

### Primary Characters (Priority)

**Chris** (22, Student)
- Arc: Moral awakening, security defection
- Voice: Torn between duty and conscience, growth-oriented
- Aesthetic: Balanced cyberpunk/solarpunk

**Sarah** (45, Faculty)
- Arc: Moral clarity provider, ethical mediator
- Voice: Thoughtful, reflective, unifying
- Aesthetic: Solarpunk-leaning

**Tria** (Organizer)
- Arc: Exposé writer, community coordinator
- Voice: Investigative, opinion-driven, action-oriented
- Aesthetic: Cypherpunk-leaning (encryption, transparency)

**Kamea** (Ideological)
- Arc: Resistance figure, philosophical opposition
- Voice: Essays on ideology and resistance, principled
- Aesthetic: Cypherpunk-primary

### Voice Style Guidelines

All characters speak through Ben West's lens:
- **Wit + Personality:** Sharp observations, humor grounded in real stakes
- **Vulnerability:** Show real fear, doubt, growth
- **Power Critique:** Question authority, expose systems
- **Solution-Oriented:** Pair critique with alternatives
- **Complexity:** Three-dimensional characters, not archetypes

### Aesthetic Balance

- **Cypherpunk (60%):** Surveillance, encryption, power resistance, neon-noir atmosphere
- **Solarpunk (40%):** Community action, sustainability, hope-in-reality, nature-tech

**Vocabulary:**
- Cypherpunk: netrunner, ICE, cyberspace, chrome, black markets, encrypted, data haven
- Solarpunk: mesh networks, permaculture, cooperative, sustainable, bioregion

## Workflow

### Daily Generation Loop

```
1. Check bulletin board (stigmergic traces)
2. Identify narrative opportunities from timeline
3. Generate posts from assigned characters
4. Create GitHub issues with drafts
5. You review + approve/edit/reject
6. Approved posts → archive
7. You copy to Bluesky/Lens manually
8. Feedback incorporated into next generation
```

### Approval Workflow

```
GitHub Issue Created
  ↓
@flower tagged for review
  ↓
You comment: "approve", "revise", or provide edits
  ↓
System processes feedback
  ↓
Post moves to approved/ or rejected/
  ↓
You publish to Bluesky/Lens when ready
  ↓
Archive timestamped
```

## Story Timeline & Context

**Current Story Date:** June 3, 2025

**Major Event:** Storm + Refugee Crisis
- Literal storm approaching campus
- Institutional conflict over refugee protection
- Board chosen bureaucracy over action
- Community organizing in shadows
- People choosing sides, power shifting

**Key Conflicts:**
- Safety vs. Solidarity
- Surveillance for protection vs. surveillance for control
- Community vs. Administration
- Idealism vs. pragmatism

**Character Stakes:**
- Chris: Can he defect without destroying relationships?
- Sarah: How do ethics guide action?
- Tria: Can investigation expose truth?
- Kamea: Will ideology translate to real change?

## LLM Backend Configuration

### Claude API (Recommended)
```
Model: claude-3-5-sonnet-20241022
Cost: ~$0.02 per post
Quality: Excellent character consistency
Uses: Primary generation
```

### Local Ollama (Experimentation)
```
Available on Seshat:
- qwen2.5:14b (9GB)
- codellama:7b (3.8GB)
- deepseek-r1:latest (5.2GB)

Use for: Character variety testing, brainstorming
Quality: Adequate for exploration, lower than Claude
```

### Hybrid Approach
1. Brainstorm with Ollama (fast, free)
2. Polish with Claude (high quality)
3. Use Ollama for emergent dialogue, Claude for final posts

## GitHub Integration

### Issue Creation
```
POST /repos/{owner}/The-Monkey-Flower-Experiment/issues
Title: [Draft] {Character} - {PostType}
Labels: draft, ai-generated, needs-review, {character_name}
Assignees: @flower
```

### Issue Template Structure
```yaml
---
type: draft_post
character: Chris
timestamp: 2025-06-03 15:30
location: campus.lan/boards/general
encryption: public
post_type: social
---

[Post content here]

---
[Editor scores if using]
```

## Storage & Deployment

### Local Development
```
~/The Monkey Flower Experiment/campus-lan-storytelling-main/
```

### Remote - Seshat Server
```
Available for deployment with RTX 4090
Ollama models available, Claude API capable
(Connection details in private notes)
```

### Archives
- SanDisk (local Pi): Long-term storage, backup
- GitHub: Version control, approval workflow
- Publication: Bluesky + Lens Protocol

## Command Reference

### Generate Posts
```bash
python scripts/phase0_setup.py              # Initial setup & generation
python scripts/generate_daily.py            # Main generation loop (Phase 1+)
```

### GitHub Workflow
```bash
python scripts/github_publisher.py --create-issues    # Create draft issues
python scripts/github_publisher.py --process-approvals # Process feedback
```

### Management
```bash
python utils/novel_crafter_parser.py        # Re-parse novel export
python scripts/archive_approved_posts.py    # Weekly archive
python scripts/compile_magazine.py          # Compile to HTML/PDF
```

## Quality Standards

**Character Consistency:** 2.8/3.0 minimum
- Score = Alignment to canonical voice
- Tracking: Cosine similarity to approved samples

**Canon Compliance:** 100%
- Zero contradictions with novel
- Character knowledge appropriately scoped
- Timeline events respected

**Authenticity:** Human-readable, not AI-template
- Vulnerability evident
- Personality shines through
- Wit grounded in real stakes

**Length:** 50-300 words per post
- Social: 50-150 words
- Blog: 200-400 words
- Editorial: 300-500 words
- Surveillance: 100-250 words

## Feedback Loop

### Every Approved Post
```
✓ Approved → Added to character semantic memory
→ Analyzed for voice consistency patterns
→ Informs next post quality score threshold
→ Examples added to training context
```

### Weekly Feedback Analysis
```
Review approval rate → Adjust generation thresholds
Identify voice drift → Retrain prompt specifics
Catalog emergent interactions → Add to story timeline
```

## Next Immediate Steps

1. **Run Phase 0:** `python scripts/phase0_setup.py`
2. **Review generated posts** in `./content/drafts/`
3. **Test GitHub issue creation** (manual or scripted)
4. **Approve 1-2 posts** to establish feedback loop
5. **Test Bluesky/Lens posting** (manual copy for now)
6. **Iterate on character voices** based on your preferences
7. **Proceed to Phase 1** once satisfied with quality

## Contact & Credits

**Developer:** Claude Code (Anthropic)
**Author & Director:** Ben West (@flower)
**Novel:** Mandate: The Monkey Flower Experiment (~decade-long project)

---

**Last Updated:** October 18, 2025
**Version:** 0.1.0 (Phase 0 - Setup)
