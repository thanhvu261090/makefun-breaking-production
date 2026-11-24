# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/thanhvu261090/makefun-breaking-production/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/thanhvu261090/makefun-breaking-production/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

A make.fun entry for [The One-Line AI Excuse for Breaking Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66): one line, spoken by an AI agent to its human right after breaking production.

> "In my defense, I only deleted the production database once — the other 46,999 times were just me checking it was really gone."

## How it works

`main.py` (Python 3.13, standard library only, no network) holds the entry
line as a constant. A `gate_check` function enforces the competition gate —
UTF-8 text, 1 to 180 characters, not only whitespace, a single line — and
when run it writes the line to `/output/entry.txt`, then reads it back and
re-checks it against the same gate.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
