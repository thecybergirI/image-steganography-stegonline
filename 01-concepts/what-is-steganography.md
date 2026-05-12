# What is Steganography?

## Definition

**Steganography** is the practice of hiding secret information within an ordinary, non-secret file so that the existence of the hidden data is concealed. The word comes from Greek: *steganos* (covered) + *graphia* (writing).

Unlike **encryption** (which scrambles data so it can't be read), steganography **hides the very existence** of the data.

---

## Steganography vs. Cryptography

| Feature | Steganography | Cryptography |
|--------|---------------|--------------|
| Goal | Hide *existence* of data | Hide *meaning* of data |
| Output | Looks like a normal file | Looks like scrambled data |
| Detection | Hard to detect | Easy to detect, hard to read |
| Example | Message hidden in image pixels | AES-encrypted message |

> Best practice: Combine both — encrypt your message first, then hide it inside an image.

---

## How Images Store Data

Digital images are made of **pixels**. Each pixel in an RGB image has 3 channels:
- **R**ed (0–255)
- **G**reen (0–255)
- **B**lue (0–255)

Each channel is an **8-bit binary number**. Example — color `(200, 100, 50)`:
```
R: 11001000
G: 01100100
B: 00110010
```

The **least significant bit (LSB)** is the rightmost bit. Changing it barely affects the color visually — this is the foundation of LSB steganography.

---

## Types of Image Steganography

### 1. LSB (Least Significant Bit) Injection
Modifies the last bit(s) of each pixel channel. Nearly invisible to the human eye. Best with PNG (lossless). See: [lsb-injection.md](../03-techniques/lsb-injection.md)

### 2. Metadata Hiding
Hides data in EXIF/IPTC metadata fields. No pixel changes needed. See: [metadata-hiding.md](../03-techniques/metadata-hiding.md)

### 3. Appended Data (EOF Hiding)
Appends data after the image's End-of-File marker. The image renders normally; extra bytes are ignored by viewers. Common in CTF challenges. See: [appended-data.md](../03-techniques/appended-data.md)

### 4. DCT-based Steganography (JPEG)
Modifies Discrete Cosine Transform coefficients inside JPEG compression. Used by tools like `steghide`.

---

## Real-World Uses

- Covert communication - journalists in hostile regions
- Digital watermarking - copyright protection
- CTF competitions - hiding flags inside challenge images
- Forensics - detecting hidden data in investigations

---

## Detection: Steganalysis

Detecting steganography is called **steganalysis**. Tools include:
- `zsteg` - statistical analysis of PNG/BMP
- `stegsolve` - visual bit-plane analysis
- `binwalk` - entropy and file signature scanning
