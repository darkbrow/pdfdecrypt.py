#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from pypdf import PdfReader, PdfWriter


def decrypt_pdf(input_path, output_path=None, force=False):
    try:
        # Determine default output filename if not provided
        if output_path is None:
            base, ext = os.path.splitext(input_path)
            if ext == "":
                # no extension, just append
                output_path = base + "_decrypted"
            else:
                output_path = base + "_decrypted" + ext

        # Check if output file already exists
        if os.path.exists(output_path) and not force:
            print(f"Error: Output file '{output_path}' already exists.")
            print("Use -f or --force flag to overwrite.")
            return False

        # Open the encrypted PDF
        reader = PdfReader(input_path)

        if reader.is_encrypted:
            # Try decrypting with an empty password
            if reader.decrypt("") == 0:
                print("Failed to decrypt. The PDF may require a password.")
                return False
            else:
                print("PDF decrypted successfully (empty password).")
        else:
            print("PDF is not encrypted.")

        # Write the decrypted content to a new file
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Decrypted PDF saved as: {output_path}")
        return True

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False


if __name__ == "__main__":
    # Accept: python pdfdecrypt.py <input.pdf> [output.pdf] [-f|--force]
    if len(sys.argv) < 2:
        print("Usage: python pdfdecrypt.py <input.pdf> [output.pdf] [-f|--force]")
        sys.exit(1)

    args = sys.argv[1:]
    force = any(a in ("-f", "--force") for a in args)
    # Collect non-flag args as file paths
    files = [a for a in args if a not in ("-f", "--force")]

    if len(files) < 1 or len(files) > 2:
        print("Usage: python pdfdecrypt.py <input.pdf> [output.pdf] [-f|--force]")
        sys.exit(1)

    input_pdf = files[0]
    output_pdf = files[1] if len(files) == 2 else None

    decrypt_pdf(input_pdf, output_pdf, force=force)
