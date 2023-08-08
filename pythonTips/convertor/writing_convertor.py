import pywhatkit as kit
from cv2 import cv2


kit.text_to_handwriting("Hello Naurangi Lal",save_to="handwriting.png")
img=cv2.imread("handwriting.png")
cv2.imshow("text to handwriting",img)
cv2.waitKey(0)
cv2.destroyAllWindows()