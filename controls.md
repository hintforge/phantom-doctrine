# Phantom Doctrine -- Controls Reference

**status:** research-integrated
**last_reconciled:** 2026-08-18

Default PC (mouse + keyboard) bindings. All bindings are rebindable in-game: **Options -> Interface -> Edit bindings.** If a binding below doesn't match what you see on screen, trust the in-game menu over this file and flag it -- patches have changed keys before.

## Global / menu

| Key | Action |
|---|---|
| `Esc` | Return to previous screen |
| `P` | Game menu |
| `M` | Open World Map |
| `B` | Open Investigation (conspiracy) Board |
| `Tab` | Next item |
| `Space` | Strategic map pause / accept on tactical map |
| `F5` | Quick save |
| `F9` | Quick load |

_source: deep-research P1 2026-08-18 (gamepressure) · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 3 sources]

## Tactical (mission) map

| Key | Action |
|---|---|
| `1`-`7` | Select ability slot |
| `1`-`8` | Select agent in current squad |
| End Round | ends the active agent's turn |
| Floor up/down | change visible floor level |
| Mouse wheel | Zoom camera |
| Camera | rotate/pan (see note below) |

_source: deep-research P1 2026-08-18 (gamepressure) · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 3 sources]

**Unverified overlap (carried from Stage 0, not resolved by P1):** the source guide lists `E` for both "end round" and "rotate camera" -- these are likely two different bindable actions that happen to share a key in the source's table formatting, not an actual in-game conflict. Confirm against your own Options -> Interface -> Edit bindings screen and correct this entry once verified from a live session.

## Facility management -- confirmed: no dedicated per-facility hotkeys

**Facility-hotkey request outcome (P1 resolves the Stage-0 standing lead):** the Steam thread requesting dedicated hotkeys for Analytics / Crew Quarters / Forger / Workshop / Infirmary was answered by a developer noting that only the World Map (`M`) shortcut exists -- **dedicated per-facility hotkeys did NOT ship.** Players must navigate the hideout screen manually (mouse click on each facility icon).

_source: deep-research P1 2026-08-18 (Steam Community discussion thread) · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ [Confirmed: 3 sources]

## Common remaps players make

Not surfaced by P1 research -- no notorious control-scheme friction found beyond the facility-hotkey request above. Revisit if in-play sessions turn up real friction points.

## Known issue: attack freezes on the cutscene, shooter never fires

Multiple Steam Community bug-report threads describe combat freezing mid-animation/cutscene, most commonly tied to a specific AI action interrupting the kill-cam (one reported case: an enemy walking to reactivate a camera station froze the fight until that agent was shot down first, before the freeze occurred). No single universal trigger is confirmed -- treat any attack-cutscene hang as this same bug family rather than a one-off.

**What to do:**
1. **Set `ActionCamera=False` in the ini.** Edit `%LOCALAPPDATA%\PhantomDoctrine\Saved\Config\WindowsNoEditor\PD_GameOptions.ini` (back it up first) and add/set `ActionCamera=False`. This setting has resolved a reload-persistent freeze -- the kill-cam itself appears to be the trigger. Treat this as the primary fix, not one item in a bundle.
2. Optionally also set the rest of the pacing bundle if you want faster turns generally: `DisableDeployAnim=True` (removes infiltration/exfil cutscenes), `Gameplay_SkipBodyDisposalAnimation=True`, `FastMoveAnim=True`, `InstantWorldmap=True`. These weren't needed for the freeze fix specifically and remain untested in isolation; community reports describe them as safe alongside `ActionCamera=False`.
3. **If already frozen right now:** `Alt+F4`, relaunch, load your most recent save -- this clears an active freeze but doesn't prevent the next one; set `ActionCamera=False` afterward so it doesn't recur. `F5`/`F9` quicksave/quickload (see Global/menu table above) keeps the loss small if you save often.
4. If it still recurs after `ActionCamera=False`, Creative Forge's support address (seen in other bug threads) is `support@creativeforge.pl`.

The same symptom can occur without a known trigger: a burst-shot animation may start without firing, or Overwatch may fail to fire and leave an infinite "Enemy turn" loop. This appears to be a general animation-state bug with multiple possible causes.

**Target-persistent variant:** a freeze can follow the target rather than the shooter, recurring after a reload even when a different squad agent attacks the same enemy. `ActionCamera=False` in `PD_GameOptions.ini` has allowed normal attacks on such a target. This supports the kill-cam/action-camera sequence as a likely trigger; disabling it is the primary fix above.

_source: Steam Community "Phantom Doctrine Bug Reports" thread; Steam Community "Devs, can we skip anim?" thread, user Jhonny G's ini workaround; in-game confirmation of the target-persistent fix · capture: web_fetch + manual_paste · confidence: medium (general freeze reports, community workarounds rather than official patch notes) / high (`ActionCamera=False` as fix for the observed target-persistent variant) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Sources

- [Phantom Doctrine PC Controls -- GamePressure](https://www.gamepressure.com/phantom-doctrine/controls/z0b365)
- [Steam Community -- facility hotkey discussion](https://steamcommunity.com/app/559100/discussions/0/1736589520006699476/)
