import cv2
import numpy as np


def nothing(x):
    print(x)


cv2.namedWindow('image')

switch = 'color/gray'

cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    img = cv2.imread('anhmoi.jpg', 1)
    k = cv2.waitKey(1)
    if k == 27:
        break

    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image', img)

cv2.destroyAllWindows()
