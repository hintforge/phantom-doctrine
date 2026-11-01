# Phantom Doctrine UI reference -- reading screenshots and icons

How to read the game's screens from player screenshots without guessing.
Written 2026-08-21; expanded same day from a full sweep of the player's
screenshot archive (~60 game captures with tooltips). Two parts: fixed screen
anatomy, and a living icon legend that grows one confirmed row at a time.

## Reading procedure (binding)

1. **Identify the screen** by its header text (`AGENT DOSSIER`, `AGENT
   TREATMENT`, `PERK ACQUISITION`, `AGENT OVERVIEW`, `LOADOUT`, `BODY
   ENGINEERING: TREATMENT COMPLETE`, `MK ULTRA: TREATMENT COMPLETE`), not by
   guessing from layout.
2. **Transcribe the regions in fixed order** into numbers/text BEFORE
   interpreting. A stat you didn't transcribe is a stat you can't cite.
3. **Perk / training / talent / marker tile:** identify it from the in-game
   tooltip (hover text) or a save id, not from the picture. If you do not have
   the tooltip, say so and ask the player ONCE for it. Never identify a tile from its shape alone,
   and never loop repeat questions about the same element. For any OTHER unknown icon (gear, items, world map),
   describe the shape and ask once.
4. **Dossier numbers outrank save-computed values** (`save_schema.md`), but
   record which screen and date -- stats change with compounds.

## Screen anatomy

### Agent Dossier (hired variant)
Header: `LOCATION` (display city name, unlike the save's place ids), `ETA`
(`0H` = on site), `STATUS`, buttons `DISMISS / LOCATE / RECALL`. Name line:
CODENAME (real name), optional **star badge** (= player character; see
legend), `HEAT` bar right. `LANGUAGES`. Primary 2x2 grid: **CIRCULATORY /
RESPIRATORY** top, **SENSORY / MOTORIC** bottom (this order = save
`Stat_A-D`, see `save_schema.md`). Derived block: MAX AP / FP / DAMAGE
THRESHOLD / DODGE COST and MAX HP / MOVEMENT RANGE / MAX AWARENESS /
AWARENESS REGEN -- these exist ONLY here; the save serializes them 0.
`EQUIPMENT` (5 slot groups + attachment sub-slots) -- standing rule: never
track or discuss gear; skip the region. `CHARACTER TRAINING`: level + XP bar
`current/needed` (400 XP to L5, 800 to L6, 1600 to L7 observed).
`BACKGROUND` emblem + label. `TRAININGS` icon grid (tiers I-IV; padlock =
locked slot). `PERKS` icon row.

### Agent Dossier (hire-pool variant)
Same body; header instead shows `COST: $N` + `HIRE` button + `HIRE DANGER
+50`. Pool dossier stats are TRUE CURRENT (include baked-in compounds) --
these, not save `Stat_A-D`, are the authority for hire decisions.

### Agent Treatment (Body Engineering facility)
Left: list of compounds AVAILABLE to this agent now (chapter + inventory
gated -- e.g. Ch3 showed only AMPEA/BMA/EPO/Gonadorelin). Selecting one shows
its card: PRICE, DURATION, **REQUIRES COMPOUNDS**, **BLOCKS COMPOUNDS** --
the in-game authority on dependency rules (used 2026-08-21 to restore EPO's
AMPEA prerequisite). **The stat panel up top becomes a PREVIEW with the
selected compound folded in** (green up / red down arrows) -- never read it
as the agent's current stats while a compound is selected. Below: `BODY
ENGINEERING JOBS 0/1` queue; extra slots show `UNAVAILABLE -- REQUIRES
UPGRADE` (facility upgrades).

### Body Engineering: Treatment Complete popup
Shows the 8 derived stats before -> after (green = up, red = down). Does NOT
show the 4 primary stats -- primary confirmation needs the dossier afterwards.
**Known anomaly (n=4 agents): the popup's MAX
AWARENESS "before" reads lower than the same-era dossier by exactly the
compound's delta, i.e. popup-after == dossier-before.** Cause unresolved; do
NOT chain popup Awareness arithmetic with dossier values -- treat the dossier
as the display authority and log both numbers separately.

### Perk Acquisition
4 named perk choices with icons; selected one shows its tooltip. Best source
for confirmed icon+effect pairs -- transcribe all 4 names/icons even if the
player only asks about one.

### MK Ultra: Treatment Complete
`PERKS REMOVED` / `PERKS ACQUIRED` icon lists (e.g. Brainwashing removing the
sleeper-conditioning perk).

### Agent Overview
`ABILITIES` (background-granted, with tooltips) + `PROFICIENCIES` (weapon
cards with names). Paired `BACKGROUND` card states codename + background name.

### Agent List
Rows: CODENAME, `LEVEL N`, status. Status vocabulary observed: AVAILABLE,
AWAY, TRAVELING, CRAFTING, FORGING, TREATMENT, INVESTIGATING, HOSPITALIZED,
TACTICAL TEAM. Chevron+ badge on a row = pending level-up/training point.

### Loadout (mission prep)
Header `LOADOUT` + `LOCATION` + `LANGUAGES`. Squad figures with per-agent
gear strips; support-slot row below (portrait + role icon; `SLOT UNAVAILABLE
-- REQUIREMENTS NOT MET` when locked); `DISTRACT AVAILABLE` indicator.
Top-right buttons: `REMOVE ALL AGENTS`, `REMOVE ALL SUPPORT`, **`MAKE ITEMS
AVAILABLE`** -- the long-unresolved button lives HERE, grouped with the two
bulk-remove actions (context suggests a bulk gear-pooling action; exact
effect still unconfirmed -- `limitations.md` Open research gaps).

## Perk / training / talent icons -- identify from the tooltip

Perk, training, talent and conditioning-marker icons are identified from the
in-game tooltip, not from the picture. A full id-to-name index was extracted
from the game's own text and icon textures (2026-08-26) but is not shipped with
this guide; perk names and effect lines are in `items/abilities.md`, and
anything not there comes from the tooltip. Do not re-derive an icon's meaning
from its shape.

**Common misreads of the old hand-built legend** (kept so the mistakes are not
repeated):

- The **dark shield with a diagonal bar** was listed as "possibly Loyal". It is
  **Masochist** (`intuitionperk_07`, improves Damage Threshold). Loyal is a
  blue-tiled rosette medal and looks nothing like it.
- "**Molecule with `+` = Shock Tacs talent**" was under-specified and would
  have produced wrong answers. That glyph family (head with four linked
  circles) covers five different trainings; the Roman numeral is what picks one
  -- I Contact, II Fire and Movement, III Rapid Dominance, IV Shock, V
  Skirmish. Same for the half-person/half-rifle family and the crossed-rifles
  family.
- The Roman numeral was described as "completed training tier for that training
  line". It is not a tier of one line -- **family plus numeral names a single
  distinct training**. An unread numeral means an unidentified training.
- Several rows were "confirmed (name)" with no effect text. All 31 live perks
  now carry the game's verbatim effect line.

Training tooltips list their granted `ABILITIES` and `PROFICIENCIES`
(Intermediate Firearms Drill -> MU-255, TKB, RP-4; Covert Operations ->
Cobra, Wembley). Weapon names observed on proficiency cards: MPK, MU-255,
TKB, RP-4, AUG, Cobra, Wembley, MG51, Estrella, B76, .45.

**Training id -> display name: resolved 2026-08-26.** All 16 ids
(`training_01` .. `training_16`) were mapped from the game's own text; that
mapping is not shipped, so read the training's name from its in-game tooltip.

Backgrounds observed (emblem + label): CIA, RAF (red star), Gladio (winged
sword shield), Freelance (fedora spy), USMC (globe + anchor), NSA (eagle),
BND (eagle roundel), SEAL, PSIA (wisteria crest), DGI, KGB, Stasi, SAS
(dagger + wings), MSS (hammer + sickle, observed on an agent acquired via
Control Phrase), DGSE (compass rose / star in a ring).
None of SAS's, MSS's or DGSE's granted proficiency/ability is confirmed yet.

**Cabal Control Phrase indicator -- confirmed 2026-08-22 from a dossier screenshot.** A small standalone icon (bottom-left of the perks
block, separate from the perk-slot row) with in-game tooltip verbatim: *"When
encountered during a mission, this agent can be turned with a trigger
phrase."* This is the mechanic-level marker for the Control Phrase ability
(`mechanics.md`) -- it can still show on an agent's dossier after recruitment,
presumably a leftover/informational flag from how the agent was acquired, not a
perk. **Correction:** an earlier pass wrongly said this icon
(and a "dark shield") meant "Loyal" and that the recruited agent had it confirmed via
tooltip -- that was a conflation error, not a real read. Loyal is NOT
confirmed by that observation; the dark-shield icon question above stays open.

**Example Freelance agent's PERKS row -- verified against the game's own extracted text.** The dossier `PERKS` row (4 tiles, L->R) and save reconcile as:
`sprinting figure + speed chevrons` = **Faster Movement**; `crossed revolvers` =
**Expert Marksman**; `assault rifle + green "+" + III` = the **Advanced Firearms**
training talent (tier III, tied to `training_09` = Advanced Firearms Drill);
`downward shield + gold "+"` = **Mild Paranoia** (`intuitionperk_02`) --
**NOT Loyal**. Save cross-check: `levelupperks` is EMPTY and `inflperks=0`, so none
of these are level-up picks -- they are background/training-granted, which is why
they show without a level-up choice logged. The agent's one ability is `AbilityRestoreAwareness`
= **Warn Ally** (Freelance). An earlier card had invented "Rifle Training"
and "Loyal" for this agent from icon shape; both were wrong and are retracted. **Lesson:
match the PERKS row against the tooltip + the save before writing any perk onto a
card; never name a perk from icon shape alone (the standing rule this violated).**

Open identification targets (perk/training/talent icons are no longer among
them): SAS and MSS background ability
grants; the derived-stat dips seen across 6 agents' Bolasterone applications
2026-08-22 (five agents, including Lamster: HP and/or Max
Awareness down; a sixth agent: Max Awareness held steady but Dodge Cost and
Awareness Regen dipped instead) -- not yet explained.

**Claim needing re-check after the 2026-08-26 extraction:** earlier notes called a "red masked figure" the *sleeper-conditioning marker*
(observed on two agents; removed from a third by Brainwashing). The extracted assets
show the red-tinted head markers are the Beholder set -- Beholder Control
Phrase, Beholder Mole, and the Beholder Mason Gambit variant -- and the game
also defines a Beholder Sleeper Agent whose own texture was not found. So the
family (Beholder conditioning) is right, but WHICH of them was never confirmed
by tooltip. Do not restate "sleeper" as settled; capture the tooltip next time
one appears.
