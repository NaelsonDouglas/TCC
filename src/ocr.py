import os
import subprocess
from pathlib import Path
import shutil
import Image
from PIL import Image
import pytesseract


#Gets as input the path to a pdf as string and outputs it's pages as png files in the same directory the pdf file is
def pdftopng(pdfpath):
        filepath = os.path.abspath(pdfpath)
        file_basename = Path(pdfpath).stem
        
        
        if os.path.exists(file_basename):
                shutil.rmtree(file_basename)
        os.mkdir(file_basename)
        dest_path = os.path.dirname(filepath)+'/'+file_basename
        imgs_out_path = dest_path+'/'+file_basename+'/'+file_basename+'-pg'
        fmt = '-png'        
        
        subprocess.call(['pdftoppm', filepath,imgs_out_path,fmt])
        shutil.copy(pdfpath,dest_path)   
        return dest_path        
        
pdftopng(f)

def imgstotxt(imgsdir='/home/ndc/repos/TCC/src/contracts/testes/arquivo A/'):                   
        for subdir, dirs, files in sorted(os.walk(imgsdir)):
                text = ''
                imgs_path = ''               
                for file in sorted(files):
                        if file.endswith('png'):
                                print(os.path.join(subdir, file))
                                page_content = pytesseract.image_to_string(Image.open(os.path.join(subdir, file)),lang='por')
                                page_content = page_content.replace('\n\n','\n')                                
                                text = text+page_content
                filepath = os.path.join(subdir, 'text.txt')
                f = open(filepath,"w")
                f.write(text)
                f.close()
                #os.system('rm pg*.png')
                print('                 <->')
                print(filepath)
                print('------------------------')
                


imgstotxt()