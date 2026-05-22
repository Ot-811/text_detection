import cv2
import pytesseract
from preprocessing import preprocess_image

img_path = './images/test_img2.jpg'
img, thresh = preprocess_image(img_path)
data = pytesseract.image_to_data(thresh, config='--psm 6', output_type=pytesseract.Output.DICT)


for i in range(len(data['text'])):
    if int(data['conf'][i]) > 70:
        x = data['left'][i]
        y = data['top'][i]
        w = data['width'][i]
        h = data['height'][i]
        text = data['text'][i]
        cv2.rectangle(img,(x, y),(x + w, y + h),(0, 255, 0),2)
        label = f"{text} ({data['conf'][i]})"
        cv2.putText(img,label,(x,y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.3,(0, 255, 0),1)





'''
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Thresholded Image', thresh) 
'''

cv2.imshow("OCR Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()