from PyPDF2 import PdfFileMerger
CPDF= ["1.pdf", "1.pdf"]

mymerger = PdfFileMerger()

for MyPDF in CPDF:
    mymerger.append(MyPDF)

mymerger.write("Rex.pdf")
mymerger.close()