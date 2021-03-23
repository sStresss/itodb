import pytesseract
from PIL import Image
import cv2
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




filename = 'C:/1/4.jpeg'
im_gray = cv2.imread(filename)

width = im_gray.shape[1]
height = im_gray.shape[0]

print(width, height)

# im_gray = cv2.colorChange(im_gray, cv2.COLOR_RGB2BGR)

im_gray = cv2.resize(im_gray, (width*15, height*15))

filename_new = 'C:/1/new.jpeg'

cv2.imwrite(filename_new, im_gray)


# time.sleep(3)
text = pytesseract.image_to_string(Image.open(filename_new))
print(text)