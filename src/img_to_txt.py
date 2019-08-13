from PIL import Image
import pytesseract
import os



rootdir = '.'

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
        print(filepath)
        print('------------------------')                