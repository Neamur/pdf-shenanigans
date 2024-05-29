import pypdf
from pypdf import PdfReader, PdfWriter
import os
reader = PdfReader("result.pdf")
input_file = 'result.pdf'
output_folder = 'pdf_pages'

with open(input_file, 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)
    num_pages = len(reader.pages)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num in range(num_pages):
        output_filename = os.path.join(output_folder, f'page_{page_num + 1}.pdf')
        with open(output_filename, 'wb') as output_file:
            pdf_writer = PdfWriter()
            pdf_writer.add_page(reader.pages[page_num])
            pdf_writer.write(output_file)

print("PDF pages extracted successfully!")

