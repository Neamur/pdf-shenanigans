

# this is to figure out the orientation issue with the pdf numbering.

import io
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter
import inquirer
import pprint
import os
global Page_no, total_pages, choice, position


ON_PAGE_INDEX = 0
WIDTH_RATIO = 2.914     # The width conversion ratio between pypdf default page size and fpdf default(A4) page size. 612/210
HEIGHT_RATIO = 2.66     # similarly, the height conversion ratio. 792/297
FONT_RATIO = 4455       # taking a4 page and size 14 as the default, we get 4455 as the ratio after doing  (210*297)//14. we have to pass the font size as an int format.



class PDF(FPDF):
    def footer(self):
        dynamic_font_scaling(self)
        self.set_font("helvetica", "B")
        self.set_text_color(255, 159, 28) # text color

        self.set_draw_color(255,255,255) # outline color

        if choice == "Fill_Stroke":
            with self.local_context(text_mode="FILL_STROKE"):
                # self.set_y(-15)     # set this seperately depending on the position given as Top or Bottom. 
                setting_y_pos(self)
                self.set_text_color(255, 159, 28) # text color
                self.set_draw_color(255,255,255) # outline color
                self.cell(w=0,h=0,text=f"{Page_no}/{total_pages}", align=position[1][0])    # Top [[R]ight] | how the pos slicing is used to get the align value
        elif choice == "Highlighted":
            with self.local_context():  # to fill with bg.
                # self.set_x(0)
                # self.set_y(-15)
                self.set_text_color(255, 255, 255) # text color
                self.set_fill_color(252, 163, 17) # cell background color

                setting_y_pos(self)
                margin_pos(self)
                # self.set_x(-20)                         # need to use this line only when doing right margin.
                self.cell(text=f"{Page_no}/{total_pages}",fill=True)




def new_content(pg_dimension,orientation="P"):      
    pdf = PDF()
    pdf.add_page(format=pg_dimension,orientation=orientation)      #format=pg_dimension
    # print(pdf.w)
    # print(pdf.h)
    return io.BytesIO(pdf.output())

def setting_y_pos(taking_self_var):    # this guy sets the y pos to -15mm/30mm to put the cursor at the bottom/top of the page.
    if position[0] == "Bottom":
        # print(position)
        taking_self_var.set_y(-15)
    elif position[0] == "Top":
        taking_self_var.set_y(30)


def margin_pos(taking_self_as_arg,right_pos=-20):     # this guy sets the x position.
    if position[1] == "Right":
        taking_self_as_arg.set_x(right_pos)     # -20 was the original value.
    elif position[1] == "Centre":
        taking_self_as_arg.set_x(taking_self_as_arg.w//2)
def set_right_pos():
    margin_pos(taking_self_as_arg=self,right_pos=-30)

def dynamic_font_scaling(taking_self_as_arg):       # scales the font size so that it doesnt appear too tiny/too large when the page size changes within the pdf.
    scaled_font_size = int(((page_dimension[2]//WIDTH_RATIO)*(page_dimension[3]//HEIGHT_RATIO))//FONT_RATIO)
    if scaled_font_size >1:
        taking_self_as_arg.font_size_pt = int(((page_dimension[2]//WIDTH_RATIO)*(page_dimension[3]//HEIGHT_RATIO))//FONT_RATIO)
    else:
        taking_self_as_arg.font_size_pt = 1

def pypdf_page_rotation():
    """ This func gets the page orientation and then re-assigns the page coordinates. """
    

style_choices = [inquirer.List("styles", message="choose the style of numbering you wish to apply: ", choices=["Fill_Stroke", "Highlighted"])]
style_choice = inquirer.prompt(style_choices)
choice = style_choice["styles"]


question = [
    inquirer.Checkbox(
        "pdfs",
        message="Select the pdfs that you wish to number (right arrow to select, left arrow to deselect):",
        choices=[a for a in os.listdir() if a.endswith(".pdf")],
    ),
]

aligning = [inquirer.List('alignments',message="Please choose the alignment: ",
                choices=['Top Left', 'Top Centre', 'Top Right', 'Bottom Left', 'Bottom Centre', 'Bottom Right'],)]
aligned_options = inquirer.prompt(aligning)     # most likely prompts the user 🤯
choosen_alignment = aligned_options["alignments"]       # stores the choosen option as a var taking it from the dict

position = choosen_alignment.split()       # seperates the two words to be used in various places for other functions.

while True:
    answer = inquirer.prompt(question)    # most likely prompts the user 🤯
    selected_pdfs =  [j for i in answer.values() for j in i]
    if len(selected_pdfs) >=1:
        break

print("Selected Pdfs Are :")
print(selected_pdfs)
for selected_pdf in selected_pdfs:
    reader = PdfReader(selected_pdf)
    
    total_pages = len(reader.pages)
    while ON_PAGE_INDEX < len(reader.pages):
        Page_no = ON_PAGE_INDEX+1
        page_dimension = reader.pages[ON_PAGE_INDEX].mediabox
        
        page_width_height = (page_dimension[2]//WIDTH_RATIO, page_dimension[3]//HEIGHT_RATIO)
        

        if ON_PAGE_INDEX == 21 or ON_PAGE_INDEX== 22:
            # page_dimension = reader.pages[ON_PAGE_INDEX].mediabox
            print(f"Page {Page_no}")
            print("lower right: ",page_dimension.lower_right)
            print("lower left : ",page_dimension.lower_left)
            print("upper right: ",page_dimension.upper_right)
            print("upper left : ",page_dimension.upper_left)
            print(f"the page width, height before is : {page_width_height}")
            page_width_height = (page_dimension[2]//HEIGHT_RATIO, page_dimension[3]//WIDTH_RATIO)
            print(f"the page width, height after is : {page_width_height}")
            print(page_dimension)
            deg = reader.get_page(ON_PAGE_INDEX).get('/Rotate')   
            print("degree of rotation is:",deg) 
        # if page_dimension.getUpperRight_x() - page_dimension.getUpperLeft_x() > page_dimension.getUpperRight_y() - page_dimension.getLowerRight_y():
        #     if deg in [0,180,None]:
        #         print('Landscape')
        #     else:
        #         print('Portrait')
        # else:
        #     if deg in [0,180,None]:
        #         print('Portrait')
        #     else:
        #         print('Landscape')
        # page_width_height as the arg for new_content()
        
            rotated_page = reader.pages[ON_PAGE_INDEX].transfer_rotation_to_content() #90
            page_overlay = PdfReader(new_content(page_width_height,"L")).pages[0]   
            # rotated_page_overlay = page_overlay.rotate(-90) #-90
            # degree = rotated_page_overlay.get("/Rotate")
            # print(degree)
        else:
            page_overlay = PdfReader(new_content(page_width_height,"P")).pages[0]
        # pdf = PDF()
        reader.pages[ON_PAGE_INDEX].merge_page(page2=page_overlay)      # page2=page_overlay

        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.write(f"numbered-{selected_pdf}")
        ON_PAGE_INDEX +=1
    print(f"Sucessfully Numbered : \"{selected_pdf}\" 👍")


