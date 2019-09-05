from PIL import Image
from pathlib import Path
import os
import subprocess
import shutil
import pytesseract


#Gets as input the path to a pdf as string and outputs it's pages as png files in the same directory the pdf file is
def pdftopng(pdfpath):
        filepath = os.path.abspath(pdfpath)
        file_basename = Path(pdfpath).stem
        
        
        if os.path.exists(file_basename):
                shutil.rmtree(file_basename)
        os.mkdir(file_basename)
        dest_path = os.path.dirname(filepath)+'/'+file_basename
        imgs_out_path = dest_path+'/'+file_basename+'-pg'
        fmt = '-png'        
        
        subprocess.call(['pdftoppm', filepath,imgs_out_path,fmt])
        shutil.move(pdfpath,dest_path)   
        return dest_path,file_basename    
        

def imgstotxt(imgsdir=['/home/ndc/repos/TCC/src/contracts/testes/arquivo A/','arquivo A']):                   
        for subdir, dirs, files in sorted(os.walk(imgsdir[0])):
                text = ''                       
                for file in sorted(files):
                        if file.endswith('png'):
                                file_fullpath = os.path.join(subdir, file)
                                print(file_fullpath)
                                page_content = pytesseract.image_to_string(Image.open(file_fullpath),lang='por')
                                page_content = page_content.replace('\n\n','\n')                                
                                text = text+page_content
                filepath = os.path.join(subdir, imgsdir[1]+'.txt')
                f = open(filepath,"w")
                f.write(text)
                f.close()
                #query_matchimgs = imgsdir[0]+'*.png'
                #subprocess.call(['rm', query_matchimgs])
                print('                 <->')
                print(filepath)
                print('------------------------')
                return filepath

def pdftotxt(pdfpath):
        imgs_output = pdftopng(pdfpath)        
        imgstotxt(imgs_output)



def wipe_pdfs_dir(dirpath):
        os.chdir(dirpath)
        for root, dirs, files in os.walk(dirpath):                
                for filename in files:
                        if filename.endswith('pdf'):
                                pdftotxt(filename)



a = "/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"
b = "/home/ndc/repos/TCC/src/contracts/2016 - 1199 arquivos"
c = "/home/ndc/repos/TCC/src/contracts/2017 - 641 arquivos"
d = "/home/ndc/repos/TCC/src/contracts/2018 - 771 arquivos"
e = "/home/ndc/repos/TCC/src/contracts/2019 - 417 arquivos"

wipe_pdfs_dir(a)
wipe_pdfs_dir(b)
wipe_pdfs_dir(c)
wipe_pdfs_dir(d)
wipe_pdfs_dir(e)