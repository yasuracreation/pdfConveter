import sys

import PyPDF2

output = PyPDF2.PdfFileWriter()

waterPdf = sys.argv[1]
orgPdf = sys.argv[2]
outputPdf = sys.argv[3]

ipdf = PyPDF2.PdfFileReader(open(orgPdf, 'rb'))
wpdf = PyPDF2.PdfFileReader(open(waterPdf, 'rb'))


def addWaterMark(inputPdf, waterMark, outputPdfName):
    for i in range(ipdf.getNumPages()):
        waterPage = waterMark.getPage(0)
        page = inputPdf.getPage(i)
        page.mergePage(waterPage)
        output.addPage(page)
    with open(outputPdfName, 'wb') as f:
        output.write(f)


addWaterMark(ipdf, wpdf, outputPdf)
