import os
directory="/home/ndc/repos/TCC/src/contratos/2016 - 1199 arquivos"
#from PIL import Image
import pytesseract

#Gets as input the path to a pdf as string and outputs it's pages as png files in the same directory the pdf file is
def pdftopng(pdfpath):
        filepath = os.path.abspath(pdfpath)
        os.system('pdftoppm '+filepath+' '+os.path.dirname(filepath)+'/pg -png')



rootdir = '.'
#Apply OCR to all .png images in a rootdir to a single .txt file
#Deletes the .png files at the end
for subdir, dirs, files in sorted(os.walk(rootdir)):
        text = ''
        for file in sorted(files):
                if file.endswith('png'):
                        print(os.path.join(subdir, file))
                        page_content = pytesseract.image_to_string(Image.open(os.path.join(subdir, file)),lang='por')
                        text = text+page_content
        filepath = os.path.join(subdir, 'text.txt')
        f = open(filepath,"w")
        f.write(text)
        f.close()
        os.system('rm pg*.png')
        print(filepath)
        print('------------------------')                