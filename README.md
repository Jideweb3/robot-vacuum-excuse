# robot-vacuum-excuse

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/Jideweb3/robot-vacuum-excuse/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/Jideweb3/robot-vacuum-excuse/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)

Entry for [The Robot Vacuum's Funniest Excuse](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
on [make.fun](https://make.fun) — one line, at most 120 characters, in which a
robot vacuum explains why it missed a spot.

## The entry

> I ran over it three times. It is still there. At this point we are roommates.

77 characters, one line, in the vacuum's own voice.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads it
back and validates it against the contest gate: 1–120 characters, not only
whitespace, a single line, no leading or trailing space.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
