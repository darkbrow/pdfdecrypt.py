#!env python
# -*- coding: utf-8 -*-
import sys
from PyPDF2 import PdfReader, PdfWriter

def decrypt_pdf(input_path, output_path):
    try:
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
    if len(sys.argv) != 3:
        print("Usage: python decrypt_pdf.py <input.pdf> <output.pdf>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]

    decrypt_pdf(input_pdf, output_pdf)
