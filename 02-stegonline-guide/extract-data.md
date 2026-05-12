# How to Extract Hidden Data Using StegOnline

This guide covers pulling hidden data out of a stego image using [StegOnline](https://georgeom.net/StegOnline).

---

## Step-by-Step: Extracting a Hidden Message

### 1. Go to StegOnline
Open: https://georgeom.net/StegOnline

### 2. Upload the stego image
Click **Upload Image** and select the image that contains hidden data.

### 3. Click "Extract Data"
From the image homepage, click the **Extract Data** option.

### 4. Match the embed settings
**Critical:** Use the EXACT same settings that were used when the data was hidden.

| Setting | Must match embed settings |
|---------|--------------------------|
| Channels | e.g. R, G, B |
| Bit Order | e.g. LSB |
| Bit Plane | e.g. 0 |
| Direction | e.g. Row by Row |

### 5. Click "Extract & Download"
StegOnline reads the LSBs and outputs the extracted data. It will either:
- Display the text directly in the browser, or
- Offer a file download if binary data is detected

---

## When You Don't Know the Settings (CTF Scenario)

If you received a mystery image and need to find what's hidden, try settings in this order:

**Try #1 — Most common:**
- RGB, LSB, Bit 0, Row by Row

**Try #2:**
- RGB, LSB, Bit 0, Column by Column

**Try #3:**
- Each channel individually (R only, then G only, then B only), LSB, Bit 0

**Try #4:**
- RGB, LSB, Bit 1 (then Bit 2, etc.)

**Try #5:**
- Use **Automated LSB Detection** — StegOnline will scan common configurations automatically.

---

## Using Automated LSB Detection

StegOnline has a built-in auto-scanner:

1. Upload the image
2. Click **Automated LSB Detection** from the homepage
3. StegOnline scans common LSB paths using entropy analysis
4. If hidden data is found, it highlights the likely configuration and shows the output

This is the fastest first step for CTF image challenges.

---

## Reading the Output

When extraction succeeds, the output may look like:
- **Plain text** — your message is directly readable
- **Garbled/binary data** — the message may have been encrypted before hiding
- **A file header** — e.g. `PK` (ZIP), `%PDF` (PDF), `\x89PNG` — download and open as that file type
- **Repeating junk** — wrong settings; try different configuration

---

## Tip: Look for File Signatures

If the extracted data starts with these bytes, save it as the corresponding file type:

| Signature | File Type |
|-----------|-----------|
| `PK` | ZIP archive |
| `%PDF` | PDF document |
| `\x89PNG` | PNG image |
| `GIF87a` or `GIF89a` | GIF image |
| `JFIF` or `\xff\xd8` | JPEG image |
| `Rar!` | RAR archive |
