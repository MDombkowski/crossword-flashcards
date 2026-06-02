#!/usr/bin/env python3
"""Generate maskable PWA icons: a crossword-grid motif on a blue field.
Pure stdlib (zlib + struct), no PIL required."""
import zlib, struct

BG   = (37, 99, 235)    # blue field (#2563eb)
WHITE= (255, 255, 255)
BLACK= (17, 24, 39)     # near-black cells (#111827)

# 5x5 crossword pattern: 1 = black (blocked) cell, 0 = white (fillable) cell
PATTERN = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0],
]

def make_png(size, path):
    grid_cells = 5
    # grid occupies center ~64% (well inside the maskable safe zone)
    grid_px = int(size * 0.64)
    cell = grid_px // grid_cells
    grid_px = cell * grid_cells
    origin = (size - grid_px) // 2
    gap = max(1, size // 128)  # thin gutter between cells

    rows = []
    for y in range(size):
        row = bytearray()
        for x in range(size):
            px = BG
            gx, gy = x - origin, y - origin
            if 0 <= gx < grid_px and 0 <= gy < grid_px:
                cx, cy = gx // cell, gy // cell
                ix, iy = gx % cell, gy % cell
                if ix >= gap and iy >= gap:  # inside a cell, leaving a gutter
                    px = BLACK if PATTERN[cy][cx] else WHITE
            row += bytes(px)
        rows.append(row)

    raw = bytearray()
    for row in rows:
        raw.append(0)        # filter type 0 (None) per scanline
        raw += row

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xffffffff)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)  # 8-bit, RGB
    idat = zlib.compress(bytes(raw), 9)
    with open(path, "wb") as f:
        f.write(sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", idat) + chunk(b"IEND", b""))
    print("wrote", path, size, "x", size)

make_png(192, "icon-192.png")
make_png(512, "icon-512.png")
