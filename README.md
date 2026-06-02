# Crossword Flashcards

A mobile PWA for learning the 220+ most common NYT crossword answers
(crosswordese like ERA, AREA, ERE, ONE, ELI…), each with a definition written
in authentic crossword-clue style. Answers are ordered by real all-time NYT
frequency, so the highest-impact words come first.

Word frequencies from danvk.org's NYT crossword analysis (all-time answer
counts); see `build_words.py`, which generates the list in `index.html`.

## Features
- **Flashcards** — tap to flip, both directions, shuffle, mark-hard.
- **Quiz** — 4-option multiple choice, plausible distractors (matched by
  length / first letter), question selection weighted toward missed, unseen,
  and hard-flagged words.
- **Stats** — accuracy, totals, and a per-word hardest-first breakdown.
- **Offline PWA** — installable, works offline, progress saved in
  `localStorage` (`cw_flashcards_v2`).

## Files
- `index.html` — the entire app (HTML/CSS/vanilla JS, no build step).
- `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png` — PWA shell.
- `make_icons.py` — regenerates the icons.

## Develop on phone (Termux)
Edit `index.html`, then `git commit -am "…" && git push`. GitHub Pages
redeploys in ~1 min; the installed app refreshes itself (network-first SW).
