# Bit Plane Analysis with StegOnline

## What Is a Bit Plane?

Every pixel in an RGB image has three channels (R, G, B), each stored as an 8-bit number (0–255). A **bit plane** is a 2D slice of the image showing only one specific bit position across all pixels.

```
Pixel value: 200 = 1 1 0 0 1 0 0 0
                   ^ ^ ^ ^ ^ ^ ^ ^
             Bit: 7 6 5 4 3 2 1 0
                  MSB           LSB
```

If you take bit 0 from every pixel in the image and view them as a black-and-white image, that is **bit plane 0** (the LSB plane).

---

## Viewing Bit Planes in StegOnline

1. Upload your image to [StegOnline](https://georgeom.net/StegOnline)
2. Click **Browse Bit Planes**
3. Use the controls to cycle through each channel (R, G, B, A) and each bit level (0–7)

You will see a black-and-white image for each plane. That gives you **32 total planes** (4 channels × 8 bits).

---

## What to Look For

### Normal images
- **Bit planes 7, 6, 5** (high bits): Look like a grainy, recognizable version of the image. They carry the most visual information.
- **Bit planes 0, 1, 2** (low bits): Look like random noise. These bits contribute very little to appearance.

### Images with hidden data
- **Bit plane 0 with LSB steganography**: Instead of random noise, you may see structured patterns, text, or shapes — a strong indicator of hidden data.
- **Unusually ordered or patterned noise** in any low bit plane is suspicious.

---

## Example: Spotting LSB Steganography

In a clean image, the LSB plane (bit 0) looks like this:
```
Random salt-and-pepper noise — no recognizable pattern
```

In an image with a hidden message, the LSB plane may show:
```
Faint horizontal banding, structured noise, or even readable text
```

---

## Hiding an Image Inside a Bit Plane

StegOnline also lets you **hide one image inside another's bit plane**:

1. Upload your cover image
2. Click **Hide Image**
3. Upload the secret image you want to hide
4. Choose which bit plane to embed it in (Bit 0 is least visible)
5. Download the result

To reveal it:
1. Upload the stego image
2. Click **Browse Bit Planes**
3. Navigate to the same bit plane and channel
4. The hidden image will be visible in the bit plane viewer

---

## Summary

| Bit Plane | Visual Importance | Steganography Use |
|-----------|------------------|-------------------|
| 7 (MSB) | Very high — changes colour drastically | Not used (too visible) |
| 6, 5, 4 | Medium to high | Rarely used |
| 3, 2, 1 | Low | Sometimes used |
| 0 (LSB) | Minimal — barely affects colour | Most common hiding spot |
