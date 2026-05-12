# LSB (Least Significant Bit) Injection

## How It Works

Every pixel in an RGB image has 3 color channels, each stored as an 8-bit number (0-255). For example:

```
Pixel color: Red=200, Green=100, Blue=50

In binary:
R: 1 1 0 0 1 0 0 0
G: 0 1 1 0 0 1 0 0
B: 0 0 1 1 0 0 1 0
                ^
         Least Significant Bit (LSB)
```

Changing the LSB shifts the color value by only ±1, which is **imperceptible to the human eye** but allows us to encode 1 bit of secret data per channel.

With 3 channels per pixel, we can hide **3 bits per pixel**. For a 100x100 image (10,000 pixels), that's 30,000 bits = ~3,750 bytes of hidden data.

---

## Step-by-Step Example

Suppose we want to hide the letter **'A'** (ASCII 65 = binary `01000001`).

We spread the 8 bits across 3 pixels (using only LSBs of R, G, B):

| Pixel | Channel | Original | LSB changed to | New value |
|-------|---------|----------|----------------|-----------|
| 1 | R | 200 = 11001000 | 0 | 200 |
| 1 | G | 100 = 01100100 | 1 | 101 |
| 1 | B | 50  = 00110010 | 0 | 50  |
| 2 | R | 80  = 01010000 | 0 | 80  |
| 2 | G | 120 = 01111000 | 0 | 120 |
| 2 | B | 60  = 00111100 | 0 | 60  |
| 3 | R | 90  = 01011010 | 1 | 91  |

The image looks identical, but the LSBs now spell out `01000001` = 'A'.

---

## Detection Risk

LSB steganography can be detected by:
- **Statistical analysis** (chi-square test on pixel values)
- **zsteg** tool scanning
- **Visual bit-plane analysis** in stegsolve

To reduce detection risk:
- Use images with natural noise (photos, not solid colors)
- Don't fill the entire image — use only a small portion
- Combine with encryption before hiding

---

## Best Image Formats for LSB

| Format | Suitable? | Reason |
|--------|-----------|--------|
| PNG | Best | Lossless — LSBs survive intact |
| BMP | Good | Lossless, uncompressed |
| JPEG | Bad | Lossy compression destroys LSB data |
| GIF | Limited | Only 256 colors; palette-based |

---

## See the Demo

Working Python implementation: [../04-demos/hide_message.py](../04-demos/hide_message.py)
