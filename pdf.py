# -*- coding:utf-8 -*-

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from PyPDF2.pdf import PdfFileWriter, PdfFileReader

class Pdf_solve():
    def createNewBooks(self, pdf_file, stPage, endPage, filename='my.pdf'):
        input = PdfFileReader(open(pdf_file,"rb"))
        if input.isEncrypted: #注意：所有的pdf，pypdf2默认都是加密形式，所以要先解密再读取
            input =input.decrypt('')
        pdf_input = input
        pdf_output = PdfFileWriter()
        i = stPage
        while i < endPage:
            page = pdf_input.getPage(i)  # 选取需要页面，需要注意的是第一页的编号是0
            pdf_output.addPage(page)  # 将选好的页面加入到新的pdf中
            i += 1
        output_stream = open(filename, 'wb')
        pdf_output.write(output_stream)
        output_stream.close()

        return 'Complete knifing'
    def merge(self, pdf_one, pdf_two, filename='my.pdf', output_dir='D:/pdf/'):
        '''
        function:#pdfone为扫描的正面；#pdftwo为扫描的背面；#本函数实现将两个扫描文件按原有的顺序合并起来
        :param pdf_one:
        :param pdf_two:
        :param filename:
        :param output_dir:
        :return:
        '''
        input_one = open(pdf_one, 'rb')
        input_two = open(pdf_two, 'rb')
        pdf_input_one = PdfFileReader(input_one)
        pdf_input_two = PdfFileReader(input_two)
        numOne = pdf_input_one.getNumPages()
        numTwo = pdf_input_two.getNumPages()
        print(numOne, numTwo)
        pdf_output = PdfFileWriter()
        index_one = 0
        index_two = numTwo - 1
        while True:
            if index_one == numOne: break
            print(index_one, index_two)
            page1 = pdf_input_one.getPage(index_one)
            pdf_output.addPage(page1)
            page2 = pdf_input_two.getPage(index_two)
            pdf_output.addPage(page2)
            index_one += 1
            index_two -= 1
        pdf_name = output_dir + filename
        output_stream = open(pdf_name, 'wb')
        pdf_output.write(output_stream)
        output_stream.close()
        input_one.close()
        input_two.close()
        print('Done!')
    def convert_pdf_to_txt(self, path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()
        fp.close()
        device.close()
        retstr.close()
        return text

if __name__ == "__main__":
    test = Pdf_solve()
    test.createNewBooks("mouse.pdf",48,150,"Figure.pdf")
