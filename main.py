"""Cutest picture entry: a baby otter pup hugging a baby duckling.

A deterministic copier. The picture itself is stored beside this script as
cute.png (a JPEG file named .png, as the competition rules allow, told apart
by its first bytes). Running this program copies it unchanged to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), verifying the
copy byte-for-byte so the output is always identical to the source.
"""

import os
import shutil
import sys

SOURCE_NAME = "cute.png"
JPEG_MAGIC = b"\xff\xd8\xff"
JPEG_END = b"\xff\xd9"
MAX_BYTES = 1048576


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    size = os.path.getsize(source)
    if size == 0:
        print(f"error: source image is empty: {source}", file=sys.stderr)
        return 1
    if size > MAX_BYTES:
        print(f"error: source image {size} bytes exceeds 1 MiB limit",
              file=sys.stderr)
        return 1

    with open(source, "rb") as fh:
        head = fh.read(3)
    if head != JPEG_MAGIC:
        print("error: source image is not a JPEG (bad magic bytes)",
              file=sys.stderr)
        return 1
    with open(source, "rb") as fh:
        fh.seek(-2, os.SEEK_END)
        tail = fh.read(2)
    if tail != JPEG_END:
        print("error: source image is not a complete JPEG (bad end marker)",
              file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, dest)

    if os.path.getsize(dest) != size:
        print("error: copied size does not match source", file=sys.stderr)
        return 1
    with open(source, "rb") as a, open(dest, "rb") as b:
        if a.read() != b.read():
            print("error: copied bytes do not match source", file=sys.stderr)
            return 1

    print(f"wrote {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
