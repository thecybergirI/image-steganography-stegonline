#!/usr/bin/env python3
"""
extract_message.py — Extract a hidden text message from a PNG image using LSB steganography.

Usage:
    python3 extract_message.py --image hidden.png
    python3 extract_message.py --image hidden.png --output recovered.txt

Requirements:
    pip install Pillow
"""

import argparse
from PIL import Image


DELIMITER = "<<END>>"


def bits_to_text(bits):
    """Convert a list of bits to a string."""
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(''.join(str(b) for b in byte), 2))
        chars.append(char)
    return ''.join(chars)


def extract_message(image_path):
    """Extract a hidden message from the LSBs of an image."""
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())

    bits = []
    for pixel in pixels:
        for channel in pixel:
            bits.append(channel & 1)  # Extract LSB

    # Decode bits to text and look for delimiter
    text = bits_to_text(bits)

    if DELIMITER in text:
        message = text[:text.index(DELIMITER)]
        return message
    else:
        return None


def main():
    parser = argparse.ArgumentParser(description="Extract a hidden message from an image")
    parser.add_argument("--image", required=True, help="Path to stego image")
    parser.add_argument("--output", help="Save extracted message to this file (optional)")
    args = parser.parse_args()

    print(f"[*] Analyzing '{args.image}'...")
    message = extract_message(args.image)

    if message:
        print(f"[+] Hidden message found!\n")
        print("-" * 40)
        print(message)
        print("-" * 40)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(message)
            print(f"\n[+] Message saved to '{args.output}'")
    else:
        print("[-] No hidden message found (delimiter not detected).")
        print("    The image may not contain a hidden message, or it was hidden with different software.")


if __name__ == "__main__":
    main()
