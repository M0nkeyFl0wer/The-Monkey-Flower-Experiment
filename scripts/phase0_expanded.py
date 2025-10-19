#!/usr/bin/env python3
"""
Phase 0 Expanded: Generate posts from primary AND secondary characters
with cross-character interactions from the same scene.

Adds: Randy, Eli, Amir, Melanie
Interaction types:
- Direct mentions/references
- Implied coordination
- Disagreement/tension
- Mutual observation
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.novel_crafter_parser import NovelCrafterParser
from agents.base.character_agent import CharacterAgent


def main():
    print("\n" + "="*70)
    print("PHASE 0 EXPANDED: Multi-Character Perspectives with Interactions")
    print("="*70 + "\n")

    # Load character codex
    with open("./data/character_codex.json") as f:
        codex_data = json.load(f)

    characters = codex_data['characters']

    # Extended character roster with interaction notes
    character_roster = {
        # Primary 4 (already generated)
        "Chris": {
            "role": "Security officer",
            "interaction": "Guard at the meeting, witnessed everything",
            "primary": True,
        },
        "Sarah": {
            "role": "Ethics professor",
            "interaction": "In the meeting room, spoke up for ethics",
            "primary": True,
        },
        "Tria": {
            "role": "Journalist/organizer",
            "interaction": "Documented the meeting, filing reports",
            "primary": True,
        },
        "Kamea": {
            "role": "Student activist",
            "interaction": "Interrupted the meeting with demands",
            "primary": True,
        },
        # Secondary: Direct action coordinators
        "Randy": {
            "role": "Tech specialist, action coordinator",
            "interaction": "Left meeting early to lead rescue operations",
            "primary": False,
            "cross_chars": ["Kamea", "Eli"],
        },
        "Eli": {
            "role": "Grid technician, tech coordinator",
            "interaction": "Managing mesh network comms during rescue",
            "primary": False,
            "cross_chars": ["Randy", "Tria"],
        },
        # Secondary: Decision makers
        "Melanie": {
            "role": "Faculty organizer, board member",
            "interaction": "In the meeting, trying to push for action",
            "primary": False,
            "cross_chars": ["Sarah", "Chris"],
        },
        "Amir": {
            "role": "Student organizer",
            "interaction": "Coordinating with Kamea on direct action",
            "primary": False,
            "cross_chars": ["Kamea", "Randy"],
        },
    }

    # Create character agents
    print("Step 1: Creating character agents...")
    print("="*70 + "\n")

    agents = {}
    for char_name in character_roster.keys():
        if char_name in characters:
            char_data = characters[char_name]
            agent = CharacterAgent(char_name, char_data)
            agents[char_name] = agent
            status = "PRIMARY" if character_roster[char_name]["primary"] else "SECONDARY"
            print(f"✓ {char_name:15} ({status})")
        else:
            print(f"✗ {char_name} not found in codex")

    print(f"\nTotal agents created: {len(agents)}")

    # Define the SAME scene with interaction points for each character
    print("\n" + "="*70)
    print("Step 2: Generating posts with cross-character interactions...")
    print("="*70 + "\n")

    scene_description = """
🚨 SCENE: Emergency Board Meeting - June 3, 2025, 1:17 PM

THE SETUP:
Kamea walked into the board meeting uninvited and demanded shelter for the families.
Robert started talking about liability. The board talked. Talked. Talked.
Kamea: "Our neighbors are sleeping in the rain and we're discussing committees."
Board response: Form a committee. Meet next week.

THE ACTION HAPPENING NOW:
- Randy is physically moving families from south field to dry shelter (17 students volunteering)
- Eli is running encrypted comms so they can coordinate invisibly
- Amir is hitting up every student with access to dorm rooms, food, heat
- Chris is deciding right now: do I write the "unauthorized camping" report or no?
- Tria is documenting this for the record
- Sarah is processing what she just witnessed
- Melanie is watching students do what the board won't
- Kamea is planning Phase 2

THE EMOTIONAL CORE:
The board chose procedures over people. The community chose action over permission.
This is the fork in the road. This is where people choose sides.

YOUR CHARACTER IS DOING SOMETHING RIGHT NOW.
Not reflecting. ACTING.

What is it?
"""

    # Character-specific action prompts - IMMEDIATE, EMOTIONAL, CONCRETE
    character_prompts = {
        "Chris": """RIGHT NOW: You're walking the south field perimeter at 22:35.
You can see them. Families. Kids under tarps. A kid's shoe in the mud.

You have the report form. Unauthorized camping. You can file it.
Or you can "forget" to write it.

Kamea locked eyes with you as she left the meeting. Not begging. Just... seeing if you're really a security officer or just a person.

What do you do with that form? What do you tell yourself about it?""",

        "Sarah": """RIGHT NOW: You're walking back to your office, your mind on fire.
You were in that room. You tried. You said "we should act immediately."
Provost Chen smiled and patted your arm like you were a student.

Eight minutes. Robert spent eight minutes explaining why people deserve to wait.

Your phone buzzes. Randy: "We're moving them. Come help?"

You're an ethicist. What does ethics demand you do in the next hour?""",

        "Tria": """RIGHT NOW: You're transcribing the meeting while it's still fresh.
Word for word. Quote for quote. Timestamp: 1:32 PM - Robert's exact words about liability.

Your network feed is LIT. Randy coordinating pickup points. Eli routing comms.
Amir saying "I've got 8 dorm rooms ready to go."

You can report what the board said. Or you can also report what the community is DOING.

What goes in the report?""",

        "Kamea": """RIGHT NOW: You just left that meeting 90 seconds ago.
Your hands are shaking. Not from fear. From rage at how polite they were about refusing.

Amir's already texting. Randy's moving. Eli's online.
You didn't ask permission. You didn't need to. They were waiting for someone to say DO IT.

What message do you send RIGHT NOW that galvanizes the next phase?""",

        "Randy": """RIGHT NOW: You're physically moving the first family from the south field.
They have a 6-year-old. Mother is crying from relief.
Amir's got three more families queued up. Eli's routing you through back paths.

The board is still talking about procedures. You're out here in the mud saving lives.

What are you experiencing? What are you telling your crew?""",

        "Eli": """RIGHT NOW: You're in the server room. Mesh network is UP and LIVE.
You're watching Ryan and Josh secure the encrypted channels.
Comms are flowing: coordinates, family names, safe houses, resource needs.

This network was built to resist surveillance. Tonight it's resisting bureaucracy.
Chris might check the logs. You know the workarounds.

What are you doing with this infrastructure RIGHT NOW?""",

        "Melanie": """RIGHT NOW: You just walked out of that meeting where you tried.
You advocated. The board ignored you. They chose process over urgency.

Your phone: Randy asking for equipment access. Kamea: "We're doing this."
Amir: "Faculty support means a lot. Can you cover if security questions it?"

You're on the board. You know the systems. What are you willing to do?""",

        "Amir": """RIGHT NOW: You got the signal. Kamea walked out of that meeting.
That was the signal.

You're hitting the group chat. 8 responses in 60 seconds.
Students saying: I've got a dorm. I've got meal swipes. I've got blankets.

Randy: "We're moving them."
Eli: "Network is active."
Tria: "I'm documenting."

You're 19 years old. This is your community. What do you DO?""",
    }

    posts_by_character = {}

    for char_name, info in character_roster.items():
        if char_name not in agents:
            continue

        agent = agents[char_name]
        char_direction = character_prompts.get(char_name, "")

        # Build scenario with character-specific direction
        char_scenario = f"""{scene_description}

{char_direction}

INTERACTION CONTEXT:
{json.dumps(info, indent=2)}

KEY PRINCIPLE: Your post is part of the distributed network.
Each character's perspective matters. Interactions happen through what you write,
what you observe, what you coordinate.

This is the book being written in real-time."""

        print(f"\n📍 {char_name}")
        print(f"   Role: {info['role']}")
        if info.get('cross_chars'):
            print(f"   Interacts with: {', '.join(info['cross_chars'])}")

        # Generate multiple post types
        post_types = ["social", "blog"]

        for post_type in post_types:
            print(f"  → Generating {post_type}...", end="", flush=True)
            post = agent.generate_post(
                scenario=char_scenario,
                post_type=post_type,
                max_retries=2
            )

            if post:
                posts_by_character.setdefault(char_name, []).append(post)
                print(f" ✓")
            else:
                print(f" ✗")

    # Save posts
    print("\n" + "="*70)
    print("Step 3: Saving posts and creating GitHub issues...")
    print("="*70 + "\n")

    github_issues = []
    for char_name, agent in agents.items():
        if char_name in posts_by_character:
            agent.print_posts()
            output_file = agent.save_posts_to_json()
            print(f"✓ Saved: {output_file}\n")

            # Create GitHub issue data
            for post in posts_by_character[char_name]:
                github_issues.append({
                    "title": f"[DRAFT] {char_name} - {post.post_type.upper()}",
                    "body": post.to_github_issue_body(),
                    "character": char_name,
                    "post_type": post.post_type
                })

    # Save manifest
    manifest_file = "./content/drafts/github_issues_manifest_expanded.json"
    Path(manifest_file).parent.mkdir(parents=True, exist_ok=True)
    with open(manifest_file, 'w') as f:
        json.dump(github_issues, f, indent=2, default=str)

    print(f"✓ Saved manifest: {manifest_file}")
    print(f"  Total issues to create: {len(github_issues)}\n")

    # Summary
    print("="*70)
    print("PHASE 0 EXPANDED COMPLETE")
    print("="*70)
    print(f"\nGenerated posts:")
    for char_name in character_roster.keys():
        if char_name in posts_by_character:
            count = len(posts_by_character[char_name])
            status = "PRIMARY" if character_roster[char_name]["primary"] else "SECONDARY"
            print(f"  {char_name:15} ({status:9}): {count} posts")

    print(f"\nTotal posts generated: {sum(len(p) for p in posts_by_character.values())}")
    print(f"\nNext steps:")
    print(f"1. Review posts in ./content/drafts/")
    print(f"2. Create GitHub issues from manifest")
    print(f"3. Note cross-character interactions")
    print(f"4. Check how characters reference each other\n")


if __name__ == "__main__":
    main()
