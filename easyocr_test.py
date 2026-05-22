from easyocr import Reader
from preprocessing import preprocess_image

reader = Reader(['en'])
img_path = './images/test_img2.jpg'
img , thresh= preprocess_image(img_path)
results = reader.readtext(img)  

for result in results:
    print(result)