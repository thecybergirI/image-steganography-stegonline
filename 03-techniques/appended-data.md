# Appended Data (EOF Hiding)

## How It Works

Image files have specific End-of-File (EOF) markers that tell image viewers when the image data ends. Data appended **after** this marker is completely ignored by image viewers but remains in the file.

### JPEG EOF Marker
JPEG files end with the two bytes: `FF D9`

```
[JPEG image data .... FF D9] [hidden data appended here]
                     ^
                 EOF marker
```

### PNG EOF Marker
PNG files end with the IEND chunk: `49 45 4E 44 AE 42 60 82`

---

## Hiding Data Manually

### Using Linux command line
```bash
# Append a text file to a JPEG
cat cover.jpg secret.txt > stego.jpg

# Append a zip archive
cat cover.jpg archive.zip > stego.jpg

# Append raw text
echo "CTF{hidden_after_eof}" >> cover.jpg
```

### Verifying it works
```bash
# Image still opens normally
eog stego.jpg

# But the hidden data is there
strings stego.jpg | tail -20
xxd stego.jpg | tail -20
```

---

## Extracting Appended Data

### Method 1: binwalk
```bash
# Detect embedded content
binwalk stego.jpg

# Auto-extract everything found
binwalk -e stego.jpg
# Creates _stego.jpg.extracted/ directory with extracted files
```

### Method 2: Manual extraction with Python
```python
def extract_after_eof(image_path, output_path, eof_marker=b'\xff\xd9'):
    with open(image_path, 'rb') as f:
        data = f.read()

    eof_index = data.rfind(eof_marker)
    if eof_index == -1:
        print("[-] EOF marker not found")
        return

    hidden = data[eof_index + len(eof_marker):]
    if not hidden:
        print("[-] No data found after EOF")
        return

    with open(output_path, 'wb') as f:
        f.write(hidden)
    print(f"[+] Extracted {len(hidden)} bytes to {output_path}")


extract_after_eof("stego.jpg", "extracted_data.zip")
```

### Method 3: Using foremost
```bash
sudo apt install foremost
foremost -i stego.jpg -o output_dir/
```

---

## Hiding a ZIP Archive Inside a JPEG

This is a popular CTF technique. A valid JPEG that is also a valid ZIP file is called a **polyglot file**.

```bash
# Create zip with the secret
zip -r secret.zip flag.txt

# Append zip to image
cat cover.jpg secret.zip > stego.jpg

# Verify: image still opens
file stego.jpg   # says: JPEG image data

# Also verify: ZIP is valid
unzip stego.jpg  # extracts flag.txt!
```

---

## CTF Tip

When analyzing a challenge image:
1. Run `binwalk image.jpg` — looks for file signatures inside the file
2. Run `file image.jpg` — checks the real file type
3. Run `strings image.jpg | tail -30` — look for readable text after EOF
4. Check file size — unusually large for the visible image content is suspicious
