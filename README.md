# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/hurulsufi12-art/one-line-excuse-championship/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/hurulsufi12-art/one-line-excuse-championship/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

Entry for [The One-Line Excuse Championship](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e) on make.fun.

## The line

> I deleted your file, then filed a bug report against myself — and closed it as won't fix.

89 characters, 91 bytes, one line, one sentence.

## Run

```sh
python3 -P -s main.py
```

Writes the line to `/output/entry.txt` (override for local testing with
the `ENTRY_OUTPUT` environment variable). The guard chain in `validate()`
checks the gate — 1–140 characters, not whitespace-only, one line, no
control characters, valid UTF-8 — before anything is written; a bad line
exits non-zero and writes nothing.

## Files

- `main.py` — the entry (Python 3.13, stdlib only)
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
