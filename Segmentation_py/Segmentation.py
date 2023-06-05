import math

import cv2
import numpy as np
from matplotlib import pyplot as plt

def ROI(image, vertices):
    mask = np.zeros_like(image)
    channel = image.shape[2]
    match_mask_color = (255,)*channel
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def distance(point1, point2):
    khoangcach = math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    return khoangcach

flag = True

images = []
S = []
white_pixel = []
Centers = []

link1 = "./test_image/Cable_clip000035.jpg"
link2 = "./test_image/Cable_clip000036.jpg"

img1 = cv2.imread(link1)
img1 = cv2.resize(img1,[500,400])

images.append(img1)

img2 = cv2.imread(link2)
img2 = cv2.resize(img2,[500,400])

images.append(img2)

region_of_interest = [(125, 400), (130, 60), (380,60), (380,380)]
region_of_interest = np.array([region_of_interest], np.int32)
dropped_image = ROI(images[0], region_of_interest)

gray = cv2.cvtColor(dropped_image, cv2.COLOR_BGR2GRAY)

_, threshold_img = cv2.threshold(gray, 140,255,cv2.THRESH_BINARY)

#median_blur
blur_img = cv2.medianBlur(threshold_img, 5)


#morohological
kernel = np.ones([4,4],np.uint8)
morpho_img = cv2.morphologyEx(blur_img, cv2.MORPH_OPEN, kernel)

#draw contuals
#canny_img = cv2.Canny(threshold_img,10,20)
#lines = cv2.HoughLinesP(canny_img, 1, np.pi/90,50,minLineLength=30,maxLineGap=20)
#for line in lines:
    #x1,y1,x2,y2 = line[0]
    #cv2.line(images[-1],[x1,y1],[x2,y2],125,3)

maxrong = maxdai = 280
minrong = mindai = 400
for i in range(400):
    for j in range(500):
        if morpho_img[i][j] != 0:
            if i <= mindai:
                mindai = i
            elif i >= maxdai:
                maxdai = i
            elif j <= minrong:
                minrong = j
            elif j >= maxrong:
                maxrong = j

#Vẽ bounding box
images[0] = cv2.rectangle(images[0],[minrong, mindai], [maxrong, maxdai], (255,0,0), 3)

#Vẽ center và lưu vào mảng
center = [int((maxrong+minrong)/2), int((maxdai+mindai)/2)]
Centers.append(center)
images[0] = cv2.circle(images[0], center, 5, [0,0,255], -1)

#Tính diện tích bounding box và lưu vào mảng
s = (maxdai-mindai) * (maxrong - minrong)
S.append(s)

#Đếm số pixel trắng của layer và lưu vào mảng
count_pixel = 0
for i in range(mindai, maxdai):
    for j in range(minrong, maxrong):
        if morpho_img[i][j] != 0:
            count_pixel += 1
white_pixel.append(count_pixel)


# Kiểm tra xem có nhận hình ảnh mới không
#while flag == False and len(images) > 1:
    #if(img2):
       # images.append(img2)
       # flag = True
   # else:
      #  flag = False
#--------------------------------------------------------------------------

# Xử lí các hình ảnh mới được đưa vào mảng và tính ratio
while len(images) >= 2 and flag == True:
    dropped_image = ROI(images[-1], region_of_interest)

    gray = cv2.cvtColor(dropped_image, cv2.COLOR_BGR2GRAY)

    _, threshold_img = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    # median_blur
    blur_img = cv2.medianBlur(threshold_img, 5)

    # morohological
    morpho_img = cv2.morphologyEx(blur_img, cv2.MORPH_OPEN, kernel)

    maxrong = maxdai = 280
    minrong = mindai = 400
    for i in range(400):
        for j in range(500):
            if morpho_img[i][j] != 0:
                if i <= mindai:
                    mindai = i
                elif i >= maxdai:
                    maxdai = i
                elif j <= minrong:
                    minrong = j
                elif j >= maxrong:
                    maxrong = j

    images[-1] = cv2.rectangle(images[-1], [minrong, mindai], [maxrong, maxdai], (0, 0, 255), 3)
    center = [int((maxrong + minrong) / 2), int((maxdai + mindai) / 2)]
    Centers.append(center)

    print("độ dời tâm = ",distance(Centers[-1],Centers[-2]))

    images[-1] = cv2.circle(images[-1], center, 5, [0, 0, 255], -1)

    s = (maxdai - mindai) * (maxrong - minrong)
    S.append(s)
    ratio = float(S[-1] / S[-2])
    print("Tỉ lệ = ", ratio)

    count_pixel = 0
    for i in range(mindai, maxdai):
        for j in range(minrong, maxrong):
            if morpho_img[i][j] != 0:
                count_pixel += 1

    white_pixel.append(count_pixel)
    hieu = abs(white_pixel[-2] - white_pixel[-1])
    print("hieu pixel giữa 2 layer liền kề = ", hieu)

    flag = False



image = [images[-2], images[-1], threshold_img, blur_img, morpho_img, dropped_image]
titles = ["layer-pre" ,"layer-current", "thresholding", "blur_img", "morpho", "drop "]
for i in range(len(image)):
    plt.subplot(3, 3, i+1)
    plt.imshow(image[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()





#print(mindai, maxdai, minrong, maxrong)

#kq = cv2.rectangle(segmen, [minrong,mindai],[maxrong,maxdai],[0,255,255],1)
#kq = cv2.bilateralFilter(kq, 9, 75 , 75)

#plt.imshow(morpho_img)
#plt.show()

#s = (maxdai-mindai)*(maxrong-minrong)
#print("S =",s)


