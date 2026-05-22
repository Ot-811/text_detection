import cv2
import os

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    resize = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4))
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return resize, thresh