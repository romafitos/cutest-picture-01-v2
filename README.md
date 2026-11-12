# Cutest Picture — Baby Otter Hugging a Baby Duckling

A 3D-rendered picture of a baby otter pup hugging a baby duckling: huge
sparkling eyes, a head tilt, and a tiny pink bow. The image is stored in
this directory as `cute.png` (a JPEG file named `.png`, as the competition
rules allow, told apart by its first bytes).

## How it works

`main.py` is a deterministic copier written in Python 3.13 using only the
standard library. It copies `cute.png` unchanged to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), checking
that the source is a non-empty JPEG under 1 MiB with a valid start and end
marker, then verifying the copy is byte-for-byte identical to the source.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The output `entry.png` is byte-identical to `cute.png` on every run.
