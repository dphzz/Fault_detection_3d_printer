import cv2
import numpy as np

def nothing(x):
    print(x)


cv2.namedWindow('Tracking')
cv2.createTrackbar("LH",'Tracking',0,179,nothing)
cv2.createTrackbar("LS",'Tracking',0,255,nothing)
cv2.createTrackbar("LV",'Tracking',0,255,nothing)

cv2.createTrackbar("UH",'Tracking',179,179,nothing)
cv2.createTrackbar("US",'Tracking',255,255,nothing)
cv2.createTrackbar("UV",'Tracking',255,255,nothing)

frame = cv2.imread("test_5.jpg", 1)
frame = cv2.resize(frame,[0,0],fx=0.5,fy=0.5)
#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#cap = cv2.VideoCapture(0)




while True:

    #_, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    LH = cv2.getTrackbarPos('LH','Tracking')
    LS = cv2.getTrackbarPos('LS','Tracking')
    LV = cv2.getTrackbarPos('LV','Tracking')

    UH = cv2.getTrackbarPos('UH', 'Tracking')
    US = cv2.getTrackbarPos('US', 'Tracking')
    UV = cv2.getTrackbarPos('UV', 'Tracking')


    lower_blue = np.array([LH, LS, LV])
    upper_blue = np.array([UH, US, UV])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
