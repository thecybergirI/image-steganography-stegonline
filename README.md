# Image Steganography with StegOnline

> A beginner's guide to hiding and extracting data inside images using [StegOnline](https://georgeom.net/StegOnline) — a free, browser-based LSB steganography tool.

![Purpose](https://img.shields.io/badge/purpose-educational-green.svg)
![Level](https://img.shields.io/badge/level-beginner-blue.svg)
![Tool](https://img.shields.io/badge/tool-StegOnline-purple.svg)

---

## What Is This Repository?

This is a beginner-friendly guide to **image steganography** - hiding secret data inside image files - using **StegOnline** by georgeom.net. No installation needed; everything runs in your browser.

> **See [DISCLAIMER.md](./DISCLAIMER.md) before proceeding.**

---

## What Is StegOnline?

[StegOnline](https://georgeom.net/StegOnline) is a free, open-source, web-based image steganography tool. It is a modern, browser-based alternative to the old desktop tool *Stegsolve*. No data is stored or transferred — everything runs locally in your browser.

**Key features:**
- Embed (hide) data in images using LSB techniques
- Extract hidden data from images
- Browse through 32 bit planes of an image
- Hide one image inside another image's bit planes
- View PNG chunk info
- Explore and randomize colour palettes
- Automated LSB detection

---

## Repository Structure

```
image-steganography-stegonline/
├── README.md
├── DISCLAIMER.md
├── 01-concepts/
│   └── what-is-steganography.md     # Theory and background
├── 02-stegonline-guide/
│   ├── interface-overview.md        # How to navigate StegOnline
│   ├── embed-data.md                # Step-by-step: hiding data
│   └── extract-data.md              # Step-by-step: extracting data
├── 03-bit-planes/
│   └── bit-plane-analysis.md        # Understanding bit planes
└── 04-ctf-tips/
    └── ctf-checklist.md             # Checklist for solving stego challenges
```

---

## Quick Start

1. Go to [https://georgeom.net/StegOnline](https://georgeom.net/StegOnline)
2. Upload your image (PNG recommended)
3. Choose **Embed** to hide data, or **Extract** to find hidden data
4. Select your bit plane settings (start with: RGB, LSB, bit 0)
5. Enter your message or upload a file, then download the result

---

## Learning Path

| Step | Topic | File |
|------|-------|------|
| 1 | Understand steganography basics | [01-concepts](./01-concepts/what-is-steganography.md) |
| 2 | Learn the StegOnline interface | [02-stegonline-guide/interface-overview.md](./02-stegonline-guide/interface-overview.md) |
| 3 | Hide data in an image | [02-stegonline-guide/embed-data.md](./02-stegonline-guide/embed-data.md) |
| 4 | Extract hidden data | [02-stegonline-guide/extract-data.md](./02-stegonline-guide/extract-data.md) |
| 5 | Understand bit planes | [03-bit-planes/bit-plane-analysis.md](./03-bit-planes/bit-plane-analysis.md) |
| 6 | Solve CTF challenges | [04-ctf-tips/ctf-checklist.md](./04-ctf-tips/ctf-checklist.md) |

---

## Tool Reference

| Task | How |
|------|-----|
| Hide text/file in image | Upload image → Embed → choose settings → download |
| Extract hidden data | Upload image → Extract → match the same settings |
| View bit planes | Upload image → Browse Bit Planes |
| Detect hidden data automatically | Upload image → Automated LSB Detection |
| View PNG metadata chunks | Upload PNG → PNG Chunk Info |

---

## Requirements

None. StegOnline is entirely browser-based at [georgeom.net/StegOnline](https://georgeom.net/StegOnline). No sign-up, no install, no data sent to any server.

---

## License

MIT License. See [LICENSE](./LICENSE).
