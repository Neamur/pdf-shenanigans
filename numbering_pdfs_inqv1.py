import io
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter
import inquirer
import pprint
import os
global Page_no, total_pages

ON_PAGE_INDEX = 0

class PDF(FPDF):
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_x(-30)
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "B", 14)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(252, 163, 17) #orange
        # Printing page number:
        # self.cell(100,0, align="L",fill=False)
        self.cell(text=f"{Page_no}/{total_pages}", align="L", fill=True)
    
def new_content():
    pdf = PDF()
    pdf.add_page()
    return io.BytesIO(pdf.output())

pp = pprint.PrettyPrinter(indent=4)

question = [
    inquirer.Checkbox(
        "pdfs",
        message="Select the pdfs that you wish to number (right arrow to select, left arrow to deselect):",
        choices=[a for a in os.listdir() if a.endswith(".pdf")],
    ),
]

answer = inquirer.prompt(question)    # most likely prompts the user 🤯
selected_pdfs =  [j for i in answer.values() for j in i]
print("Selected Pdfs Are :")
pp.pprint(selected_pdfs)
for selected_pdf in selected_pdfs:
    reader = PdfReader(selected_pdf)
    total_pages = len(reader.pages)
    while ON_PAGE_INDEX < len(reader.pages):
        Page_no = ON_PAGE_INDEX+1
        page_overlay = PdfReader(new_content()).pages[0]
        pdf = PDF()
        # page_overlay = PdfReader(pdf).pages[0]
        reader.pages[ON_PAGE_INDEX].merge_page(page2=page_overlay)

        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.write(f"numbered-{selected_pdf}")
        ON_PAGE_INDEX +=1
    print(f"Sucessfully Numbered : \"{selected_pdf}\" 👍")
    # print("sucessful 👍")


