import cv2
import numpy as np

orange = cv2.imread("Quynh.jpg",1)
apple = cv2.imread("Vinh.jpg",1)

apple = cv2.resize(apple,[512,512])
orange = cv2.resize(orange,[512,512])

#Gaussian Pyramid for apple
apples_gp = [apple]
for i in range(5):
    apple = cv2.pyrDown(apple)
    apples_gp.append(apple)

#Gaussian Pyramid for orange
oranges_gp = [orange]
for i in range(5):
    orange = cv2.pyrDown(orange)
    oranges_gp.append(orange)

#Laplacian Pyramid for apple
apple_copy = apples_gp[4]
apples_lp = [apple_copy]
for i in range(4,0,-1):
    gaussian_extended = cv2.pyrUp(apples_gp[i])
    apple_laplacian = cv2.subtract(apples_gp[i-1],gaussian_extended)
    apples_lp.append(apple_laplacian)

#Laplacian Pyramid for orange
orange_copy = oranges_gp[4]
oranges_lp = [orange_copy]
for i in range(4,0,-1):
    gaussian_extended = cv2.pyrUp(oranges_gp[i])
    orange_laplacian = cv2.subtract(oranges_gp[i-1],gaussian_extended)
    oranges_lp.append(orange_laplacian)


#join Laplacian pyramids of orange and apple
apples_oranges_pyramid = []
for apple_lap, orange_lap in zip(apples_lp, oranges_lp):
    cols, rows, channel = apple_lap.shape
    apple_orange = np.hstack((apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    apples_oranges_pyramid.append(apple_orange)


#reconstruct
apple_orange_reconstruct = apples_oranges_pyramid[0]
for i in range(1,5):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_reconstruct, apples_oranges_pyramid[i])


cv2.imshow("kq",apple_orange_reconstruct)



cv2.waitKey()
cv2.destroyAllWindows()
