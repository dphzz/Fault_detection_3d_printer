import cv2
import numpy as np

img = cv2.imread("anhmoi.jpg",0)
cv2.imshow("image", img)

cv2.waitKey()
cv2.destroyAllWindows()
