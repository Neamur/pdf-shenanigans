import os
from pypdf import PdfReader, PdfWriter
import inquirer
import pprint
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
import logging
from rich.logging import RichHandler
from inquirer.themes import BlueComposure
global selected_pages


# the code is about extracting pages from selected pdf file.
# a complicated version of the splitting pages.py file.
# make it run as a module and seperately too.


'''
[?] Select pdfs  (Select the PDFs for page extraction)
    |_ [ ] sdfs.pdf
    |_ [ ] sdfyer.pdf
    |_ [ ] ...

You have selected these PDFs to work on :
['sdfs','sdfyer']

Currently working on the PDF: ['sdfs']

[?]Extracting
    |_ > All
    |_ > select pages to extract.

[?] Select the pages you wish to extract.
    |_ [ ] Page 1
    |_ [ ] Page 2
    |_ ...

[?] Apply the same settings to the rest of the pdfs? (if you wish to select different settings for the remaining pdfs, select 'NO')
    |_ > Yes
    |_ > No'''

# num_pages = 0
# output_folder = "pdf_pages"


logging.basicConfig(
level="NOTSET",
format="%(message)s",
datefmt="[%X]",
handlers=[RichHandler(rich_tracebacks=True)])
log = logging.getLogger("rich")

def all_pages(num_pages,selected_pdf,reader):
    for page_num in range(num_pages):
        output_filename = os.path.join(output_folder, f'{selected_pdf}_page {page_num + 1}.pdf')
        pdf_writer = PdfWriter()
        pdf_writer.add_page(reader.pages[page_num])
        pdf_writer.write(output_filename)
    console.print(f"[bold green]👍 PDF pages from \[{selected_pdf}] extracted successfully! \n")

def select_pages(selected_pages,selected_pdf):
    try:
        for i in selected_pages:
            output_filename = os.path.join(output_folder, f'{selected_pdf}_{i}.pdf')
            pdf_writer = PdfWriter()
            pdf_writer.add_page(reader.pages[int(i[4:])-1])
            pdf_writer.write(output_filename)
        console.print(f"[bold green]👍 PDF pages from \[{selected_pdf}] extracted successfully! \n")
    except Exception: 
        return i,log.exception(f"Index out of range \n")
console = Console() # no need softwarp

question = [inquirer.Checkbox(
        "pdfs",
        message="Select the PDF/PDFs. (right arrow to select, left arrow to deselect):",
        choices=[a for a in os.listdir() if a.endswith(".pdf")],
    ),
]
# pp = pprint.PrettyPrinter(indent=4)

while True:
    answer = inquirer.prompt(question)    # most likely prompts the user 🤯
    selected_pdfs =  [j for i in answer.values() for j in i]
    if len(selected_pdfs) >=1:
        rprint("[bold green]You have selected these PDFs to work on: ")
        console.print(selected_pdfs,"\n")
        break

extracting_options = [inquirer.List("Extracting",
        message="Extracting (right arrow to select, left arrow to deselect):",
        choices=["All pages","Select pages to extract"],
    ),
]

def extracting_option_func():
    extracting_prompt = inquirer.prompt(extracting_options,theme=BlueComposure())
    extracting_option = extracting_prompt["Extracting"]
    return extracting_option
extracting_option = "All pages" #extracting_option_func()
def selecting_pages(num_pages):
    pages_in_pdf = [inquirer.Checkbox("Pages_of_pdf",
        message="Select the pages you wish to extract (right arrow to select, left arrow to deselect):",
        choices=[f"Page {i+1}" for i in range(num_pages)],
        ),
        ]

    while True:
        prompting_for_pages = inquirer.prompt(pages_in_pdf)
        selected_pages =  [j for i in prompting_for_pages.values() for j in i]
        if len(selected_pages) >=1:
            print("You have selected these Pages to extract: ")
            console.print(selected_pages,"\n")
            break
    return selected_pages

keep_settings = [inquirer.List("settings",
        message="Apply the same settings to the rest of the pdfs? (Default=Yes)",
        choices=["Yes","No"],
        
    ),
]

def general_read_write(selected_pdf):
    console.print(f"[green]you are currently working on `{selected_pdf}`\n")
    reader = PdfReader(selected_pdf)
    output_folder = 'pdf_pages'
    num_pages = len(reader.pages)
    # with open(selected_pdf, 'rb') as pdf_file:

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return num_pages,output_folder,reader

def completed_success(selected_pdf):
    print(f"PDF pages from [{selected_pdf}] extracted successfully! 👍\n")

def many_pdfs_settings_runner():    # pass the settings and selected_pages as args
    if settings == "Yes":
        print("global now works")
    # if yes, we need to reuse same pdf pages for the extraction but diff pdf.
    for selected_pdf in selected_pdfs[1:]:
        num_pages,output_folder,reader = general_read_write(selected_pdf)
        if extracting_option == "All pages":
            all_pages(num_pages=num_pages,selected_pdf=selected_pdf,reader=reader)
        elif extracting_option == "Select pages to extract":
            # selecting_pages(num_pages=num_pages)
            select_pages(selected_pages,selected_pdf)
        completed_success(selected_pdf)

# if len(selected_pdfs) == 1:
#     num_pages,output_folder,reader = general_read_write(selected_pdfs[0])
#     if extracting_option== "All pages":
#         all_pages(num_pages,selected_pdf=selected_pdfs[0],reader=reader)
#     elif extracting_option == "Select pages to extract":
#         selected_pages = selecting_pages(num_pages)
#         select_pages(selected_pages,selected_pdf=selected_pdfs[0])
#     completed_success(selected_pdf=selected_pdfs[0])

# elif len(selected_pdfs) > 1:
#     num_pages,output_folder,reader = general_read_write(selected_pdfs[0])
#     if extracting_option== "All pages":
#         all_pages(num_pages=num_pages,selected_pdf=selected_pdfs[0],reader=reader)
#     elif extracting_option == "Select pages to extract":
#         selected_pages = selecting_pages(num_pages)
#         select_pages(selected_pages,selected_pdf=selected_pdfs[0])
#     completed_success(selected_pdf=selected_pdfs[0])
#     settings_prompt = inquirer.prompt(keep_settings)
#     settings = settings_prompt["settings"]
#     # print(settings,settings[0])
#     many_pdfs_settings_runner()
# if __name=="__main__":
settings_check = True
page_selection_check = True
counter = 0
extracting_option_check = True
output_folder = 'extracted_pages'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for selected_pdf in selected_pdfs:
    console.print(f"[bold green]👉 You are Currently Working on `{selected_pdf}`\n")
    reader = PdfReader(selected_pdf)
    num_pages = len(reader.pages)
    # with open(selected_pdf, 'rb') as pdf_file:
    # counter += 1
    # print(counter)

    if extracting_option_check == True:# if settings_check == False and extracting_option_check == True:
        # extracting_prompt = inquirer.prompt(extracting_options)
        # extracting_option = extracting_prompt["Extracting"] #"Select pages to extract"
        extracting_option = extracting_option_func()
        extracting_option_check = False
        
    if extracting_option== "All pages":
        all_pages(num_pages=num_pages,selected_pdf=selected_pdf,reader=reader)
        if len(selected_pdfs) >1:
            if settings_check == True:
                settings_prompt = inquirer.prompt(keep_settings, theme=BlueComposure())
                settings = settings_prompt["settings"]
            if settings == "Yes":
                settings_check = False
                page_selection_check = False
                # all_pages(num_pages=num_pages,selected_pdf=selected_pdf,reader=reader)
            else:
                # all_pages(num_pages=num_pages,selected_pdf=selected_pdf,reader=reader)
                page_selection_check = True
                settings_check = False
                extracting_option_check = True
            # else:
                # all_pages(num_pages=num_pages,selected_pdf=selected_pdf,reader=reader)
        # else:
            # all_pages(num_pages=num_pages,selected_pdf=selected_pdf,reader=reader)
                
            # if page_selection_check == True:
            #     selected_pages = selecting_pages(num_pages)
            #     select_pages(selected_pages,selected_pdf)

    elif extracting_option == "Select pages to extract":
        if page_selection_check == False:
            # try:
            page,logs = select_pages(selected_pages,selected_pdf)
            # except Exception:
            if page != None:
                console.print(f'\n[bold][red]⚠️ Error: Page number selected exceeded the maximum number of pages allowed for the selected PDF :-[/bold]\[{selected_pdf}]\n')
                console.print(f'[bold][yellow]⚠️ Warning[/bold]: unable to extract \[{page}] from \[{selected_pdf}] with only [{num_pages}] pages.\n')
                console.print(f'[bold][yellow]The page length is measured in units of the original document, which differ from the selected page size in the current PDF. Selected page number does not exist in the current PDF.\n')
                # log.exception(f"Index out of range ")
                # print(logs)
            # page_selection_check = False

            # selected_pages = selecting_pages(num_pages)

        elif page_selection_check == True:
            selected_pages = selecting_pages(num_pages)
            select_pages(selected_pages,selected_pdf)

            if len(selected_pdfs) >1:
                if settings_check == True:
                    settings_prompt = inquirer.prompt(keep_settings,theme=BlueComposure())
                    settings = settings_prompt["settings"]
                if settings == "Yes":
                    page_selection_check = False
                    settings_check =False
                    extracting_option_check = False
                else:
                    # extracting_option = "All pages" #extracting_prompt["Extracting"]
                    page_selection_check = True
                    settings_check =False
                    extracting_option_check = True
            # else:
                # selected_pages = selecting_pages(num_pages)
                # select_pages(selected_pages,selected_pdf)

                
        # select_pages(selected_pages,selected_pdf)


    # console.print(f"[bold green]👍 PDF pages from \[{selected_pdf}] extracted successfully! \n")


# for selected_pdf in selected_pdfs:
#     console.print(f"[green]you are currently working on `{selected_pdf}`\n")
#     reader = PdfReader(selected_pdf)
#     output_folder = 'pdf_pages'
#     num_pages = len(reader.pages)
#     # with open(selected_pdf, 'rb') as pdf_file:

#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     if extracting_option== "All pages":
#         all_pages()
#     elif extracting_option == "Select pages to extract":
#         selected_pages = selecting_pages(num_pages)

#         select_pages(selected_pages)


#     print(f"PDF pages from [{selected_pdf}] extracted successfully! 👍\n")

