# PDF Decryption Script

This Python script decrypts an encrypted PDF file using an empty password and saves the decrypted version to a new file.

## Features

- Detects if a PDF is encrypted
- Attempts decryption using an empty password
- Saves decrypted content to a new PDF file
- Provides clear error messages for common issues

## Requirements

- Python 3.x
- [pypdf](https://pypi.org/project/pypdf/)

Install the required package using pip:

```bash
pip install pypdf
```

## Usage
```
python pdfdecrypt.py <input.pdf> [output.pdf] [-f --force]
```
- If you don't specify output file, it will be saved in the format 'filename_decrypted.pdf'.
- If you want to overwrite the existing file, add the -f switch.

