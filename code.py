import cv2
import pytesseract
import base64

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img  = cv2.imread('img4.jpg')
text = pytesseract.image_to_string(img)
print(text)

def encodeDecode(img):
    image = open('image.png', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    print(image_read)
    image_64_decode = base64.decodestring(image_64_encode) 
    image_result = open('image_decode.png', 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)


