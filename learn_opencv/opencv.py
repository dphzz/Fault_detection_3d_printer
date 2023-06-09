import cv2
import numpy as np
a = cv2.imread("D:\Tai Lieu\TGM\picture 2.jpg",1)  #doc anh

#a = np.zeros([500,500,3],np.uint8)

a = cv2.resize(a,(600,510))             #chỉnh size ảnh
#a = cv2.rotate(a,cv2.ROTATE_180)                     #xoay ảnh
#a = cv2.line(a,[0,0], [300,255], [0, 0, 255], 5)     #vẽ line
#a = cv2.arrowedLine(a, [0,0], [300,255],[0,255,0],3) #vẽ arrowline
#a = cv2.rectangle(a,[0,0],[300,300],[0,0,255],3)     #vẽ HCN
#a = cv2.circle(a,[150,150],150,[255,0,0],3)          #vẽ tròn
#font = cv2.FONT_HERSHEY_SIMPLEX                    #chọn Font
#a = cv2.putText(a,'OpenCV',[300,150],font,3,[255,0,255],3)  #Ghi text
print(a)

cv2.imshow("cua so hien thi",a)                    #xuat anh
k=cv2.waitKey()

if k==ord("a"):
    cv2.imwrite("anhmoi1.jpg", a)
    cv2.destroyWindow()