#!/usr/bin/env python3
"""
Phase 0: Parse Novel Crafter data and create character agents.

This script:
1. Parses Novel Crafter export into character codex
2. Creates character agent instances
3. Generates first batch of posts for review
4. Prepares GitHub issues for approval
"""

import sys
import json
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.novel_crafter_parser import NovelCrafterParser
from agents.base.character_agent import CharacterAgent


def main():
    print("\n" + "="*70)
    print("PHASE 0: SETUP - Parse Novel Crafter & Create Character Agents")
    print("="*70 + "\n")

    # Step 1: Parse Novel Crafter export
    print("Step 1: Parsing Novel Crafter export...")
    parser = NovelCrafterParser("./data/novel_export")
    parser.parse_all()
    parser.print_summary()

    # Save character codex
    codex = parser.save_codex("./data/character_codex.json")

    # Step 2: Create character agents for primary characters
    print("\n" + "="*70)
    print("Step 2: Creating character agents for primary characters...")
    print("="*70 + "\n")

    # Load codex
    with open("./data/character_codex.json") as f:
        codex_data = json.load(f)

    characters = codex_data['characters']

    # Priority characters
    priority_characters = [
        "Chris",     # Moral conflict, defection arc
        "Sarah",     # Ethics mediator
        "Tria",      # Investigative journalist/organizer
        "Kamea",     # Ideological resistance
    ]

    agents = {}
    for char_name in priority_characters:
        if char_name in characters:
            char_data = characters[char_name]
            agent = CharacterAgent(char_name, char_data)
            agents[char_name] = agent
            print(f"✓ Created agent for {char_name}")
        else:
            print(f"✗ Character '{char_name}' not found in codex")

    print(f"\nTotal agents created: {len(agents)}")

    # Step 3: Generate first posts
    print("\n" + "="*70)
    print("Step 3: Generating first batch of posts...")
    print("="*70 + "\n")

    # Define key story scenes - each character will provide their perspective
    # on the SAME scenes from different angles
    scenes = [
        {
            "title": "Emergency Board Meeting",
            "time": "June 3, 2025, 1:17 PM",
            "description": """
SCENE: Emergency Board Meeting - Resistance Against Bureaucracy

Kamea interrupts the mundane board meeting demanding immediate action for refugee support.
The board discusses "proper channels" and "institutional liability" while families
sleep in the rain outside. Robert (treasurer) argues resources vs. morality.
Kamea's rebuttal: "Humanity and sustainability go hand-in-hand. This isn't statistics—it's our neighbors."

A committee is formed. Decisive action is deferred.

You were there. What did you witness? What was your role? What do you think happened?
What will you tell people on the network?
""",
            "character_directions": {
                "Chris": "You were assigned to security during the meeting. You heard everything. How does this conflict with your sense of duty?",
                "Sarah": "You sat in that meeting trying to find the ethical middle ground. What questions do you have? What's your analysis?",
                "Tria": "You're there as journalist/organizer. You caught the key moment. Report what happened.",
                "Kamea": "You spoke truth to power. How did that feel? What comes next?",
            }
        },
        {
            "title": "Rescue in the Woods",
            "time": "June 3, 2025, 3:00 PM",
            "description": """
SCENE: Quiet Help in the Woods - Direct Action

While Kamea faces security/board resistance, Randy leads volunteers bringing stranded
families through the woods to safety. Heavy rain. Equipment failing. But they move anyway.
They don't ask for permission. They just act.

The network lights up with encrypted coordinates, supply requests, safe house info.
This is what resistance looks like when you stop waiting for approval.

You know what's happening. You might be involved. You might be watching.
What do you see? What will you say?
""",
            "character_directions": {
                "Chris": "You're security—you know these rescue runs are happening. Do you report it? Do you look away? What goes in the log?",
                "Sarah": "You're watching students move faster than bureaucracy. What's your reflection? Your analysis?",
                "Tria": "You're documenting this. Details matter. Tell the story of what's actually happening in the real world.",
                "Kamea": "Your speech triggered this. Volunteers took action. What do you think is happening in those woods?",
            }
        },
        {
            "title": "The Storm Approaches",
            "time": "June 3, 2025, 2:45-6:00 PM",
            "description": """
SCENE: The Storm - Literal and Institutional

Weather is deteriorating. Wind picking up. The literal storm will hit soon.
The institutional storm is already here: divided community, families in danger,
security tightening, volunteers risking everything, network buzzing with encrypted activity.

What are you doing RIGHT NOW?
What do you see happening?
What's your next move?
""",
            "character_directions": {
                "Chris": "The storm is coming. Your orders are to tighten security. But those families... What do you do?",
                "Sarah": "You're watching chaos unfold. What do you understand about what's really at stake?",
                "Tria": "Everything is happening NOW. Document it. This is the story unfolding in real-time.",
                "Kamea": "Your moment is here. The board failed. Community is acting. What's your role in what comes next?",
            }
        }
    ]

    posts_by_character = {}

    # For Phase 0, focus on the first scene: Emergency Board Meeting
    # Generate multiple perspectives on the SAME scene
    current_scene = scenes[0]

    print(f"\n📍 SCENE: {current_scene['title']}")
    print(f"   Time: {current_scene['time']}")
    print(f"   Characters: {', '.join(current_scene['character_directions'].keys())}\n")

    for char_name, agent in agents.items():
        print(f"\nGenerating posts from {char_name}...")

        # Build character-specific scenario
        char_direction = current_scene['character_directions'].get(char_name, "")
        char_scenario = f"""{current_scene['description']}

{char_direction}

{characters[char_name].get('voice_notes', '')}

Remember: Report what you personally experienced. Name specific people, moments, decisions.
This post is part of the permanent record of what happened."""

        # Generate varied post types for this character's perspective on the scene
        # Most posts are short (twitter-length), one longer anchor post per character per scene
        post_specs = [
            {"type": "social", "length": "short", "image": True},  # Tweet-length with optional image
            {"type": "blog", "length": "long", "image": True},     # Anchor post with image description
        ]

        for post_spec in post_specs:
            post_type = post_spec["type"]
            print(f"  → Generating {post_type} post...")
            post = agent.generate_post(
                scenario=char_scenario,
                post_type=post_type,
                max_retries=2
            )

            if post:
                posts_by_character.setdefault(char_name, []).append(post)
                print(f"     ✓ Generated: {post.post_type.upper()}")
                print(f"       Location: {post.location} | Encryption: {post.encryption}")
                print(f"       Preview: {post.content[:80]}...")
            else:
                print(f"     ✗ Failed to generate {post_type}")

    # Step 4: Save and prepare for GitHub
    print("\n" + "="*70)
    print("Step 4: Saving posts and preparing GitHub issues...")
    print("="*70 + "\n")

    # Save all posts
    for char_name, agent in agents.items():
        agent.print_posts()
        output_file = agent.save_posts_to_json()
        print(f"Saved to: {output_file}\n")

    # Create GitHub issues manifest
    github_issues = []
    for char_name, posts in posts_by_character.items():
        for post in posts:
            github_issues.append({
                "title": f"[Draft] {char_name} - {post.post_type.upper()}",
                "body": post.to_github_issue_body(),
                "labels": ["draft", "ai-generated", "needs-review", char_name],
                "character": char_name,
                "post_type": post.post_type
            })

    # Save manifest
    manifest_file = "./content/drafts/github_issues_manifest.json"
    Path(manifest_file).parent.mkdir(parents=True, exist_ok=True)
    with open(manifest_file, 'w') as f:
        json.dump(github_issues, f, indent=2, default=str)

    print(f"✓ Saved GitHub issues manifest: {manifest_file}")
    print(f"  Total issues to create: {len(github_issues)}")

    # Step 5: Summary
    print("\n" + "="*70)
    print("PHASE 0 COMPLETE")
    print("="*70)
    print(f"\nGenerated posts:")
    for char_name, posts in posts_by_character.items():
        print(f"  {char_name}: {len(posts)} posts")

    print(f"\nNext steps:")
    print(f"1. Review posts in: ./content/drafts/")
    print(f"2. Create GitHub issues from: {manifest_file}")
    print(f"3. Test GitHub approval workflow")
    print(f"4. Proceed to Phase 1: Multi-character coordination\n")


if __name__ == "__main__":
    main()
