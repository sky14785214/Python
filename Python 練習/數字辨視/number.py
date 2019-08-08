import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
image = Image.open(r"E:\GitHub\keras-yolo3-master\car_card.jpg")
text = pytesseract.image_to_string(image)
print(text)