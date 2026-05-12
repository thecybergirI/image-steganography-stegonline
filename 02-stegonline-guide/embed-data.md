# How to Hide Data Using StegOnline

This guide walks you through embedding (hiding) a secret message or file inside an image using [StegOnline](https://georgeom.net/StegOnline).



## Step-by-Step: Hiding a Text Message

### 1. Go to StegOnline
Open your browser and navigate to: https://georgeom.net/StegOnline

### 2. Upload your cover image
Click Upload Image and select a PNG image. This is the "cover" image that will carry your hidden data. It will look completely unchanged after embedding.

### 3. Click "Embed Data"
From the image homepage, click the Embed Data option.

### 4. Configure your LSB settings

Use these beginner-friendly settings:

| Setting | Recommended Value |
|---------|-------------------|
| Channels | R, G, B (all three checked) |
| Bit Order | LSB |
| Bit Plane | 0 |
| Direction | Row by Row |

### 5. Enter your message or upload a file
- Type your text directly into the input box, OR
- Upload a text file (.txt) with your message

### 6. Click "Embed & Download"
StegOnline generates a new image file with your message hidden inside. Download and save it.

### 7. Verify
Upload the downloaded image back to StegOnline, go to Extract Data, use the exact same settings, and confirm your message is recovered correctly.

 
## Important Notes

- **Always note your settings** - you cannot extract without them.
- **PNG is strongly preferred** over JPEG. JPEG's lossy compression will destroy LSB data.
- The output image file size may be slightly different from the original - this is normal.
- Do not re-compress or resize the stego image, as this will destroy the hidden data.
