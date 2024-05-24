#import pypdf
from pypdf import PdfReader
import argparse
import os

def get_attachments(reader):
    """
    Retrieves the file attachments of the PDF as a dictionary of file names
    and the file data as a bytestring.
    :param reader: PyPDF2.PdfFileReader object
    :return: dictionary of filenames and bytestrings
    """
    catalog = reader.trailer["/Root"]
    if '/Names' in catalog and '/EmbeddedFiles' in catalog['/Names'] and '/Names' in catalog['/Names']['/EmbeddedFiles']:
        file_names = catalog['/Names']['/EmbeddedFiles']['/Names']
        attachments = {}
        for f in file_names:
            if isinstance(f, str):
                name = f
                data_index = file_names.index(f) + 1
                f_dict = file_names[data_index].get_object()
                f_data = f_dict['/EF']['/F'].get_data()
                attachments[name] = f_data
        return attachments
    else:
        return {}

def save_attachments(attachments, output_dir):
    """
    Saves the attachments to the specified directory.
    :param attachments: dictionary of file data
    :param output_dir: directory to save files
    """
    for file_name, file_data in attachments.items():
        output_path = os.path.join(output_dir, file_name)
        with open(output_path, 'wb') as outfile:
            outfile.write(file_data)
            print(f"File saved: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Extract attachments from a PDF file.")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    parser.add_argument("-o", "--output", default=".", help="Output directory for extracted files")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    
    args = parser.parse_args()

    if args.verbose:
        print(f"Opening PDF file: {args.pdf_file}")

    try:
        with open(args.pdf_file, 'rb') as handler:
            reader = PdfReader(handler)
            if args.verbose:
                print("Extracting attachments...")
            attachments = get_attachments(reader)
            if attachments:
                save_attachments(attachments, args.output)
            else:
                print("No attachments found in the PDF.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
