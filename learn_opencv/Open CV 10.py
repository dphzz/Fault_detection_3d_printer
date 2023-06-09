import cv2
import numpy as np

a = cv2.imread('anhmoi.jpg',1)
b = cv2.imread('D:\Tai Lieu\TGM\pexels-shahadat-hossain-9307205.jpg',1)

print(a.shape)
print(a.size)
print(a.dtype)

a = cv2.resize(a,(500,600))
b = cv2.resize(b,(500,600))
#tong = cv2.add(a,b)
tong = cv2.addWeighted(a,0.2,b,0.5,0)
cv2.imshow("window",tong)


cv2.waitKey()
cv2.destroyAllWindows()

