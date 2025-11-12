# PDF Decryption Script

This Python script decrypts an encrypted PDF file using an empty password and saves the decrypted version to a new file.

## Features

- Detects if a PDF is encrypted
- Attempts decryption using an empty password
- Saves decrypted content to a new PDF file
- Provides clear error messages for common issues

## Requirements

- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Install the required package using pip:

```bash
pip install PyPDF2
```

## Usage
```
python decrypt_pdf.py <input.pdf> <output.pdf>
```

