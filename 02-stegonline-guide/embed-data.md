# How to Hide Data Using StegOnline

This guide walks you through embedding (hiding) a secret message or file inside an image using [StegOnline](https://georgeom.net/StegOnline).

---

## Step-by-Step: Hiding a Text Message

### 1. Go to StegOnline
Open your browser and navigate to: https://georgeom.net/StegOnline

### 2. Upload your cover image
Click **Upload Image** and select a PNG image. This is the "cover" — the image that will carry your hidden data. It will look completely unchanged after embedding.

> **Tip:** Use a PNG image with natural detail (a photo, not a solid colour). Larger images can carry more data.

### 3. Click "Embed Data"
From the image homepage, click the **Embed Data** option.

### 4. Configure your LSB settings

Use these beginner-friendly settings:

| Setting | Recommended Value |
|---------|-------------------|
| Channels | R, G, B (all three checked) |
| Bit Order | LSB |
| Bit Plane | 0 |
| Direction | Row by Row |

### 5. Enter your message or upload a file
- Type your text directly into the input box, **OR**
- Upload a text file (.txt) with your message

### 6. Check capacity
StegOnline will warn you if the image is too small for your message. If so, use a larger image or a shorter message.

### 7. Click "Embed & Download"
StegOnline generates a new image file with your message hidden inside. Download and save it.

### 8. Verify (optional)
Upload the downloaded image back to StegOnline, go to **Extract Data**, use the **exact same settings**, and confirm your message is recovered correctly.

---

## Example Walkthrough

```
Cover image:     photo.png  (500 x 500 pixels = 750,000 bits of capacity)
Message:         "The flag is: CTF{steg_basics}"
Settings:        RGB, LSB, Bit 0, Row by Row
Output:          photo_hidden.png
```

The output image is visually identical to `photo.png`, but the LSBs of its pixels now encode your message.

---

## Capacity Formula

The maximum bytes you can hide in an image:

```
Max bytes = (image width × image height × number of channels) / 8

Example: 500×500 image, 3 channels (RGB)
= (500 × 500 × 3) / 8
= 93,750 bytes ≈ 91 KB
```

---

## Important Notes

- **Always note your settings** — you cannot extract without them.
- **PNG is strongly preferred** over JPEG. JPEG's lossy compression will destroy LSB data.
- The output image file size may be slightly different from the original — this is normal.
- Do not re-compress or resize the stego image, as this will destroy the hidden data.
