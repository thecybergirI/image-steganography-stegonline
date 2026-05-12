# Tools Overview

A collection of tools used for image steganography — both for hiding data and detecting it.

---

## 1. steghide

**Purpose**: Embed and extract data in JPEG and BMP images using passphrase protection.

**Install**:
```bash
sudo apt install steghide       # Linux/WSL
brew install steghide            # macOS
```

**Usage**:
```bash
# Hide a file inside an image
steghide embed -cf cover.jpg -sf secret.txt -p "mypassword"

# Extract hidden data
steghide extract -sf cover.jpg -p "mypassword"

# Get info about a file
steghide info cover.jpg
```

---

## 2. zsteg

**Purpose**: Detect hidden data in PNG and BMP files using statistical analysis.

**Install**:
```bash
gem install zsteg
```

**Usage**:
```bash
# Scan an image for hidden data
zsteg image.png

# Check all bit planes
zsteg -a image.png

# Extract a specific channel
zsteg -E "b1,rgb,lsb,xy" image.png
```

---

## 3. exiftool

**Purpose**: Read and write metadata (EXIF, IPTC, XMP) in image files.

**Install**:
```bash
sudo apt install libimage-exiftool-perl    # Linux
brew install exiftool                       # macOS
```

**Usage**:
```bash
# View all metadata
exiftool image.jpg

# Write a comment into metadata
exiftool -Comment="hidden message here" image.jpg

# Remove all metadata
exiftool -all= image.jpg
```

---

## 4. binwalk

**Purpose**: Scan files for embedded/appended files and data.

**Install**:
```bash
sudo apt install binwalk
```

**Usage**:
```bash
# Scan a file
binwalk image.png

# Extract embedded files automatically
binwalk -e image.png

# Show entropy graph
binwalk -E image.png
```

---

## 5. stegsolve

**Purpose**: Java-based visual analysis tool for examining image bit planes.

Download the JAR from https://github.com/Eugenio2314/stegsolve

```bash
java -jar stegsolve.jar
```

---

## 6. strings

**Purpose**: Built-in Unix tool; extracts printable strings from binary files. Quick first check.

```bash
strings image.png | grep -i flag
strings image.jpg | less
```

---

## Quick Reference

| Task | Tool |
|------|------|
| Hide data in JPEG (with password) | steghide |
| Detect LSB in PNG | zsteg |
| View/edit metadata | exiftool |
| Find appended/embedded files | binwalk |
| Visual bit-plane analysis | stegsolve |
| Quick string scan | strings |
| Python scripting | Pillow, piexif |
