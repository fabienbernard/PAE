# PDF Attachment Extractor

## Overview
This Python script is designed to extract attachments from a PDF file. It has been enhanced to support command-line argument parsing, allowing for more flexible and user-friendly interaction.

## New Functionalities and Flags

### Command-Line Argument Parsing
The script can now be executed with command-line arguments for the PDF file and an optional output directory.

### Output Directory Specification
The `-o` or `--output` flag allows the user to specify where the extracted files should be saved.

### Verbosity Flag
The `-v` or `--verbose` flag increases the verbosity of the script's output for better user feedback.

### Error Handling
The script includes basic error handling to manage issues like file not found or reading errors.

## Requirements
- Python 3
- pypdf library

## Installation
Ensure that you have Python 3 installed on your system. You can install the pypdf library using pip:

```bash
pip install pypdf
```

## Usage
Run the script from the command line by specifying the path to the PDF file. Optionally, you can specify the output directory and verbosity:

```bash
python pdf_extract.py path/to/yourfile.pdf -o path/to/output/dir -v
```

Replace `pdf_extract.py` with the name of your Python script file, and adjust the paths as necessary.

## Example
To extract attachments from `example.pdf` and save them to the `attachments` directory with verbose output:

```bash
python pdf_extract.py -o attachments -v
```

## License
This project is licensed under the MIT License.

---
