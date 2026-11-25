# The Funniest Office Joke, Judged Head to Head

[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Xutep/makefun-u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Xutep/makefun-u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

Entry for the [make.fun bounty "The Funniest Office Joke, Judged Head to Head"](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c).

## What it does

`main.py` (Python 3, standard library only) writes one single-line joke
about office life to `/output/entry.txt`. The joke is 122 characters,
one line, with the punchline last:

> My boss said his door is always open, so I walked in and asked for a raise — the door was open, but the budget was closed.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program validates its own output before writing: non-empty, at most
200 characters, a single line, and it reads the file back to confirm what
was written matches what was validated.
