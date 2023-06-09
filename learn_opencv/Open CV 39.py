import cv2
import numpy as np

cap = cv2.VideoCapture("Lane Detection Test Video.mp4")

fgbg = cv2.createBackgroundSubtractor(detectShadows=True)

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    cv2.imshow("kq",fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()