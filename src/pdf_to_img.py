import os
directory="/home/ndc/repos/TCC/src/contratos/2016 - 1199 arquivos"
x=os.walk(directory)

[print(x[0]) for x in os.walk(directory)]



from PIL import Image
import pytesseract
text = pytesseract.image_to_string(Image.open('image.jpg'))