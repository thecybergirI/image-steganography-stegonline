#!/usr/bin/env python3
"""
hide_message.py — Hide a text message inside a PNG image using LSB steganography.

Usage:
    python3 hide_message.py --image input.png --message "your secret" --output hidden.png
    python3 hide_message.py --image input.png --file secret.txt --output hidden.png

Requirements:
    pip install Pillow
"""

import argparse
from PIL import Image


# Delimiter to mark end of hidden message
DELIMITER = "<<END>>"


def text_to_bits(text):
    """Convert a string to a list of bits."""
    bits = []
    for char in text:
        byte = format(ord(char), '08b')
        bits.extend([int(b) for b in byte])
    return bits


def hide_message(image_path, message, output_path):
    """Hide a message in the LSB of an image's pixel channels."""
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())
    width, height = img.size

    full_message = message + DELIMITER
    bits = text_to_bits(full_message)

    # Check capacity
    max_bits = len(pixels) * 3
    if len(bits) > max_bits:
        raise ValueError(
            f"Message too long! Max capacity: {max_bits // 8} bytes, "
            f"message size: {len(bits) // 8} bytes"
        )

    new_pixels = []
    bit_idx = 0

    for pixel in pixels:
        r, g, b = pixel
        channels = [r, g, b]
        new_channels = []

        for channel in channels:
            if bit_idx < len(bits):
                # Replace LSB with message bit
                new_channel = (channel & 0xFE) | bits[bit_idx]
                bit_idx += 1
            else:
                new_channel = channel
            new_channels.append(new_channel)

        new_pixels.append(tuple(new_channels))

    # Save modified image
    new_img = Image.new("RGB", (width, height))
    new_img.putdata(new_pixels)
    new_img.save(output_path)

    print(f"[+] Message hidden successfully in '{output_path}'")
    print(f"[+] Used {bit_idx} of {max_bits} available bits "
          f"({bit_idx/max_bits*100:.1f}% capacity)")


def main():
    parser = argparse.ArgumentParser(description="Hide a message in an image using LSB")
    parser.add_argument("--image", required=True, help="Path to cover image (PNG recommended)")
    parser.add_argument("--output", required=True, help="Output stego image path")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--message", help="Text message to hide")
    group.add_argument("--file", help="Path to text file to hide")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            message = f.read()
    else:
        message = args.message

    hide_message(args.image, message, args.output)


if __name__ == "__main__":
    main()
