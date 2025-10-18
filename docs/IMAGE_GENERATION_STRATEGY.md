# Image Generation Strategy

## Overview

Each character post can include image descriptions. When posts are approved, we need a strategy for converting those descriptions into actual images for the 200-page magazine layout.

## Current Image Descriptions

From Phase 0 posts, image descriptions are embedded as:
```
[image: View from admin building northwest window, 22:20—south field visible in distance, scattered lights from phones and small fires]
```

Extracted to JSON metadata for each post containing images.

## Image Generation Options

### Option 1: Claude + DALL-E (Recommended for Development)

**Pros:**
- ✅ Integrated with Claude Code workflow
- ✅ Can use Claude to iterate/refine prompts
- ✅ Consistent with existing architecture
- ✅ Cost-effective for testing
- ✅ Good for cyberpunk/solarpunk aesthetic

**Cons:**
- DALL-E has limitations on complex scenes
- May need prompt engineering per image

**Integration:**
```python
# In character_agent.py or new image_generator.py

from openai import OpenAI

client = OpenAI()

for image_desc in post['images']:
    # Use Claude to enhance prompt
    prompt = enhance_image_prompt(image_desc['description'])

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="hd"
    )

    image_url = response.data[0].url
    # Download and save
```

**Cost:** ~$0.08 per image (HD quality)

### Option 2: Midjourney (Best Quality, But Manual)

**Pros:**
- ✅ Highest visual quality
- ✅ Best for cyberpunk/solarpunk aesthetics
- ✅ Excellent at understanding complex scenes
- ✅ Can handle multiple variations easily
- ✅ Community-driven improvements

**Cons:**
- ❌ Manual submission required (no API)
- ❌ More expensive per image
- ❌ Not automatable in current workflow
- ❌ Would require manual copy-paste process

**Integration Strategy:**
1. Export image descriptions to a Midjourney-ready format
2. User submits to Midjourney Discord manually
3. Save generated images to repo
4. Link images in final markdown

**Cost:** ~$0.10-0.15 per image (subscription-based)

### Option 3: Hybrid Approach (Recommended for Production)

**Strategy:**
1. **Use Claude for quick iteration** during post development
   - Fast feedback on composition, framing, mood
   - Cyberpunk/solarpunk aesthetic testing

2. **Use Midjourney for final publication**
   - High-quality renders for the 200-page magazine
   - User handles batch Midjourney submissions
   - Images stored in repo at publication

**Workflow:**
```
Post Approved (GitHub Issue)
    ↓
Extract image descriptions
    ↓
Generate draft images (Claude/DALL-E)
    ↓
Review drafts with user
    ↓
User submits to Midjourney
    ↓
High-quality images saved to repo
    ↓
Magazine layout uses final images
```

## Recommendation: Hybrid (Claude for drafts, Midjourney for final)

**Why this approach:**

1. **Development Speed**: Claude/DALL-E allows fast iteration on image concepts
2. **Quality Control**: You get to see drafts before expensive Midjourney generation
3. **Cost Efficient**: Don't waste money on Midjourney if concepts don't work
4. **Flexibility**: Can pivot image styles without committed costs
5. **Magazine Ready**: Final Midjourney images are publication-quality

## Implementation Steps

### Phase 1: Draft Generation (Claude/DALL-E)
1. Extract image descriptions from approved posts
2. Enhance descriptions using Claude's understanding of story context
3. Generate 1-2 draft images per description using DALL-E
4. Store drafts in `content/images/drafts/`
5. Link drafts back to GitHub issues for user review

### Phase 2: User Review & Refinement
User can:
- Comment on drafts in GitHub issues
- Request style changes, reframing, composition adjustments
- Approve for Midjourney or iterate again

### Phase 3: Final Generation (Midjourney)
Once user approves draft direction:
1. Export approved prompt + aesthetic notes
2. Format for Midjourney batch submission
3. User submits to Midjourney Discord
4. High-res images saved to `content/images/final/`
5. Magazine layout compilation

## Image Organization

```
content/images/
├── drafts/
│   ├── chris_social_001_draft.png
│   ├── chris_blog_001_draft.png
│   └── ...
├── final/
│   ├── chris_social_001_final.png
│   ├── chris_blog_001_final.png
│   └── ...
└── prompts/
    ├── chris_social_001_prompt.md
    └── ...
```

## Metadata Structure

Each image will have associated metadata:
```json
{
  "image_id": "chris_social_001",
  "post_id": "issue_2",
  "character": "Chris",
  "post_type": "social",
  "original_description": "View from admin building...",
  "enhanced_prompt": "Security camera footage style, overhead angle...",
  "draft_image_url": "content/images/drafts/chris_social_001_draft.png",
  "final_image_url": "content/images/final/chris_social_001_final.png",
  "style_notes": "Cyberpunk noir, surveillance aesthetic",
  "approval_status": "approved_for_midjourney"
}
```

## Next Steps

1. **Immediate**: You review & approve the 8 text posts in GitHub
2. **After text approval**: Extract image descriptions
3. **Option A**: Generate Claude/DALL-E drafts for your review
4. **Option B**: Export Midjourney prompts if you want to go straight to final
5. **Final**: Magazine layout compilation with images

## Questions for User

1. **Workflow preference**:
   - Hybrid (drafts → final)
   - Direct to Midjourney
   - Claude only for testing?

2. **Visual style**:
   - 60% cyberpunk, 40% solarpunk - how specific should we be?
   - Examples of image styles you want?

3. **Volume**:
   - Expected number of images per post?
   - All posts get images or selective?

---

**Current Status**: Strategy defined, awaiting post approval and user preference on image generation pipeline.
