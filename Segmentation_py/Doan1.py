import math

import cv2
import numpy as np
from matplotlib import pyplot as plt


#This function accepts 2 paramater that is the directory to the required 2 images. 
def Img_processing(link1, link2):
    def ROI(image, vertices):                           #CT con Drop ảnh
        mask = np.zeros_like(image)
        channel = image.shape[2]
        match_mask_color = (255,)*channel
        cv2.fillPoly(mask, vertices, match_mask_color)
        masked_image = cv2.bitwise_and(image, mask)
        return masked_image

    img1 = cv2.imread(link1)
    img1 = cv2.resize(img1,[448,448])

    img2 = cv2.imread(link2)
    img2 = cv2.resize(img2, [448, 448])

    region_of_interest = [(115, 320), (100, 70), (185, 0), (380, 0), (380, 320)]                  #Tọa độ các đỉnh vùng ảnh cần drop
    region_of_interest = np.array([region_of_interest], np.int32)

    #--------------------------------------------------------------------------

    # Xử lí các hình ảnh
    dropped_image1 = ROI(img1, region_of_interest)
    dropped_image2 = ROI(img2, region_of_interest)

    gray1 = cv2.cvtColor(dropped_image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(dropped_image2, cv2.COLOR_BGR2GRAY)

    _, threshold_img1 = cv2.threshold(gray1, 140, 255, cv2.THRESH_BINARY)
    _, threshold_img2 = cv2.threshold(gray2, 140, 255, cv2.THRESH_BINARY)

    # median_blur
    blur_img1 = cv2.medianBlur(threshold_img1, 5)
    blur_img2 = cv2.medianBlur(threshold_img2, 5)

    # morohological
    kernel = np.ones([5,5],np.uint8)
    morpho_img1 = cv2.morphologyEx(blur_img1, cv2.MORPH_OPEN, kernel)
    morpho_img2 = cv2.morphologyEx(blur_img2, cv2.MORPH_OPEN, kernel)

    #Tìm tọa độ bounding box
    maxrong1 = maxdai1 = maxrong2 = maxdai2 = 0
    minrong1 = mindai1 = minrong2 = mindai2 = 400
    for i in range(400):
        for j in range(500):
            if morpho_img1[i][j] != 0:
                if i <= mindai1:
                    mindai1 = i
                if i >= maxdai1:
                    maxdai1 = i
                if j <= minrong1:
                    minrong1 = j
                if j >= maxrong1:
                    maxrong1 = j

    for i in range(400):
        for j in range(500):
            if morpho_img2[i][j] != 0:
                if i <= mindai2:
                    mindai2 = i
                if i >= maxdai2:
                    maxdai2 = i
                if j <= minrong2:
                    minrong2 = j
                if j >= maxrong2:
                    maxrong2 = j

    # Tính diện tích bouding box và tỉ lệ bb của 2 layer kế tiếp nhau
    s1 = (maxdai1 - mindai1) * (maxrong1 - minrong1)
    s2 = (maxdai2 - mindai2) * (maxrong2 - minrong2)

    #Tính vị trí tâm bounding box
    img1 = cv2.rectangle(img1, [minrong1, mindai1], [maxrong1, maxdai1], (0, 0, 255), 2)        #Vẽ bouding box
    center1 = [int((maxrong1 + minrong1) / 2), int((maxdai1 + mindai1) / 2)]                                 #Xác định tọa độ tâm
    img2 = cv2.rectangle(img2, [minrong2, mindai2], [maxrong2, maxdai2], (0, 255, 0), 2)  # Vẽ bouding box
    center2 = [int((maxrong2 + minrong2) / 2), int((maxdai2 + mindai2) / 2)]

    # Vẽ tâm
    img1 = cv2.circle(img1, center1, 5, [0, 0, 255], -1)
    img2 = cv2.circle(img2, center2, 5, [0, 2555, 0], -1)

    # Đếm số pixel trắng và hiêu 2 giữa layer
    count_pixel1 = 0
    for i in range(mindai1, maxdai1):
        for j in range(minrong1, maxrong1):
            if morpho_img1[i][j] != 0:
                count_pixel1 += 1

    count_pixel2 = 0
    for i in range(mindai2, maxdai2):
        for j in range(minrong2, maxrong2):
            if morpho_img2[i][j] != 0:
                count_pixel2 += 1
    print(s1, ", ", center1, ", ", count_pixel1)
    print(s2, ", ", center2, ", ", count_pixel2)


    # Hiển thị ảnh
    image = [img1, img2, threshold_img2, blur_img2, morpho_img2, dropped_image2]
    titles = ["layer_pre", "layer-current", "thresholding", "blur_img", "morpho", "drop "]
    for i in range(len(image)):
        plt.subplot(3, 3, i + 1)
        plt.imshow(image[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    #s1,s2 is the area of the image boudning box.
    #center1, center2 are the position of the center of the bounding box
    #count_pixel1, count_pixel2 are the total number of white pixel in each image
    return s1, s2, center1, center2, count_pixel1, count_pixel2



#---------------------------------------------------------------------------------
def  Caculate(s1,s2,cen1,cen2,white1, white2):
    def distance(point1, point2):  # CT con tính khoảng cách
        khoangcach = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        return khoangcach

    #Tính độ dời tâm
    center_distance = distance(cen1,cen2)
    print("Độ dời tâm = ",center_distance)

    #Tính tỉ lệ diện tích
    ratio = float(s1 / s2)
    print("Tỉ lệ = ", ratio)

    #Tính hiệu pixel trắng
    hieu = abs(white1 - white2)
    print("Hiệu số pixel giữa 2 layer liền kề = ", hieu)

    return center_distance,ratio,hieu



#---------------------------------------------------------------------------------
def Compare(center_distance, ratio, hieu):
    if center_distance > 20:
        print("Lỗi vật bị bong ra khỏi bàn in")
        return 1
    if hieu > 3500 or ratio > 1.2:
        print("Lỗi đầu in không bám theo quỹ đạo mong muốn")
        return 2
    if center_distance <20 and hieu < 3500 and ratio < 1.2:
        print("Continue")
        return 0

#This part is used to debug this library.
if __name__ == "__main__":
    first_img   = r"Z:\screwdriver_case_kn_body000046.jpg"
    second_img  = r"Z:\screwdriver_case_kn_body000047.jpg"
    # first_img   = r"G:\Shared drives\Ngo_Duc_Phu\Do_an_1\Python_code\Segmentation_py\test_image\Cable_clip000035.jpg"
    # second_img  = r"G:\Shared drives\Ngo_Duc_Phu\Do_an_1\Python_code\Segmentation_py\test_image\Cable_clip000035.jpg"


    s1,s2,center1,center2,white1,white2 = Img_processing(first_img, second_img)
    Caculate(s1,s2,center1,center2,white1,white2)