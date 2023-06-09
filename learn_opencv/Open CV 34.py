import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread("Circle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=720,param2=30,minRadius=0,maxRadius=50)
detected_circles = np.uint16(np.around(circles))

print(circles[0])
print(circles.shape)

for x,y,r in detected_circles[0]:
    cv2.circle(img, [x, y], r, [0, 0, 255], 2)
    cv2.circle(img, [x, y], 2, [0, 255, 0], -1)

cv2.imshow("kq",img)
cv2.waitKey()
cv2.destroyAllWindows()
