#!/usr/bin/env python3
"""
metadata_hide.py — Hide and extract messages using JPEG EXIF metadata.

Usage:
    # Hide a message
    python3 metadata_hide.py hide --image input.jpg --message "secret" --output stego.jpg

    # Extract a message
    python3 metadata_hide.py extract --image stego.jpg

Requirements:
    pip install Pillow piexif
"""

import argparse
import piexif


ENCODING_PREFIX = b"ASCII\x00\x00\x00"


def hide_in_metadata(image_path, message, output_path):
    """Hide a message in the EXIF UserComment field of a JPEG."""
    try:
        exif_data = piexif.load(image_path)
    except Exception:
        exif_data = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}}

    encoded = ENCODING_PREFIX + message.encode('utf-8')
    exif_data["Exif"][piexif.ExifIFD.UserComment] = encoded

    exif_bytes = piexif.dump(exif_data)
    piexif.insert(exif_bytes, image_path, output_path)

    print(f"[+] Message hidden in EXIF UserComment of '{output_path}'")


def extract_from_metadata(image_path):
    """Extract a message from the EXIF UserComment field of a JPEG."""
    exif_data = piexif.load(image_path)
    comment = exif_data.get("Exif", {}).get(piexif.ExifIFD.UserComment, None)

    if comment and len(comment) > 8:
        return comment[8:].decode('utf-8', errors='ignore')
    return None


def main():
    parser = argparse.ArgumentParser(description="Hide/extract messages in JPEG metadata")
    subparsers = parser.add_subparsers(dest="command")

    # Hide command
    hide_parser = subparsers.add_parser("hide", help="Hide a message")
    hide_parser.add_argument("--image", required=True)
    hide_parser.add_argument("--message", required=True)
    hide_parser.add_argument("--output", required=True)

    # Extract command
    extract_parser = subparsers.add_parser("extract", help="Extract a message")
    extract_parser.add_argument("--image", required=True)

    args = parser.parse_args()

    if args.command == "hide":
        hide_in_metadata(args.image, args.message, args.output)
    elif args.command == "extract":
        message = extract_from_metadata(args.image)
        if message:
            print(f"[+] Hidden message found:\n\n{message}")
        else:
            print("[-] No hidden message found in metadata.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
