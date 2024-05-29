from pypdf import PdfWriter, PdfReader

reader = PdfReader("result.pdf")
writer = PdfWriter()

for i in range(len(reader.pages)):
    writer.add_page(reader.pages[i])
    if i in [4,5,6,7,8]:
        writer.pages[i].rotate(-90)

with open("output.pdf", "wb") as fp:
    writer.write(fp)
