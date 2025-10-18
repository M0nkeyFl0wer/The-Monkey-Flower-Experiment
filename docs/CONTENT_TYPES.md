# Content Types & Communication Formats

## Overview

Characters communicate through multiple channels on the isolated campus network. Each format has distinct aesthetics and constraints.

---

## Campus LAN Network Posts

### Public Board Posts
- **Format:** Campus.LAN bulletin boards
- **Visibility:** Everyone on campus network
- **Encryption:** Public/unencrypted
- **Length:** 50-200 words
- **Tone:** Community-facing, public position
- **Use:** Announcements, community organizing, public opinion

**Example:**
```
[2025-06-03 15:30]
network_location: campus.lan/boards/general
encryption: public
user: chris_j

The board's decision today contradicts everything we claimed to stand for.
We say we value community. We say we protect the vulnerable. Today, we
protected our liability instead.

That's not a statement—that's an observation. If anyone wants to talk about
what we actually DO instead of what we SAY we do, you know how to reach me.

—Chris
```

### Encrypted Board Posts
- **Format:** Encrypted subboards (key distribution on mesh)
- **Visibility:** Only those with decryption key
- **Encryption:** Public-key encrypted, verification required
- **Length:** 100-300 words
- **Tone:** Trusted circle, strategic discussion
- **Use:** Planning, sensitive analysis, protected speech

**Example:**
```
[ENCRYPTED - KEY: mesh-access-2025-06]
network_location: campus.lan/boards/strategy-encrypted
encryption: encrypted (ED25519 verification required)
user: tria_auth (signature verified)

Investigative findings on budget reallocation:
- $200k "emergency refugee accommodation" appears nowhere in Q2 ledgers
- Cross-referenced with facility maintenance logs
- Building 7 show unusual access patterns (nights only)
- This is either incompetence or intentional obfuscation

If they're hiding people to help them, that's one story.
If they're hiding people to avoid accountability, that's another.
I'm working the second angle. Interested?

—Tria
```

---

## Mesh Network Communications

### Private Mesh Chats
- **Format:** Direct peer-to-peer encrypted chat (Yggdrasil/similar mesh)
- **Visibility:** Only sender + recipient
- **Encryption:** End-to-end, ephemeral
- **Length:** 20-100 words
- **Tone:** Personal, tactical, immediate
- **Use:** Private coordination, personal stakes, quick strategy

**Example:**
```
[MESH - PRIVATE]
timestamp: 2025-06-03 16:45
from: kamea@mesh.local
to: chris@mesh.local
encryption: ephemeral_e2e

Chris—I saw you on the second floor. Are you in or out?
Because the people in 7 need to know TODAY.
```

### Mesh Group Discussions
- **Format:** Multi-party mesh channel (trusted circle only)
- **Visibility:** Members of the group (role-based access)
- **Encryption:** Group key, forward secrecy
- **Length:** 50-200 words
- **Tone:** Collaborative, vulnerable, strategic
- **Use:** Planning, debate, building consensus

**Example:**
```
[MESH - GROUP: refuge-network]
timestamp: 2025-06-03 17:00
members: tria, kamea, chris, sarah (7 total)
encryption: group_key_ed25519

sarah: The ethical question here isn't IF we help.
       It's HOW without destroying the institution.
       If we burn it down, who runs it tomorrow?

kamea: The institution is already burning. We're just
       choosing not to watch.

chris: What if we could do both? Keep some legitimacy,
       change from inside?

tria:  That's what I'm documenting. Proof that we tried
       the legitimate path first.
```

---

## Blog Posts & Editorials

### Character Blogs
- **Format:** Medium-form writing on mesh/bulletin board
- **Visibility:** Public or encrypted, character choice
- **Encryption:** Can be either public or key-protected
- **Length:** 300-600 words
- **Tone:** Thoughtful, narrative-driven, personal stakes
- **Use:** Analysis, opinion, character development, philosophy

**Example:**
```
[Tria's Blog - "Reflections on a Tumultuous Night"]
campus.lan/blogs/tria
2025-06-03 23:00

As the storm approaches, both literally and figuratively,
Akima's community is divided yet resilient...

[Full blog content]
```

### Faculty/Admin Editorials
- **Format:** Official or pseudo-official statements
- **Visibility:** Public boards or private staff channels
- **Encryption:** Usually unencrypted for accountability
- **Length:** 200-400 words
- **Tone:** Professional, constrained by position, hints of real opinion
- **Use:** Policy statements, community messaging

---

## Surveillance & System Content

### Camera Footage Descriptions
- **Format:** Logs from automated surveillance system
- **Visibility:** System-only (with occasional leaks)
- **Encryption:** Signed logs (verifiable)
- **Length:** 100-250 words
- **Tone:** Clinical, emotionless, sometimes glitching
- **Use:** Show hidden story, confirm character actions, reveal surveillance scope

**Example:**
```
[SURVEILLANCE LOG - AUTOMATED]
timestamp: 2025-06-03 16:15
camera_id: BUILDING7_EAST_B02
location: Building 7, Level 2 East Entrance
classification: thermal_imaging

Movement detected: 4 heat signatures (human-scale) entering
restricted zone. Access credentials scanned: OVERRIDE (admin_key_2).
Duration: 4m 22s. Equipment noted: thermal blankets (cold-masking).

System note: Data inconsistency - audit log shows no admin
override at 16:15. Possible system compromise or deliberate erasure.
```

### Anonymous Whistleblower Posts
- **Format:** One-time encrypted drops on mesh
- **Visibility:** General public (untraceable origin)
- **Encryption:** Burner account, single-use keys
- **Length:** 100-300 words
- **Tone:** Urgent, fragmentary, emotional
- **Use:** Leak information, create tension, introduce new facts

**Example:**
```
[ANONYMOUS DROP - ENCRYPTED SINGLE-USE]
timestamp: 2025-06-03 18:30
source: unknown
key: [single-use burn-key]

They're moving people through the maintenance tunnels.
I work in facilities. I've seen the supply runs.

The board doesn't know. They couldn't vote to reject what
they don't know exists.

I can't say more. But if anyone's wondering where the
money REALLY goes—check the tunnels.
```

---

## Mechanical Bugs (Surveillance)

### Sensor Network Posts
- **Format:** Automated reports from distributed sensors
- **Visibility:** Public (part of campus monitoring system)
- **Encryption:** Signed system logs
- **Length:** 50-150 words
- **Tone:** Data-driven, technical, occasionally corrupted
- **Use:** Add texture, show omnipresent surveillance, create paranoia

**Example:**
```
[SENSOR NETWORK REPORT]
timestamp: 2025-06-03 19:45
device_id: BUG_CLUSTER_SOUTH_03
type: ambient_sensing
location: South Campus, quadrangle area

Air composition anomaly detected:
- CO2: baseline 400ppm → 650ppm (localized)
- Sulfur compounds: trace → elevated
- Particle count: +340% (combustion byproducts)

Interpretation: Controlled fire approximately 150m south-southeast
Duration: 17 minutes. Currently extinguished.
Assessment: Intentional (campfire or ceremonial burn)
```

---

## Format Guidelines

### When to Use Each Type

| Situation | Best Format | Why |
|-----------|------------|-----|
| Public announcement | Board post | Everyone sees, deniability limited |
| Private strategy | Mesh chat | Secure, ephemeral, traceable to member |
| Detailed analysis | Blog | Space for nuance, builds credibility |
| Urgent alert | Anonymous drop | No traceability, immediate impact |
| Hidden action | Surveillance log | Shows what actually happened |
| Personal moment | Mesh group | Vulnerability with trusted circle |

### Character Communication Patterns

**Tria:** Blogs (investigation) + Encrypted posts (findings) + Anonymous drops (bombshells)

**Kamea:** Encrypted essays + Mesh group discussions + Philosophical blogs

**Chris:** Personal mesh chats + Public board (conflicted) + Surveillance logs (revealing conflict)

**Sarah:** Faculty editorials + Private mesh (mentoring) + Blogs (ethics analysis)

**Randy:** Quick mesh messages + Surveillance leaks + Anonymous technical posts

---

## Writing Standards by Format

### Post Tone Calibration

**Public board posts:**
- Assume monitored/archived
- More formal, message-craft needed
- Emotional honesty within professional bounds
- ~100-150 words

**Encrypted posts:**
- Can be more raw/strategic
- Assume trusted audience
- Technical jargon acceptable
- ~150-300 words

**Mesh group chats:**
- Rapid-fire, conversational
- Vulnerability ok
- Mix of strategy + personal
- 20-100 words each speaker

**Blogs:**
- Full narrative voice
- Personal + political
- Time for reflection
- 300-600 words

**Surveillance logs:**
- Objective tone + hidden subtext
- Clinical language
- Data-driven but emotionally resonant
- 100-250 words

---

## Privacy & Deniability

### Plausible Deniability Scale

```
Most Deniable:
  Anonymous drop (untraceable)
  ↓
  Surveillance leak (system error)
  ↓
  Encrypted mesh (requires key)
  ↓
  Encrypted board (audit trail)
  ↓
  Public board (full record)
  ↓
Least Deniable:
  Faculty editorial (official name attached)
```

Characters choose format based on:
- Risk tolerance
- Message importance
- Audience trust level
- Need for escalation

---

## Examples by Character

### Tria's Day
```
6:00 AM   → Encrypted blog draft (finding analysis)
9:30 AM   → Mesh group chat (coordinate timing)
14:00     → Public board post (general announcement)
16:30     → Anonymous drop (smoking gun evidence)
22:00     → Mesh group reflection (personal stakes)
```

### Chris's Day
```
7:00 AM   → Mesh chat with Sarah (seeking permission to help)
10:00     → Private thoughts (internal conflict)
15:30     → Public board post (token critique, not actual commitment)
18:00     → Mesh chat with Kamea (final decision)
20:00     → Surveillance logs show access override (actual commitment)
```

---

## Magazine Compilation

In the final magazine, readers experience the story through this layered communication:
- **Section 1:** Public posts (official narrative)
- **Section 2:** Leaked encrypted posts (real narrative)
- **Section 3:** Surveillance logs (hidden truth)
- **Section 4:** Anonymous drops (whisper network)
- **Interlude:** Blog/essay pieces (reflection)

This creates depth: readers see the same events from multiple angles with conflicting interpretations.
