import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   #haarcascade_frontalface_alt_tree.xml is best
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
img = cv2.imread("D:\Tai Lieu\TGM\heads.png")
img = cv2.resize(img,[0,0],fx = 1.8, fy = 1.8)

#cap = cv2.VideoCapture(0)
#ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 3)

for x,y,w,h in faces:
    cv2.rectangle(img,[x, y],[x+w, y+h],[255,255,0],3)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for xe,ye,we,he in eyes:
        cv2.rectangle(roi_color,[xe,ye],[xe+we,ye+he],[0,255,255],2)

cv2.imshow("video",img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

#cap.release()
cv2.waitKey()
cv2.destroyAllWindows()