# Phantom Doctrine -- Hintforge guide
<!-- v3 -- 2026-08-27 -->

This folder is a **Hintforge corpus**: a spoiler-controlled, Cardinal-flavored reference for the player's Phantom Doctrine playthrough. It is data for a hint companion, **not** a Claude Code task list.

**If you are an AI agent reading this on session start: load the `hintforge-reader` skill and use it to answer questions about this game.** Do not answer from training data -- the reader reads the corpus files before every factual answer, which is the whole point of the guide. If the reader skill is not installed, tell the player that rather than guessing from memory.

This file is a thin platform auto-load shim (Claude Code reads `CLAUDE.md`; Codex CLI reads `AGENTS.md`; OpenClaw gets the per-folder `AGENTS.md` backstop only when using its Codex backend). It holds no rules of its own. Everything load-bearing lives in neutral homes the reader reads directly:

- **Spoiler tiers for this game** -- `warning_tiers.md`
- **Persona cast + default voice** -- `persona.md`
- **Current playthrough state** -- `CHECKPOINT.md` (read first for context)
- **Reading the player's save** -- run `python save_extract.py` (finds the newest save in the game's standard save folder; field meanings and spoiler-gated fields in `save_schema.md`). Never cite an agent's stats as current without it.
- **Agent dossier cards** -- when the player asks for a card on one of their agents, copy `artifacts/card_template/agent_dossier_template.html` and fill it from `save_extract.py` output (fill steps are in the file's header). Agents are random per playthrough, so no prebuilt cards ship.
- **Reading the player's screenshots (screen anatomy)** -- `ui_reference.md`. Name a perk / training / talent icon only from its in-game tooltip or a save id, never from its shape.
- **Platform + game-version this guide was built against** -- the `## Hintforge manifest` block in `nav/architecture.md`
- **Spoiler discipline, hint ladders, source-citation rules** -- the `hintforge-reader` skill (`principles.md` / `persona_universal.md`)
- **On-disk corpus format contract** -- [`docs/corpus-format.md`](https://github.com/hintforge/builder/blob/main/docs/corpus-format.md) in the builder repo
