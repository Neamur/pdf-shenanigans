# PDF Shenanigans (numbering) 
---
This code base is all about manipulating pdfs with code. 


Trying avoid paying for subscription fees and stuff.


- [ ] gotta add comments to `scritp.py` -> is about merging pdfs.
- [X] `rotator_inq.py` is done.
- [ ] `rotator_complex.py` is NOT done.
- [ ] splitting pages in inq mode.
- [X] extracting pages in inq mode.
- [ ] `numbering pages` has to be made in inquirer
    - [ ] other functionalities are still left to be implemented. see `numbering pages` section below
- [ ] 

## `numbering pages` AKA `orientation.py` (current iteration; figured out the orientation issue.)
---
- ask the user with what number to start numbering, `default=1`
- option to the user to select which features they want to work with, then give options to input values for those features.
    - eg: 
    ```python 
    select the features:
    [ ] numbering index
        - nani? what did i mean by this?
    [ ] num of pages to number
    [ ] upto which page to number
    [ ] fonts
        [ ] selection option that presents all the available fonts.
        [ ] font size option that promts the user to input a font size. (set a hard limit on the size range. maybe 4-150.)
        [ ] give option to choose from B , I , U, None.
        [ ] 
    [X] position
        For the 'Highlighted' option, could not be bothered to figure out how to centre the cell with any of the methods available (pulled my hair out for 3 days straight), just resorted to placing the xpos to centre of the pdf and calling it a day.
    [ ] number only select pages from the pdf.
        [ ] give the user 2 options to number the select pages.
            [ ] keep the numbering count from the start of the pdf.
            [ ] numbering count seperately for the selected pdf pages.
        [ ] show the pages as a list form in the inquirer checkbox format, for the user to select from.
        ```

- [X] set the font type to orange fill with white stroke.

- ~~[] make a var set the `header`/`footer` based on the `position[0]` value.~~
    - i think i will just stick to using the footer func for now since i don't wanna repeat bunch of code just to have a header.
        - no need to add any more bloat than what i already have.
- ~~[] `nex_x` pos for the `cell` should be done only when the highlighted version is drawn in `center`/`right side`.~~
    - there is no requirement for this since we have switched to using the pdf width for the alignment. 👍
- [ ] change the `ON_PAGE_INDEX` to 1 instead of 0, then just do `on_page_index - 1 < len(reader.pages)`
    - this is cus the user may wish to number the last page only, so, if the page_index is 0, then it will not enter the loop and thus the page wont get numbered.

    - `pdf.set_right_margin(pdf.w - right_boundary)` --> this shows us that there is a pdf.w which gives the width of the page 👍
- [X] repeat the pdf menu if the user has not selected a pdf file to work with.


### Notes
- Dude, why this pypdf got a goofy aahhh coordinate system? who takes the bottom left corner as the origin. 
    - it is diff from the fpdf one. *sigh 😔 
- For the orientation issue, applying `transfer_rotation_to_content` doesn't seem to help.
    - will try setting new page coordinates this time or maybe the rotate counter clockwise.
        - doesn't exist
    - update: [31/5/2024] `transfer_rotation_to_content` from `pypdf` does work when setting page orientation to `L` in `fpdf`.
### Test cases
- [ ] single pdf
    - [ ] Top
        - [ ] Left
        - [ ] Centre
        - [ ] Right
    - [ ] Bottom
        - [ ] Left
        - [ ] Centre
        - [ ] Right
- [ ] 2 pdf
    - [ ] Top
        - [ ] Left
        - [ ] Centre
        - [ ] Right
    - [ ] Bottom
        - [ ] Left
        - [ ] Centre
        - [ ] Right
---
## Rotating pdfs.
- [X] complete.
### Rotating complex.
- [ ] lots of bugs in the system! Note all the behavioural issues and then find a fix for it.

### Features to add.
- [ ] give options to choose rotate all pages by selected angle.
- [ ] option to choose pages of a pdf from selected pdfs and rotate them by selected angle.
    [X] option to select pdf and apply selected angle to it.

    [X] option to apply the same settings to rest of the pdfs.

    [X] error handling for when the page is out of range after one asks for the rotation to be applied to all the pdfs for selected page numbers based on the first pdf.
        - [X]~~Just skips to the next one since there is no page to rotate, it goes on to the next one without rotating anything.~~
            - [X] now doesn't make a new roated-{pdf} when the pages selected are out of range for the current pdf.
## Rotating pages.

## Extracting pages.
- ### exhausted with this, lets turn back to font styling (pdf numbering) date:25/5/2024
- [X] give the user the option to select the pages to extract.
    this one is about extracting pages.

    ```txt
        [?]Extracting
            |_ All
            |_ select pages.
    ```
- [X] ⚠️ **Warning**: unable to extract [Page 12] from [xyz.pdf] with only [num_of_pages] pages
    - Give this warning when the user set the apply same settings to all, and the pdf doesn't have the selected page number.
    - [X] **Implenentation**: grab the page num during the `except` in the try and except block during extraction, then return that page number for the error message. Additionaly, the `num_pages` from the current for loop, also the `pdf name` in the current loop.
- [X] Ask once whether to apply same settings or not, then based on answer show the option to select pages for the next pdf/s.
- [ ] Show inquirer based file navigation option to the user to navigate to the folder and select that as the working folder instead of setting the current folder as the working folder.
    - [ ] set this in a sep branch called `cli exe`.
    - [ ] just set it as a env variable in the system env vars. 
### NOTE
-  as of writing, all the functionalities seem to work except for one case. thus i have disabled that case.
    - too tired to fix that right now, it goes >= 2 PDFs  -> all_pages() -> Same settings -> No -> applies to all of the pdfs
    - Basically, doesn't follow the order of operations.
    - Should be: No -> give option in the next pdf to select individual pages / all_pages again.
- Thus right now when you select all pages, it applies that settings to all the selected pdfs.
- update: [29/05/2024] gives the user to select "extraction method" after the user enters "No" for "same settings"
- update: [29/05/2024] just converted to exe with `pyinstaller`.
- update: [04/05/2025] so the compile cli command needs --collect-all readchar for the program to properly compile in linux for the merger script.
  the collect all command is to copy the metadata properly.
  
### Test Cases
- [X] 1 PDF
    - [X] all_pages()
    - [X] 2,4,8
    - [X] 1,3,5
    - [X] last page
    - [X] first page
    - [X] all pages in the pdf selected individually
- [ ] 2 pdfs
    - [ ] same settings (apply same settings == "YES")
        - [ ] all_pages()
        - [ ] 2,4,8
        - [ ] 1,3,5
        - [ ] last page
        - [ ] first page
        - [ ] each page selected individually
        - [ ] test if the warning is given incase the second pdf doesnt have a page selected by the user.
            - [ ] allow user to re-enter the pages for that particular pdf.
            - [ ] re-show the same_settings() method call
    - [ ] diff settings
        - [ ] all_pages()
        - [ ] 2,4,8
        - [ ] 1,3,5
        - [ ] last page
        - [ ] first page
        - [ ] each page selected individually
        - [ ] show the option to select the same settings for the rest of the pdfs.

## Splitting pdf/pages.
- [ ] give the user the option to select the pages to split as a seperate pdf file.

    ```txt
        [?]Splitting
            |_ select pages that you wish split and create a new pdf.
    ```

## Removing pages.
- [ ] Option to remove certain pages from the pdf and save that as a new pdf.

    ```txt
        [?]Removing pages.
            |_ select pages to Remove.
    ```
## Compressing pdf.
- [ ] lossless compression
- [ ] jpeg compression
    - [ ] quality selector (80%,40%, etc )

## Organizing Pdf.
- [ ] show the pages to select
    - [ ] add the pages selected to the top of the pdf, then the unselected ones in the original order. (check notes for logic)

## Packaging it as an application
---
- [ ] make it a pypi package
- [ ] windows app with either QT, Tinker, or Briefcase
- [ ] compiled app for cli with Pyinstaller or Click. 
- [simple article showing various packaging libraries](https://www.blog.pythonlibrary.org/2021/05/27/pyinstaller-how-to-turn-your-python-code-into-an-exe-on-windows/). this article focuses on Pyinstaller.
- update: [04/05/2025] so the compile cli command needs --collect-all readchar for the program to properly compile in linux for the merger script.
  the `collect all` command is to copy the metadata properly.
- update: [15/05/2025] same for windows.
- update: [18/05/2025] `--copy-metadata` does the same.

### Linux
- [ ] merger is now a stanalone application for linux. 
    
    `pyinstaller -D -F --collect-all readchar -n merger "scritp.py"`

to add the program to your user and allow systemwide usage only for that user.
- `cp /path/to/your/pdfnumbering ~/.local/bin/`
- `source ~/.bashrc`

### Windows
- example cli command to compile:
`pyinstaller --copy-metadata readchar -n merger_win "scritp.py" --onefile`

- To add the exe as a cli application to be accessed system wide, you may choose to add it to your path. 
    - to do so, search `edit the system environment variables` -> `Environment Variables` -> `Path` -> `Edit` -> `New` 
    - now paste in the file path where your exe is located. 
- had to use `pyinstaller -p "Lib/site-packages" --copy-metadata readchar -n merger_windows scritp.py --onefile` this time around. weird.
    - that readchar is a submodule that inquirer calls, guessing based on the error.
 
## package versions (requirements.txt)
```
PyPDF4==1.27.0
pypdf==4.2.0
rich==13.7.1
inquirer==3.2.4
pdfnumbering==0.1.1
readchar===4.0.6
```

## Notable bugs in exes.

- [ ] ctr + c doesn't exit gracefully either. 
    - [ ] merger
    - [ ] extract
    - [ ] rotate_complex.py
    - [X] scritp.py
    - [X] rotator_inq.py

