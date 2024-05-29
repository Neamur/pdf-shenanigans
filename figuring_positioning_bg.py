# this is to figure out how to number with the BG fill in centre.

import io
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter
import inquirer
import os
global Page_no, total_pages, choice, position

# pdf.set_right_margin(pdf.w - right_boundary) --> this shows us that there is a pdf.w which gives the width of the page 👍
ON_PAGE_INDEX = 0


class PDF(FPDF):
    def footer(self):
        self.set_font("helvetica", "B", 14)
        self.set_text_color(255, 159, 28) # text color
        self.set_draw_color(255,255,255) # outline color
        with self.local_context():  # to fill with bg.
            self.set_text_color(255, 255, 255) # text color
            self.set_fill_color(252, 163, 17) # cell background color
            setting_xy_pos(self)
            margin_pos(self)
            self.cell(text=f"{Page_no}/{total_pages}",fill=True)


def new_content():
    pdf = PDF()
    pdf.add_page()

    return io.BytesIO(pdf.output())


def setting_xy_pos(taking_self_var):    # this guy sets the y pos to -15mm/30mm to put the cursor at the bottom of the page.
    if position[0] == "Bottom":
        print(position)
        taking_self_var.set_y(-15)
    elif position[0] == "Top":
        taking_self_var.set_y(30)

def margin_pos(taking_self_as_arg):     # this guy sets the x position.
    if position[1] == "Right":
        taking_self_as_arg.set_x(-20)
    elif position[1] == "Center":
        taking_self_as_arg.set_x(taking_self_as_arg.w//2)



question = [
    inquirer.Checkbox(
        "pdfs",
        message="Select the pdfs that you wish to number (right arrow to select, left arrow to deselect):",
        choices=[a for a in os.listdir() if a.endswith(".pdf")],
    ),
]
answer = inquirer.prompt(question)    # most likely prompts the user 🤯
selected_pdfs =  [j for i in answer.values() for j in i]

aligning = [inquirer.List('alignments',message="Please choose the alignment: ",
                choices=['Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right'],)]
aligned_options = inquirer.prompt(aligning)     # most likely prompts the user 🤯
choosen_alignment = aligned_options["alignments"]       # stores the choosen option as a var taking it from the dict

position = choosen_alignment.split()  

for selected_pdf in selected_pdfs:
    reader = PdfReader(selected_pdf)
    
    total_pages = len(reader.pages)
    while ON_PAGE_INDEX < len(reader.pages):
        Page_no = ON_PAGE_INDEX+1
        page_overlay = PdfReader(new_content()).pages[0]
        pdf = PDF()
        reader.pages[ON_PAGE_INDEX].merge_page(page2=page_overlay)

        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.write(f"numbered-{selected_pdf}")
        ON_PAGE_INDEX +=1
    print(f"Sucessfully Numbered : \"{selected_pdf}\" 👍")



