import os
from pypdf import PdfMerger
import inquirer
from pprint import pprint
# pdfs = [a for a in os.listdir() if a.endswith(".pdf")]
# #pdfs =['01.pdf','output.pdf' ]
# merger = PdfMerger()

# for pdf in pdfs:
#     merger.append(pdf)

# merger.write("result.pdf")
# merger.close()

# print(pdfs)

questions = [
    inquirer.Checkbox(
        "pdfs",
        message="Select the pdfs that you wish to merge (right arrow to select, left arrow to deselect):",
        choices=[a for a in os.listdir() if a.endswith(".pdf")],
    ),
]
    
answers = inquirer.prompt(questions)
pdfs =  [j for i in answers.values() for j in i]
print(pdfs)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()


## by the 4B qwen
# print([j for i in answers.values() for j in i]))



## this block of code just gives each element instead of a list
# for i in answers.values():
#     for j in i:
#         print(j)



## by qwen 1.8B
# answer_combinations = [v for k, v in answers.items()]
# # print(answer_combinations)
# for combination in answer_combinations:
#     print(combination)
