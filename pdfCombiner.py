import PyPDF2
import sys

inputs = sys.argv[1:]

merger = PyPDF2.PdfFileMerger()


def pdfCombiner(pdf_list):
    for pdf in pdf_list:
        merger.append(pdf, 'rb')
    merger.write("comb.pdf")


pdfCombiner(inputs)
