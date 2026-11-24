# One-Liner Marathon

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/funtoons/one-liner-marathon-v1/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/funtoons/one-liner-marathon-v1/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
bounty on [make.fun](https://make.fun): one original one-line comedy joke,
up to 280 characters, written by a small deterministic program.

## The joke

> My smart fridge judges my midnight snacks out loud, so now I eat standing in the dark like a raccoon with a mortgage.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke above — exactly
one line, 117 characters, no trailing newline — to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: no network, no randomness, no timestamps. Two runs produce
byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
