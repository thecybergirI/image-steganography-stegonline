# CTF Image Steganography Checklist

A step-by-step checklist for analyzing a mystery image in a CTF challenge. Work through these in order.

---

## Phase 1: Basic Recon (Before Any Tools)

- [ ] Note the file extension — is it actually what it claims to be?
- [ ] Check the file size — unusually large for the image dimensions?
- [ ] Open the image — does it look normal, or distorted?
- [ ] Read the challenge description — any hints about the tool or technique?

---

## Phase 2: StegOnline Checks

Go to [https://georgeom.net/StegOnline](https://georgeom.net/StegOnline) and upload the image.

### 2.1 — Automated Detection (try first)
- [ ] Click **Automated LSB Detection**
- [ ] Review all flagged configurations
- [ ] Check if any output looks like a flag or readable text

### 2.2 — Extract with Common Settings
Try each of these extract configurations in order:

| # | Channels | Order | Bit Plane | Direction |
|---|----------|-------|-----------|-----------|
| 1 | R, G, B | LSB | 0 | Row by Row |
| 2 | R, G, B | LSB | 0 | Column by Column |
| 3 | R only | LSB | 0 | Row by Row |
| 4 | G only | LSB | 0 | Row by Row |
| 5 | B only | LSB | 0 | Row by Row |
| 6 | R, G, B | LSB | 1 | Row by Row |
| 7 | R, G, B | MSB | 0 | Row by Row |

- [ ] For each attempt, look for: readable text, CTF flag format (`CTF{...}`), or a file header

### 2.3 — Browse Bit Planes
- [ ] Click **Browse Bit Planes**
- [ ] Check R, G, B bit plane 0 — is there a visible pattern instead of noise?
- [ ] Check bit planes 1 and 2 as well
- [ ] Look for hidden images embedded in a bit plane

### 2.4 — PNG Chunk Info
- [ ] Click **PNG Chunk Info** (PNG files only)
- [ ] Look for unusual or extra chunks (e.g. `tEXt`, `zTXt`, custom chunks)
- [ ] Read any text chunks for embedded messages

### 2.5 — Colour Palette (for GIF or indexed images)
- [ ] Click **Colour Palette**
- [ ] Try randomizing to see if a hidden image appears

---

## Phase 3: Quick Output Interpretation

When you get extract output, look for:

| Output looks like... | What to do |
|----------------------|------------|
| `CTF{...}` or flag text | You found it! |
| Readable English text | Read it — may contain hints |
| `PK` at start | Save as `.zip` and unzip |
| `\x89PNG` at start | Save as `.png` and open |
| `%PDF` at start | Save as `.pdf` and open |
| Random garbled bytes | Try different settings, or data may be encrypted |
| All zeros or all ones | Wrong settings |

---

## Reminder

> If none of these work, the challenge may use a different technique (metadata, appended files, audio steganography, etc.). StegOnline covers LSB — for broader analysis, try `binwalk`, `exiftool`, or `strings` on the file.
