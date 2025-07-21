""" Merges pdfs with a CLI interface """

import os
from pypdf import PdfWriter
import inquirer
from pprint import pprint
import sys
# pdfs = [a for a in os.listdir() if a.endswith(".pdf")]
# #pdfs =['01.pdf','output.pdf' ]
# merger = PdfMerger()

# for pdf in pdfs:
#     merger.append(pdf)

# merger.write("result.pdf")
# merger.close()

# print(pdfs)
def main():

    questions = [
        inquirer.Checkbox(
            "pdfs",
            message="Select the pdfs that you wish to merge (right arrow to select, left arrow to deselect):",
            choices=[a for a in os.listdir() if a.endswith(".pdf")],
        ),
    ]
    # while True:
        # try:
    answers = inquirer.prompt(questions)
    if answers is None:
        sys.exit(0)
    pdfs =  [j for i in answers.values() for j in i]
    print(pdfs)

    merger = PdfWriter()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()
    # break # ensures that the loop only runs once. since we didn't implement a exit option.

        # except EOFError:
            # print("this was maybe ctrl + d")
            # sys.exit(0)
        # except KeyboardInterrupt:
            # print("this was maybe ctrl + c")
            # sys.exit(0)

if __name__ == "__main__":
    main()

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
