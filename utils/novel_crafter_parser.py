"""
Parse Novel Crafter export into structured character codex and story data.

Reads from /data/novel_export/ (copied from Novel Crafter export)
Creates character_codex.json, story_timeline.json with canonical constraints.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
from dataclasses import dataclass, asdict
import yaml


@dataclass
class Character:
    """Canonical character data from novel."""
    name: str
    age: int = None
    tags: List[str] = None
    background: str = ""
    motivations: str = ""
    connections: List[str] = None
    voice_notes: str = ""
    aesthetic_lean: str = ""  # "cypherpunk", "solarpunk", or "balanced"
    sample_dialogue: List[str] = None
    personality_traits: List[str] = None
    knowledge_scope: Dict[str, List[str]] = None  # What they know at different story points
    emotional_state: str = ""
    social_position: str = ""  # "student", "faculty", "staff", "admin", etc.

    def to_dict(self):
        return asdict(self)


class NovelCrafterParser:
    """Parse Novel Crafter markdown exports into canonical data."""

    def __init__(self, novel_export_dir: str = "./data/novel_export"):
        self.export_dir = Path(novel_export_dir)
        self.characters: Dict[str, Character] = {}
        self.story_events: List[Dict] = []
        self.locations: Dict[str, Dict] = {}

    def parse_all(self):
        """Parse all files from novel export."""
        self._parse_character_files()
        self._extract_timeline_events()
        self._build_relationship_map()
        return self

    def _parse_character_files(self):
        """
        Parse character markdown files from Novel Crafter export.
        Expected format: /data/novel_export/characters/{name}/entry.md
        """
        characters_dir = self.export_dir / "characters"
        if not characters_dir.exists():
            print(f"No characters directory found at {characters_dir}")
            return

        for char_dir in characters_dir.iterdir():
            if not char_dir.is_dir():
                continue

            entry_file = char_dir / "entry.md"
            if not entry_file.exists():
                continue

            try:
                character = self._parse_character_md(entry_file)
                if character:
                    self.characters[character.name] = character
                    print(f"✓ Parsed: {character.name}")
            except Exception as e:
                print(f"✗ Error parsing {char_dir.name}: {e}")

    def _parse_character_md(self, filepath: Path) -> Character:
        """Parse a single character markdown file."""
        content = filepath.read_text()

        # Extract YAML frontmatter
        lines = content.split('\n')
        frontmatter_end = None
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                frontmatter_end = i
                break

        frontmatter = {}
        if frontmatter_end:
            yaml_content = '\n'.join(lines[1:frontmatter_end])
            try:
                frontmatter = yaml.safe_load(yaml_content) or {}
            except:
                pass

        # Extract body content
        body_start = frontmatter_end + 1 if frontmatter_end else 0
        body = '\n'.join(lines[body_start:])

        # Parse markdown body for character fields
        char_data = self._extract_character_fields(body, frontmatter)

        if not char_data.get('name'):
            # Try to extract from filename
            char_data['name'] = filepath.parent.name.split('-')[0].strip()

        return Character(**char_data)

    def _extract_character_fields(self, body: str, frontmatter: Dict) -> Dict[str, Any]:
        """Extract character information from markdown body and frontmatter."""
        data = {
            'name': frontmatter.get('name', 'Unknown'),
            'tags': frontmatter.get('tags', []),
            'background': '',
            'motivations': '',
            'connections': [],
            'voice_notes': '',
            'sample_dialogue': [],
            'personality_traits': [],
            'aesthetic_lean': 'balanced'
        }

        # Extract sections from markdown
        sections = re.split(r'^## ', body, flags=re.MULTILINE)

        for section in sections:
            if 'background' in section.lower():
                # Extract background
                match = re.search(r'Background[:\s]*(.+?)(?=^##|\Z)', section, re.DOTALL | re.MULTILINE)
                if match:
                    data['background'] = match.group(1).strip()

            elif 'motivation' in section.lower():
                match = re.search(r'Motivation[:\s]*(.+?)(?=^##|\Z)', section, re.DOTALL | re.MULTILINE)
                if match:
                    data['motivations'] = match.group(1).strip()

            elif 'connection' in section.lower():
                # Extract character connections (who they know)
                matches = re.findall(r'@(\w+)|mentions? (\w+)', section, re.IGNORECASE)
                data['connections'] = [m[0] or m[1] for m in matches if m[0] or m[1]]

            elif 'age' in section.lower():
                match = re.search(r'Age[:\s]*(\d+)', section)
                if match:
                    data['age'] = int(match.group(1))

        # Extract fields from frontmatter with fallbacks
        if frontmatter.get('fields'):
            fields = frontmatter['fields']
            if isinstance(fields, dict):
                data.update(fields)

        return data

    def _extract_timeline_events(self):
        """Extract story events and timeline from chats/scenes."""
        # This would parse chat/scene files for timeline
        # For now, create placeholder with key date
        self.story_events = [
            {
                'date': '2025-06-03',
                'time': '15:30',
                'event': 'Storm approaching, community divided on refugee protection',
                'key_characters': ['Chris', 'Sarah', 'Tria', 'Kamea', 'Randy'],
                'significance': 'Major conflict point'
            }
        ]

    def _build_relationship_map(self):
        """Build graph of character relationships."""
        relationships = {}
        for name, char in self.characters.items():
            relationships[name] = {
                'knows': char.connections or [],
                'social_position': char.social_position,
                'allegiances': self._infer_allegiances(char)
            }
        return relationships

    def _infer_allegiances(self, char: Character) -> List[str]:
        """Infer character's ideological position from tags and background."""
        allegiances = []

        if not char.tags:
            return allegiances

        tags_lower = [t.lower() for t in char.tags]

        # Cypherpunk indicators
        if any(w in tags_lower for w in ['rebel', 'security', 'resistance', 'crypto', 'hacker']):
            allegiances.append('cypherpunk')

        # Solarpunk indicators
        if any(w in tags_lower for w in ['organizer', 'community', 'sustainability', 'ethics']):
            allegiances.append('solarpunk')

        # Authority
        if any(w in tags_lower for w in ['admin', 'faculty', 'staff', 'president', 'board']):
            allegiances.append('administration')

        return allegiances

    def save_codex(self, output_file: str = "./data/character_codex.json"):
        """Save parsed character codex to JSON."""
        codex = {
            'characters': {name: char.to_dict() for name, char in self.characters.items()},
            'story_events': self.story_events,
            'generated_at': datetime.now().isoformat(),
            'total_characters': len(self.characters)
        }

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(codex, f, indent=2, default=str)

        print(f"\n✓ Saved character codex to {output_file}")
        return codex

    def print_summary(self):
        """Print summary of parsed data."""
        print(f"\n{'='*60}")
        print(f"Novel Crafter Export Summary")
        print(f"{'='*60}")
        print(f"Characters parsed: {len(self.characters)}")
        print(f"\nCharacters:")
        for name, char in sorted(self.characters.items()):
            tags = ", ".join(char.tags) if char.tags else "untagged"
            print(f"  • {name:20} | {tags}")

        print(f"\nStory Events: {len(self.story_events)}")
        for event in self.story_events:
            print(f"  • {event['date']} - {event['event']}")

        print(f"{'='*60}\n")


if __name__ == "__main__":
    parser = NovelCrafterParser()
    parser.parse_all()
    parser.print_summary()
    parser.save_codex()
