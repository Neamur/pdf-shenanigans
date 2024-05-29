from rich.console import Console
console = Console()

"""just rotator_inq.py but with more options for the user."""

""" 
Features i want to implement.

> select pdfs
> rotation angle
> apply to all the pages?
    > yes
        rotate all pages by selected angle
    > no
        select pages to rotate by selected angle
> You have selected [xyz.pdf,bxy.pdf]
> You have selected to rotate by -90 degree
> You have selected these pages: Page 1 ,Page 2 to rotate from the xyz pdf
> Do you wish to apply the same rotation and to the same pages from the rest of the pdfs?

> apply to all the pdfs?
    > apply to all pages
        yes
            rotate all pdfs 
        no
            rotation angle for the next pdf
            apply to all pages? for the next pdf
    > selected pages
        yes
            rotate all the pdfs with same selected pages
        no
            rotation angle for the next pdf
            apply to all pages? for the next pdf

- [x] func to get pdfs
    - outpts list of selected pdfs
- [x] looks like we need a func to get the rotation angle from the user
    - [x] then a var to hold tht value in case we need to reapply the same rotation angle for all pages or select pages
    - func to get rotation angle
        - [x]outputs selected rotation angle.
- func to rotate pages. 
    - [x]takes in individual page as an arg outputs rotated page.
- [x] func to get pages.
    -> input pdf -> outputs selected pages in a list
- func to rotate all pdfs
    -> input list of all the selected pdfs -> outputs rotated pdfs.
        - rotate_all_pdfs(selected_pdfs, rotation_angle):
            for pdf in selected_pdfs:
                the current code we already have.
- func to rotate few pages
    -> rotate_few_pages(selected_pdf, selected_pages) #selected_pages -> [j for i in anwers.values() for j in i]
        - put this in a for loop for selected_pdf in pdfs:
        - let the selected_pages be a const
    - no need for this if we just do something like :-
        for current_page in range(len(reader.pages)):
            if f"Page {current_page+1}" in selected_pages[4:]:
                rotate_pages(reader.pages[current_page])
        - this does seem too clunky tho. feels like jumping back and forth between the func and main code.


"""

import os
from pypdf import PdfWriter, PdfReader
import inquirer
import pprint

pp = pprint.PrettyPrinter(indent=4)

# dict of pdfs that the user wants to rotate
def get_pdfs():
    question = [
        inquirer.Checkbox(
            "pdfs",
            message="Select the pdfs that you wish to rotate (right arrow to select, left arrow to deselect):",
            choices=[a for a in os.listdir() if a.endswith(".pdf")],
        ),
    ]

    # idk wht the bottom line does
    answers = inquirer.prompt(question)    # most likely prompts the user 🤯
    pdfs =  [j for i in answers.values() for j in i]    # list of the options the user selected
    # print("selected pdfs are -> ",pdfs,"\n")          # you can use this line instead of the 2 lines written below and remove a module (pretty print/ pprint) thus making this code base lighter and faster. 🤯
    console.print("[blue]selected pdfs are :")
    console.print(pdfs)
    return pdfs

def rotation():
    rotator_angles = [inquirer.List("angles", message="by what angle do you wish to rotate? (rotation in clockwise)", choices=[90, 180,270,-90,-180,-270])]  # gives option to the user to choose an angle that is multiple of 90.
    rotator_angle = inquirer.prompt(rotator_angles)     # prompts the user to select the angle 
    rot_angle = rotator_angle['angles']     # var tht holds the angle selected by user
    print("selected angle -> ",rot_angle)       #prints angle selected by user
    return rot_angle

# rot_angle = rotation()
# hold_rotation_angle = rot_angle 
# print(rot_angle)

def rotate_page(selected_page,rot_angle):
    writer.pages[selected_page].rotate(rot_angle)

def get_pages(num_pages):
    pages_option = [
    inquirer.Checkbox(
        "pages",
        message="Select the Pages that you wish to rotate (right arrow to select, left arrow to deselect):",
        choices=[f"Page {a+1}" for a in range(num_pages)],
    ),]

    # idk wht the bottom line does
    prompt_pages_option = inquirer.prompt(pages_option)    # most likely prompts the user 🤯
    selected_pages =  [j for i in prompt_pages_option.values() for j in i]    # list of the options the user selected
    # print("selected pdfs are -> ",pdfs,"\n")          # you can use this line instead of the 2 lines written below and remove a module (pretty print/ pprint) thus making this code base lighter and faster. 🤯
    console.print("[blue]selected pages are :")
    pp.pprint(selected_pages)
    return [int(i[4:])-1 for i in selected_pages]
def rotate_pdfs(selected_pdfs,rot_angle):
    for pdf in selected_pdfs:
        reader = PdfReader(f"{pdf}")
        writer = PdfWriter()
        num_pages = len(reader.pages)
        rotation()
        print(hold_rotation_angle)
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])
            writer.pages[i].rotate(rot_angle)
        # with open(f"rotated-{pdf}", "wb") as fp:
        writer.write(f"rotated-{pdf}")
        print(f"Successful with {pdf}👍")

def apply_to_pdfs_ques():
    apply_to_pdfs = [inquirer.List("apply_all_pdfs", message="do you wish to apply the settings to all the pdfs", choices=["Yes","No"])]  # gives option to the user to choose an angle that is multiple of 90.
    apply_to_pdfs_prompt = inquirer.prompt(apply_to_pdfs)     # prompts the user to select the angle 
    user_reply = apply_to_pdfs_prompt['apply_all_pdfs']     # var tht holds the angle selected by user
    console.print("[blue]You have choosen -> ",user_reply)       #prints angle selected by user
    return user_reply, ["Yes","No"]
 
# def apply_to_pages_ques():
def apply_to_pages_ques():
    apply_to_pages = [inquirer.List("apply_all_pages", message="do you wish to apply the settings to all the pages", choices=["Yes","No"])]  # gives option to the user to choose an angle that is multiple of 90.
    apply_to_pdfs_prompt = inquirer.prompt(apply_to_pdfs)     # prompts the user to select the angle 
    user_reply = apply_to_pdfs_prompt['apply_all_pages']     # var tht holds the angle selected by user
    console.print("[blue]You have choosen -> ",user_reply)       #prints angle selected by user
    return user_reply, ["Yes","No"]

def option_all_few():
    """ displays option for the user to choose between 
    1) all pages  
    2) select pages"""
    option = [inquirer.List("all_or_not", message="How do you wish to apply the rotation?", choices=["Apply to all pages","let me select pages"])]  # gives option to the user to choose an angle that is multiple of 90.
    apply_to_all_prompt = inquirer.prompt(option)     # prompts the user to select the angle 
    user_reply = apply_to_all_prompt['all_or_not']     # var tht holds the angle selected by user
    print("You have choosen -> ",user_reply)       #prints angle selected by user
    return user_reply, ["Apply to all pages","let me select pages"]






if __name__ == "__main__": 
    pdfs = get_pdfs()   # option to select pfds
    # print(f"you are currently working on : {pdfs[0]}")

    rot_angle = rotation()  # angle to rotate by
    hold_rotation_angle = rot_angle 
    print(rot_angle)
    
    for pdf in pdfs:
        reader = PdfReader(f"{pdf}")
        writer = PdfWriter()
        num_pages = len(reader.pages)
        # rotation()
        # print(hold_rotation_angle)
        console.print(f"[bold green]You are currently working on : \[{pdf}]")
        selected_option, selected_options = option_all_few()         # apply to all pages/select pages? 
        if pdf == pdfs[0] and selected_option == selected_options[0]:
            all_pdfs, apply_to_pdfs_option = apply_to_pdfs_ques()




        if all_pdfs == "Yes" and selected_option == selected_options[0]:
            rotate_pdfs(selected_pdfs=pdfs,rot_angle=rot_angle)

        elif all_pdfs == "No" and selected_option == selected_options[0]:
            for i in range(num_pages):
                writer.add_page(reader.pages[i])
                writer.pages[i].rotate(rot_angle)
            writer.write(f"rotated-{pdf}")
        elif all_pdfs == "Yes" and selected_option == selected_options[1]:
            selected_pages = get_pages(num_pages=num_pages)
            # all_pdfs, apply_to_pdfs_option = apply_to_pdfs_ques()
            for i in range(num_pages):
                writer.add_page(reader.pages[i])
                if i in selected_pages:
                # current_page_index = int(i[4:])-1
                    writer.pages[i].rotate(rot_angle)  
            # with open(f"rotated-{pdf}", "wb") as fp:
            writer.write(f"rotated-{pdf}")
        elif all_pdfs == "No" and selected_option == selected_options[1]:
            for i in range(num_pages):
                writer.add_page(reader.pages[i])
                writer.pages[i].rotate(rot_angle)
            writer.write(f"rotated-{pdf}")
        console.print(f"[bold green]Successfully rotated \[{pdf}] 👍\n")

        


# no idea wht i wrote here below, didnt comment on tht code base(scritp.py)
# for pdf in pdfs:
#     reader = PdfReader(f"{pdf}")
#     writer = PdfWriter()
#     num_pages = len(reader.pages)
#     rotation()
#     print(hold_rotation_angle)
#     for i in range(len(reader.pages)):
#         writer.add_page(reader.pages[i])
#         writer.pages[i].rotate(rot_angle)
#     with open(f"rotated-{pdf}", "wb") as fp:
#         writer.write(fp)
# print("Successful 👍")

