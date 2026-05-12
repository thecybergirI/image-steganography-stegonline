# StegOnline Interface Overview

**Tool URL:** https://georgeom.net/StegOnline

---

## Step 1: Upload Your Image

Go to [StegOnline](https://georgeom.net/StegOnline) and upload any image file (PNG, BMP, or JPEG). PNG is recommended because it is lossless — LSB data won't be destroyed by compression.

Once uploaded, you are taken to the **Image Homepage**.

---

## Step 2: The Main Menu

After uploading, you will see a panel with the following options:

| Option | What It Does |
|--------|--------------|
| **Embed Data** | Hide text or a file inside the image using LSB |
| **Extract Data** | Pull out hidden data from an image |
| **Browse Bit Planes** | View each individual bit layer of the image visually |
| **Hide Image** | Embed one image inside another image's bit plane |
| **PNG Chunk Info** | View the raw PNG chunk structure and metadata |
| **Download RGBA** | Export pixel RGBA values as a CSV |
| **Colour Palette** | Browse/randomize the colour palette (for GIF/indexed images) |
| **Automated LSB Detection** | Auto-scan for hidden data using entropy analysis |

---

## Step 3: The LSB Settings Table

When you click **Embed** or **Extract**, you will see a settings table. This is the most important part of StegOnline. The options are:

### Colour Channels
Select which channels to use for hiding data:
- **R** — Red channel
- **G** — Green channel
- **B** — Blue channel
- **A** — Alpha (transparency) channel

You can use one, two, or all three RGB channels.

### Bit Order
- **LSB** (Least Significant Bit) — hides data in the last bit; minimal visual change. Most common.
- **MSB** (Most Significant Bit) — hides data in the first bit; causes visible distortion. Rarely used.

### Bit Plane (0–7)
Selects *which* bit position to use (0 = least significant, 7 = most significant).
- Bit 0 is the default and least detectable.
- Higher bit planes cause more visible image distortion.

### Read Direction
- **Row by Row** (left to right, top to bottom) — standard
- **Column by Column**

---

## Key Rule

> **The settings used to EMBED data must exactly match the settings used to EXTRACT data.**
> If you embed using RGB, LSB, Bit 0 — you must extract with RGB, LSB, Bit 0.

---

## Recommended Default Settings (for beginners)

| Setting | Value |
|---------|-------|
| Channels | R, G, B |
| Order | LSB |
| Bit Plane | 0 |
| Direction | Row by Row |

This is the most common configuration and the first thing to try when solving CTF challenges.
