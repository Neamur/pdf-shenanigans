from numbering2pdf import add_numbering_to_pdf
import pypdf
import inquirer
import os

# pdfs = [a for a in os.listdir() if a.endswith(".pdf")]

# questions = [
#   inquirer.List('pdf files',
#                 message="which pdf to number?",
#                 choices=[a for a in os.listdir() if a.endswith(".pdf")],
#             ),
# ]
# answers = inquirer.prompt(questions)
# pdfs =  [i for i in answers.values()]
# print(pdfs)
# print(answers)

# filename= input('enter the file name to number (without the .pdf): ')
# add_numbering_to_pdf(f"{pdfs[0]}", "numbered.pdf")
# num_pages = len(reader.pages)
# for page_num in range(len(pdfs)):
    # add_numbering_to_pdf(f"{pdfs[page_num]}", f"{pdfs[page_num]}",position="right",font="Courier", start_index=page_num+1)

# for i in range(29):
#     add_numbering_to_pdf(f"page_{i+1}.pdf", f"numbered{i+1}.pdf", start_index=i+1)

add_numbering_to_pdf("page_5.pdf", "numbered_5.pdf")

