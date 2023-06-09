import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(a,[x,y],3,[255,255,255],-1)
        #points.append([x,y])
        #if len(points) >= 2:
            #cv2.line(a,points[-1],points[-2],[255,0,0],1)
        blue = a[y,x,0]
        green = a[y,x,1]
        red = a[y,x,2]
        colorpoint = np.zeros((300,300,3), np.uint8)
        colorpoint[:]=[blue,green,red]
        cv2.imshow("color",colorpoint)
        cv2.imshow("image",a)

a = cv2.imread('anhmoi.jpg',1)
cv2.imshow("image",a)
points =[]
cv2.setMouseCallback("image", click_event)

cv2.waitKey()
cv2.destroyAllWindows()


