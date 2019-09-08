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
        counter = 0
        for root, dirs, files in os.walk(dirpath):                
                for filename in sorted(files):
                        print(str((100*counter)/len(files))+"% done")
                        if filename.endswith('pdf'):
                                pdftotxt(filename)
                                counter = counter+1

'''
f2015 = "/home/ndc/repos/TCC/src/contracts/2015 - 204 arquivos"
f2016 = "/home/ndc/repos/TCC/src/contracts/2016 - 1199 arquivos"
f2017 = "/home/ndc/repos/TCC/src/contracts/2017 - 641 arquivos"
f2018 = "/home/ndc/repos/TCC/src/contracts/2018 - 771 arquivos"
f2019 = "/home/ndc/repos/TCC/src/contracts/2019 - 417 arquivos"
'''

#wipe_pdfs_dir(f2015)
#wipe_pdfs_dir(f2016)
#wipe_pdfs_dir(f2017)
#wipe_pdfs_dir(f2018)
#wipe_pdfs_dir(f2019)