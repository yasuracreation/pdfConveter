import PyPDF2
import sys

args = sys.argv
merger = PyPDF2.PdfFileMerger()
counter = 0
for arguments in args:
    if counter > 0:
        merger.append(PyPDF2.PdfFileReader(arguments, 'rb'))
    counter += 1

merger.write("merged.pdf")
