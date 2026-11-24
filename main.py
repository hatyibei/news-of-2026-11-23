#!/usr/bin/env python3
"""Entry program for make.fun's "Sum up 23 November's world news in one
image" bounty (news-image-20261123).

Writes the repository's pre-drawn front page, entry.png, to the output
directory as entry.png. Standard library only, no network, and a plain
byte copy, so every run writes exactly the same bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
