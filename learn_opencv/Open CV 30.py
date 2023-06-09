import cv2
import numpy as np

img = cv2.imread("anhmoi.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,200)
cv2.imshow("da", edges)
lines = cv2.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    print(rho, theta)
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 - 1000*b)
    y1 = int(y0 + 1000*a)
    x2 = int(x0 + 1000*b)
    y2 = int(y0 - 1000*a)
    cv2.line(img,[x1,y1],[x2,y2],(255,255,0),2)

cv2.imshow("kq",img)
cv2.waitKey()
cv2.destroyAllWindows()