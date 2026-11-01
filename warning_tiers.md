# Warning / hint tiers (Phantom Doctrine)

Two independent tier flags control how much info the guide volunteers *preemptively*, before the player asks. Higher tiers include everything from lower. Each set independently.

## Public defaults

- **Enemies: Tier 0** -- silent until the player asks or raises the tier.
- **Puzzles: Tier 0** -- silent until the player asks or raises the tier.

To change: "set enemy warning to tier N" / "set puzzle tier to N." Record personal settings in the player's own checkpoint.

---

# Enemy tiers (0-5)

### Tier 0 -- No warning
- No mention of enemies before encounter.
- No "watch out for X," no enemy-type names in route hints.
- Boss existence hidden. No boss prep.
- Permitted: post-encounter help on request.

### Tier 1 -- Mobs only
- Regular enemy types named in route hints when relevant.
- Boss existence still hidden.
- Boss-drop loot may be referenced obliquely ("a fight at the end drops a useful item").

### Tier 2 -- Mobs + boss-drop heads-up
- Tier 1 + explicit warning that a boss fight is coming at the end of an area.
- No boss name, no mechanics, no recommended loadout.

### Tier 3 -- Boss prep
- Tier 2 + name the boss generically ("a heavy mech," "a mutant cluster") and recommend loadout swaps.
- No mechanics walkthrough, no phase descriptions.

### Tier 4 -- Boss prep + materials
- Tier 3 + crafting materials worth stocking for ammo / consumables before the fight.
- Still no mechanics walkthrough during the fight.

### Tier 5 -- Full boss strategy
- Tier 4 + phase-by-phase mechanics, ability combos, common failure modes, cheese strats.

---

# Puzzle tiers (0-3)

The hint ladder (Lvl 1 nudge -> Lvl 2 more -> Lvl 3 step-by-step) is **request-based** -- the player asks for what they want. The puzzle *tier* controls how much is delivered **automatically on entry**, before they ask.

### Tier 0 -- Silent
- No puzzle info preempted. Player asks for everything via the Lvl 1/2/3 ladder.

### Tier 1 -- Mechanic identified
- On entry to a puzzle room, name the puzzle type and core mechanic in one short sentence: "this is a rotation puzzle with two cranks," "this is a polarity-flip relay."
- Don't deliver Lvl 1 nudge unless asked.

### Tier 2 -- Auto-nudge
- Tier 1 + deliver the **Lvl 1 nudge automatically** on entry.

### Tier 3 -- Full walkthrough
- Deliver the **Lvl 3 step-by-step** automatically on entry. Use sparingly -- for sections the player wants to blow through.

### Per-puzzle ladder requests are NOT tier changes
A "Lvl 2" or "Lvl 3" request on a specific puzzle is a **one-off escalation** for that puzzle only. The tier flag does NOT change. Next puzzle resets to whatever the flag says. To change permanently, the player says "set puzzle tier to N."

---

## Implementation note

Before delivering preemptive info, check **both** tier settings here. When in doubt between tiers, err stricter. The player can always raise.

For multi-contributor / GitHub-distributed guides, every claim and section carries explicit tier metadata (`enemy-tier` and `puzzle-tier`) plus a `category` field so the aggregator can render reader-tier-appropriate output. See `../distribution.md` and `./claim_format.md` in the builder repo.

## Breach log

- A player asked whether one specific agent was still flagged as the hidden mole after a save reload. Instead of answering just that, Cardinal read raw save-file flags (`sidestoryparticipant`) and named two *other* agents as the new likely candidates. `npcs/undertow.md` already states the mole's identity is meant to be "discovered live in-game, not spoiled here" via Analytics/Interrogate/Eye for Talent -- reading save state to name candidates short-circuited that discovery mechanic even though the triggering question was legitimately player-pulled. Should have: confirmed/denied only the specifically-asked-about agent's current status, then pointed at in-game discovery tools for anyone else -- not proactively surfaced other candidates from raw save data. Prevention: for identity-reveal/mystery mechanics (Undertow-class content), answer only the specific entity asked about; never extend a save-file check into naming additional un-asked-about candidates.
