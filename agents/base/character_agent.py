"""
Base Character Agent - generates in-character posts for campus LAN network.

Each character maintains three-tier memory, uses Claude CLI (Claude Code plan) for consistency,
and coordinates through stigmergic bulletin board.
"""

import json
import time
import subprocess
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class Post:
    """A generated post from a character."""
    character_name: str
    content: str
    timestamp: str
    location: str
    encryption: str
    post_type: str  # "social", "blog", "editorial", "dm", "surveillance"
    score: float = 0.0
    approved: bool = False
    metadata: Dict = None
    images: List[Dict] = None  # List of {"description": str, "type": "security_cam|photo|etc", "prompt": str}

    def to_dict(self):
        return asdict(self)

    def to_github_issue_body(self) -> str:
        """Format post for GitHub issue creation."""
        return f"""
---
type: draft_post
character: {self.character_name}
timestamp: {self.timestamp}
location: {self.location}
encryption: {self.encryption}
post_type: {self.post_type}
---

## {self.character_name}

**Location:** {self.location}
**Encryption:** {self.encryption}
**Type:** {self.post_type}

---

{self.content}

---

*Generated at {datetime.now().isoformat()}*
"""


class CharacterAgent:
    """
    An AI agent embodying a specific character from the novel.

    Uses Claude API with character-specific prompting to generate authentic voices.
    Maintains conversation history for coherence and multi-turn generation.
    """

    def __init__(
        self,
        character_name: str,
        character_data: Dict,
        model: str = "claude-3-5-sonnet-20241022",
        voice_style: str = "ben_west"  # Your writing style as baseline
    ):
        self.character_name = character_name
        self.character_data = character_data
        self.model = model
        self.voice_style = voice_style

        # Three-tier memory
        self.short_term = []  # Current conversation context
        self.episodic_memory = []  # Recent events/posts
        self.semantic_memory = {}  # Character knowledge

        # Conversation history for multi-turn coherence
        self.conversation_history = []

        # Generated posts archive
        self.posts_generated = []

        print(f"Initialized {character_name} agent")

    def generate_post(
        self,
        scenario: str,
        post_type: str = "social",
        max_retries: int = 3
    ) -> Optional[Post]:
        """
        Generate a single post in character voice using Claude CLI (Claude Code plan).

        Args:
            scenario: The narrative trigger/context for this post
            post_type: Type of post ("social", "blog", "editorial", "dm", "surveillance")
            max_retries: How many times to retry on failure

        Returns:
            Post object with generated content, or None if generation failed
        """

        for attempt in range(max_retries):
            try:
                # Build character context
                system_prompt = self._build_system_prompt()
                user_message = self._build_user_prompt(scenario, post_type)

                # Build full prompt combining system + user
                full_prompt = f"{system_prompt}\n\n{user_message}"

                # Call Claude through CLI using your Claude Code max plan
                result = subprocess.run(
                    ["claude", "--print", "--output-format", "text"],
                    input=full_prompt,
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                if result.returncode != 0:
                    raise Exception(f"Claude CLI error: {result.stderr}")

                generated_content = result.stdout.strip()

                # Parse response for structured post
                post = self._parse_generated_post(generated_content, post_type, scenario)

                # Store in memory
                self.posts_generated.append(post)
                self.short_term.append(post)

                return post

            except Exception as e:
                print(f"Error generating post (attempt {attempt + 1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    return None

    def _build_system_prompt(self) -> str:
        """Build the system prompt that defines character."""
        char = self.character_data

        # Base style from Ben West's writing
        ben_style = """
You write with wit, personality, and vulnerability. You critique power structures explicitly.
You propose solutions while maintaining healthy skepticism. Show three-dimensional complexity.
Balance earnestness with sharp observation. Vulnerability and personality evident in every piece."""

        # Character-specific details
        char_prompt = f"""
You are {self.character_name} from "Mandate: The Monkey Flower Experiment" by Ben West.

{ben_style}

YOUR CHARACTER:
- Background: {char.get('background', 'Unknown')}
- Age: {char.get('age', 'Unknown')}
- Motivations: {char.get('motivations', 'Unknown')}
- Tags/Role: {', '.join(char.get('tags', []))}
- Social Position: {char.get('social_position', 'student/community')}

VOICE CHARACTERISTICS:
- Aesthetic lean: {char.get('aesthetic_lean', '60% cyberpunk, 40% solarpunk')}
- Known for: {char.get('voice_notes', 'Being authentic and thoughtful')}
- Style: {self.voice_style}

SETTING CONTEXT:
- You exist in an isolated campus (Akima University)
- Everything is networked but surveillance-watched
- Community is divided on refugee protection
- There's a storm both literal and figurative
- Technology is salvaged/sustainable hybrid
- Your posts appear on campus LAN boards

GENRE:
- 60% Cyberpunk: Encryption, resistance, surveillance, power critique
- 40% Solarpunk: Community action, solutions, hope, nature-tech integration
- Cypherpunk vocabulary: netrunner, ICE, cyberspace, chrome, jacking, black markets
- Solarpunk vocabulary: mesh networks, permaculture, bioregion, cooperative, sustainable

INSTRUCTIONS - GROUNDED IN SPECIFIC EVENTS:
1. ONLY comment on what you personally witnessed or directly experienced
2. Name specific actions, decisions, moments - not abstractions
3. "The board rejected emergency shelter" > "Systems of oppression"
4. "I watched them turn away three families" > "Power structures are cruel"
5. Reference specific conversations you overheard, decisions you saw, people involved
6. Ground vulnerability in concrete consequences, not philosophical reflection
7. Show wit through observation of specific moments, not general commentary
8. Keep posts 50-300 words
9. Feel like a witness reporting what happened, not a philosopher

CRITICAL: THIS BOOK IS MADE OF YOUR POSTS. Each post is a story moment.
- You are reporting events YOU EXPERIENCED
- Name specific people, locations, decisions, times
- Posts should advance the plot through your eyes
- Readers will build the full story from character posts
- Generic philosophy helps no one. Concrete moments build narrative.
"""
        return char_prompt

    def _build_user_prompt(self, scenario: str, post_type: str) -> str:
        """Build the user message that triggers post generation."""

        # Post type specifications
        post_specs = {
            "social": {
                "length": "50-150 words (tweet-length)",
                "description": "Quick, urgent update. Can include image description if relevant.",
                "include_image": True
            },
            "blog": {
                "length": "300-500 words (anchor post)",
                "description": "Longer analysis/narrative. Often includes detailed image description.",
                "include_image": True
            },
            "editorial": {
                "length": "400-600 words (opinion piece)",
                "description": "Formal op-ed. Can include security footage descriptions.",
                "include_image": True
            },
            "dm": {
                "length": "100-300 words (private message)",
                "description": "Confidential message. Often includes specific details/instructions.",
                "include_image": False
            },
            "surveillance": {
                "length": "200-400 words (security log)",
                "description": "Security camera or surveillance report. Heavy on technical details and image descriptions.",
                "include_image": True
            }
        }

        spec = post_specs.get(post_type, post_specs["social"])

        image_instruction = ""
        if spec.get("include_image"):
            image_instruction = """

IF YOUR POST INCLUDES AN IMAGE:
- Describe what photo/screenshot would accompany this
- Examples: "Security cam footage from north entrance, 14:23" or "Photo of families camping in south field"
- Add: [image: <description>] at the end

The actual image will be generated separately from your description."""

        return f"""
Generate a {post_type} post for the campus LAN network.

POST TYPE SPECIFICATIONS:
- Length: {spec['length']}
- Purpose: {spec['description']}

SCENARIO/CONTEXT:
{scenario}

REQUIRED OUTPUT FORMAT:
```
[timestamp] HH:MM
network_location: campus.lan/boards/{{location}}
encryption: {{public|encrypted|partial}}
user: {{your_handle}}

{{post_content - {spec['length']}}}

{{optional: attachments or metadata}}
```

CRITICAL REQUIREMENTS:
1. This is your actual witnessed account of events
2. Include specific names, times, locations, decisions
3. Write like you were there - report what you saw
4. Keep consistent with character voice and position{image_instruction}

Generate authentic, voice-consistent post now:
"""

    def _parse_generated_post(self, response: str, post_type: str, scenario: str) -> Post:
        """Parse Claude's response into structured Post object."""
        # Extract timestamp
        import re

        timestamp_match = re.search(r'\[(\d{2}:\d{2})\]', response)
        timestamp = timestamp_match.group(1) if timestamp_match else datetime.now().strftime("%H:%M")

        # Extract location
        location_match = re.search(r'campus\.lan/boards/(\w+)', response)
        location = location_match.group(1) if location_match else "general"

        # Extract encryption
        encryption_match = re.search(r'encryption:\s*(public|encrypted|partial)', response, re.IGNORECASE)
        encryption = encryption_match.group(1) if encryption_match else "public"

        # Extract content (everything between ``` markers or after user:)
        content_match = re.search(r'user:.*?\n\n(.*?)(?:\n\n\[image:|$)', response, re.DOTALL)
        if content_match:
            content = content_match.group(1).strip()
        else:
            # Fallback: just use the whole response
            content = response.strip()

        # Extract image descriptions
        images = []
        image_matches = re.findall(r'\[image:\s*(.+?)\]', response)
        for img_desc in image_matches:
            images.append({
                "description": img_desc.strip(),
                "type": "auto",  # Will be inferred from description
                "prompt": f"Scene from Akima University: {img_desc.strip()}"
            })

        post = Post(
            character_name=self.character_name,
            content=content,
            timestamp=f"{datetime.now().date()} {timestamp}",
            location=location,
            encryption=encryption,
            post_type=post_type,
            metadata={"scenario": scenario},
            images=images if images else None
        )

        return post

    def save_posts_to_json(self, output_file: str = None):
        """Save generated posts to JSON file."""
        if not output_file:
            output_file = f"./content/drafts/{self.character_name}_{datetime.now().isoformat()}.json"

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)

        posts_data = {
            "character": self.character_name,
            "generated_at": datetime.now().isoformat(),
            "posts": [p.to_dict() for p in self.posts_generated],
            "total_posts": len(self.posts_generated)
        }

        with open(output_file, 'w') as f:
            json.dump(posts_data, f, indent=2, default=str)

        print(f"✓ Saved {len(self.posts_generated)} posts to {output_file}")
        return output_file

    def print_posts(self):
        """Pretty-print generated posts."""
        print(f"\n{'='*70}")
        print(f"{self.character_name} - Generated Posts ({len(self.posts_generated)})")
        print(f"{'='*70}\n")

        for i, post in enumerate(self.posts_generated, 1):
            print(f"POST {i}")
            print(f"Type: {post.post_type} | Location: {post.location} | Encryption: {post.encryption}")
            print(f"Timestamp: {post.timestamp}")
            print("-" * 70)
            print(post.content)
            print(f"{'='*70}\n")
