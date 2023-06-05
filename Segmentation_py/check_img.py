from matplotlib import pyplot as plt
import cv2
img = cv2.imread("D:\Tai Lieu\Do an 1\hinh_new_led\hinhnled\hinh_new_led\Cable_clip_3000002.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img,[500,400])

plt.imshow(img)
plt.show()