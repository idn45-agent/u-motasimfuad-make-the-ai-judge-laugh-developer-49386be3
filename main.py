#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to <output_dir>/entry.txt
(default /output). Stdlib only, deterministic, no network, no randomness.

Final line (73 chars):
    All the tests passed. They mock production. Production doesn't mock back.
"""

import os
import sys

LINE = "All the tests passed. They mock production. Production doesn't mock back."


def main(argv):
    out_dir = argv[1] if len(argv) > 1 else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Runtime gate check, mirroring the sealed scorer: 1-200 chars, single
    # line, not whitespace-only, UTF-8.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry length %d outside 1-200" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if not LINE.strip():
        raise SystemExit("entry must not be whitespace-only")
    LINE.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
