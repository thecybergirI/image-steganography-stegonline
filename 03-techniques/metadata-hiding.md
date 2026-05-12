# Metadata Hiding (EXIF Steganography)

## What Is EXIF Metadata?

Image files carry metadata — data about the data. EXIF (Exchangeable Image File Format) metadata is embedded in JPEG and PNG files and typically includes:

- Camera make and model
- Date and time photo was taken
- GPS coordinates
- Exposure settings (ISO, aperture, shutter speed)
- Software used to edit the image
- **Comment fields** — freely writable

These comment and description fields can store **arbitrary text**, making them a simple hiding spot.

---

## Hiding Data with exiftool

```bash
# View existing metadata
exiftool photo.jpg

# Hide a message in the Comment field
exiftool -Comment="Meet me at midnight. Bring the package." photo.jpg

# Hide in the ImageDescription field
exiftool -ImageDescription="The flag is: CTF{hidden_in_plain_sight}" photo.jpg

# Hide in a custom XMP field
exiftool -XMP-dc:Description="secret data here" photo.jpg
```

---

## Extracting Hidden Metadata

```bash
# Show all metadata
exiftool photo.jpg

# Show only the Comment field
exiftool -Comment photo.jpg

# Show only specific fields
exiftool -ImageDescription -Comment photo.jpg
```

---

## Hiding Data with Python (piexif)

```python
import piexif
import json

def hide_in_exif(image_path, secret, output_path):
    # Load existing EXIF or create new
    try:
        exif_data = piexif.load(image_path)
    except:
        exif_data = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}}

    # Store secret in UserComment field (tag 0x9286)
    # UserComment requires a specific encoding prefix
    prefix = b"ASCII\x00\x00\x00"
    exif_data["Exif"][piexif.ExifIFD.UserComment] = prefix + secret.encode()

    exif_bytes = piexif.dump(exif_data)
    piexif.insert(exif_bytes, image_path, output_path)
    print(f"[+] Secret hidden in EXIF of {output_path}")


def extract_from_exif(image_path):
    exif_data = piexif.load(image_path)
    comment = exif_data["Exif"].get(piexif.ExifIFD.UserComment, b"")
    # Strip the 8-byte encoding prefix
    if comment:
        return comment[8:].decode(errors="ignore")
    return None


# Example usage
hide_in_exif("original.jpg", "CTF{exif_master}", "stego.jpg")
print(extract_from_exif("stego.jpg"))
```

---

## Limitations

- Many social media platforms (Twitter, Facebook, Instagram) **strip EXIF data** on upload
- Easily detected with `exiftool` — not very covert on its own
- Best used in combination with encoded/encrypted content in the field

---

## CTF Tip

Always run `exiftool` as your **first step** when analyzing a CTF image challenge. Hidden flags are very commonly placed in metadata fields.

```bash
exiftool challenge.png | grep -i "flag\|ctf\|secret\|hint"
```
