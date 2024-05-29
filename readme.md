# PDF Shenanigans (numbering) 
---
This code base is all about manipulating pdfs with code. 


trynna avoid paying subscription fees and stuff


- [ ] gotta add comments to `scritp.py` -> is about merging pdfs.
- [X] `rotator_inq.py` is done.
- [ ] splitting pages in inq mode.
- [X] extracting pages in inq mode.
- [ ] `numbering pages` has to be made in inquirer
    - [ ] other functionalities are still left to be implemented. see `numbering pages` section below
- [ ] 

## `numbering pages`
---
- ask the user with what number to start numbering, `default=1`
- option to the user to select which features they want to work with, then give options to input values for those features.
    - eg: ```python 
    select the features:
    - [ ] numbering index
        - nani? what did i mean by this?
    - [ ] num of pages to num
    - [ ] upto which page to number
    - [ ] fonts
        - [ ] selection option that presents all the available fonts.
        - [ ] font size option that promts the user to input a font size. (set a hard limit on the size range. maybe 4-150.)
        - [ ] give option to choose from B , I , U, None.
        - [ ] 
    - [X] position
        - For the 'Highlighted' option, could not be bothered to figure out how to centre the cell with any of the methods available (pulled my hair out for 3 days straight), just resorted to placing the xpos to centre of the pdf and calling it a day.
    - [ ] number only select pages from the pdf.
        - [ ] give the user 2 options to number the select pages.
            - [ ] keep the numbering count from the start of the pdf.
            - [ ] numbering count seperately for the selected pdf pages.
        - [ ] show the pages as a list form in the inquirer checkbox format, for the user to select from.```

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
- For the orientation issue, applying `transfer_rotation_to_content` doesnt seem to help.
    - will try setting new page coordinates this time or maybe the rotate counter clockwise.
        - doesnt exist
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
### Features to add.
- [ ] give options to choose rotate all pages by selected angle.
- [ ] option to choose pages of a pdf from selected pdfs and rotate them by selected angle.
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
- [ ] "⚠️ **Warning**: unable to extract [Page 12] from [xyz.pdf] with only [num_of_pages] pages"
    - give this warning when the user set the apply same settings to all, and the pdf doesnt have the selected page number.
- [X] ask once whether to apply same settings or not, then based on answer show the option to select pages for the next pdf/s.
### NOTE
-  as of writing, all the functionalities seem to work except for one case. thus i have disabled that case.
    - too tired to fix that right now, it goes 2 PDF +  -> all_pages() -> Same settings -> No -> applies to all of the pdfs
    - Basically, doesn't follow the order of operations.
    - should be No -> give option in the next pdf to select individual pages / all_pages again.
- thus right now when you select all pages, it applies that settings to all the selected pdfs.
- update: [29/05/2024] gives the user to select "extraction method" after the user enters "No" for "same settings"
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
