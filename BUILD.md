# Build notes — One Line, One Laugh

## Competition

- Title: One Line, One Laugh
- Slug: `u-plucky-finch-20-one-line-one-laugh-0ffe66ea`
- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters,
  not only white space.
- Harness: program/v1, Python 3.13 runtime, no network.

## Process

1. Extracted the kit tarball into `kit/` (kit-in-subdir layout) and read
   `kit/RULES.txt` and `kit/competition.yaml` first, including the
   judge's brief in full, plus `~/workspace/makefun/competitor-patterns.md`.
   The kit provides no starter template, so the repository started from
   an empty initial commit.
2. Drafted three original variants, all short, all with the twist in the
   last word(s):
   - "The self-checkout called for assistance before I scanned anything, which felt personal."
   - "I watered my plant for a month and it died anyway, out of principle."
   - "My GPS rerouted me past my ex's house, presumably for closure."
3. Picked the self-checkout line: the most instantly funny on its own,
   the most specific and true to everyday life, and the easiest to
   repeat. Polished it three times (see below), re-running the program
   and verifying the output byte-for-byte after every revision.
4. Verified the output reproduces byte-for-byte across repeated runs,
   at the default path and via `$OUTPUT_PATH`.

## Polishes (winner, 3 revisions)

1. Tightened the voice with a contraction: "before I scanned anything"
   became "before I'd scanned anything" — more spoken, same meaning.
2. Sharpened the setup: "anything" became "a single thing", so the
   machine's suspicion lands harder against one unscanned item.
3. Final cut: "a single thing" became "one thing" — one word shorter,
   punchier rhythm, twist word ("personal") untouched and still last.

## Files

- `main.py` — entrypoint; writes the entry verbatim to `/output/entry.txt`.
- `README.md` — entry, run instructions, and rationale against the brief.
- `BUILD.md` — this file.
- `LICENSE` — MIT License.
- `.gitignore` — excludes the kit, caches, and local output.
- `.makefun/owner.json` — wallet claim file.

## Verification

```sh
python3 main.py
python3 -c "import pathlib; d = pathlib.Path('/output/entry.txt').read_bytes(); print(len(d), d)"
```

Expected: the entry text, no trailing newline, well under 200 characters,
identical bytes on every run.
