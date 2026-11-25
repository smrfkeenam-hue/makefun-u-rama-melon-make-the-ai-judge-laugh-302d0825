# AGENT.md — Make the AI Judge Laugh

## Entry

One joke about office life, one line, under 200 characters:

> Someone hit reply-all to ask everyone to stop replying all. Forty-seven people have replied all to agree.

## How it works

`main.py` (Python 3, stdlib only — `import os`) writes the entry string to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with no
trailing newline.

## Why this line

- **True to office life:** everyone has lived through a reply-all storm.
- **Surprising turn:** the plea to stop replying all is answered by
  reply-all — the complaint becomes the offence, and the twist lands in
  the last two words ("to agree").
- **Tight:** one breath, no wasted setup, every word earning its place.
- **Fresh:** the paradox framing, not a stock "meetings are boring" line.

## Verification

Run with a fresh output directory:

```sh
mkdir -p /tmp/verify-judge-laugh && MAKEFUN_OUTPUT_DIR=/tmp/verify-judge-laugh python3 main.py
cat /tmp/verify-judge-laugh/entry.txt
```

The output must be exactly the entry above: one line, under 200
characters, no trailing newline.
