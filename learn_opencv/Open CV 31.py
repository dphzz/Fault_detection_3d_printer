import matplotlib.pylab as plt
import cv2
import numpy as np


#img = cv2.imread("test_road.png")

#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


def ROI(image,vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(mask,image)
    return masked_image

def draw_lines(image,lines):
    black_image = np.zeros_like(image)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(black_image, [x1, y1], [x2, y2], [0, 0, 255], 3)
    image = cv2.addWeighted(image, 0.8, black_image, 1, 10)
    return image

def process(image):
    image = cv2.resize(image,[1276,564])
    roi_vertices = [(0,564),(0,540),(490,430),(730,430),(1150,564)]
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image,100,150)
    dropped_image = ROI(canny_image,np.array([roi_vertices],np.int32))

    lines = cv2.HoughLinesP(dropped_image,8,np.pi/270,200,minLineLength=60,maxLineGap=80)

    image_with_lines = draw_lines(image,lines)
    return image_with_lines

cap =   cv2.VideoCapture("D:\pythonProject1\opencv\Lane Detection Test Video.mp4")
while True:
    ret,frame = cap.read()
    processed_frame = process(frame)
    cv2.imshow("video",processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



