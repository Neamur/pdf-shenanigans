
import io
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter
global Page_no, total_pages

IN_FILEPATH = "result.pdf"
OUT_FILEPATH = "new-tuto23.pdf"
ON_PAGE_INDEX = 0 # Index of the target page (starts at zero)

class PDF(FPDF):
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_x(15)
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
    # pdf.set_font("times", "B", 0)
    # pdf.text(50, 150, ".")
    # print(io.BytesIO(pdf.output()))
    return io.BytesIO(pdf.output())

reader = PdfReader(IN_FILEPATH)
total_pages = len(reader.pages)
try:
    while ON_PAGE_INDEX < len(reader.pages):
        Page_no = ON_PAGE_INDEX+1
        page_overlay = PdfReader(new_content()).pages[0]
        pdf = PDF()
        # page_overlay = PdfReader(pdf).pages[0]
        reader.pages[ON_PAGE_INDEX].merge_page(page2=page_overlay)

        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.write(OUT_FILEPATH)
        ON_PAGE_INDEX +=1
    print(f"sucessfully numbered {selected_pdf} 👍")
except:
    print("there was some error")