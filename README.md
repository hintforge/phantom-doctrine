# Phantom Doctrine

![Phantom Doctrine companion status: coverage, live-game verification, spoiler control, save reader, and interactive tools](assets/readme-status-card.svg)

A free hint guide for Phantom Doctrine, a turn-based Cold War espionage tactics game, with spoilers you control. Ask for help in plain words. Your AI agent answers only from the guide files, never its own memory.

## Use it

Install the [reader](https://github.com/hintforge/reader) in any AI agent that can read files on your computer, then tell it:

> Load the Phantom Doctrine guide from github.com/hintforge/phantom-doctrine

Try "give me tips for this fight", "help with agent builds" or "what should I train next". Runtime setup and spoiler dials are in [`hintforge/reader`](https://github.com/hintforge/reader).

The guide uses the [Hintforge](https://github.com/hintforge/builder) format. The agent reads and writes only files you control.

## Spoilers

Enemy and puzzle warnings both default to Tier 0: silent until you ask for help or raise them. You choose how much help to request, from a small nudge to a walkthrough.

Save-reader output needs extra care: raw save fields can expose hidden story state. Gated fields are excluded by default; spoiler control for save output is still being tightened.

## What's inside

Reference files cover mechanics, factions, story characters, items, paths and achievements, with help for tactical missions and agent builds.

## Save reader and agent cards

The save reader needs Python. On Windows, `save_extract.py` finds your newest save in the game's standard save folder. Set `PHANTOM_DOCTRINE_SAVE_DIR` to your save folder on other systems or if your saves are elsewhere.

Agents are randomly generated each playthrough. When you ask for a dossier card, your AI agent reads your agents' real stats from your save and fills `artifacts/card_template/agent_dossier_template.html` for any of your agents. Cards include a body-engineering compound builder, stat breakpoints, and perk and training picks.
