import cv2
import numpy as np
import pytesseract

def preprocess_image(img):
    img_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img_resized = cv2.resize(img_np, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    img_blurred = cv2.medianBlur(img_resized, 3)
    return img_blurred

def img_string(img):
    preprocessed_img = preprocess_image(img)
    resultado = pytesseract.image_to_string(preprocessed_img, config='--psm 1 -l eng+spa')
    return resultado