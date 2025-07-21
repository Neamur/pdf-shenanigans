"""just rotator.py but with the cli interface giving options to users."""

import os
from pypdf import PdfWriter, PdfReader
import inquirer
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)

# dict of pdfs that the user wants to rotate
questions = [
    inquirer.Checkbox(
        "pdfs",
        message="Select the pdfs that you wish to rotate (right arrow to select, left arrow to deselect):",
        choices=[a for a in os.listdir() if a.endswith(".pdf")],
    ),
]

# idk wht the bottom line does
answers = inquirer.prompt(questions)    # most likely prompts the user 🤯
if answers == None:
    sys.exit(0)
pdfs =  [j for i in answers.values() for j in i]    # list of the options the user selected
# print("selected pdfs are -> ",pdfs,"\n")          # you can use this line instead of the 2 lines written below and remove a module (pretty print/ pprint) thus making this code base lighter and faster. 🤯
print("selected pdfs are :")
pp.pprint(pdfs)

rotator_angles = [inquirer.List("angles", message="by what angle do you wish to rotate?", choices=[90, 180,270,-90,-180,-270])]  # gives option to the user to choose an angle that is multiple of 90.
rotator_angle = inquirer.prompt(rotator_angles)     # prompts the user to select the angle 
rot_angle = rotator_angle['angles']     # var tht holds the angle selected by user
print("selected angle -> ",rot_angle)       #prints angle selected by user

# no idea wht i wrote here below, didnt comment on tht code base(scritp.py)
for pdf in pdfs:
    reader = PdfReader(f"{pdf}")
    writer = PdfWriter()
    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])
        writer.pages[i].rotate(rot_angle)
    with open(f"{pdf}", "wb") as fp:
        writer.write(fp)
print("Successful 👍")
