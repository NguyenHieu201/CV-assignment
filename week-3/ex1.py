import cv2
import numpy as np


img_path = "./input/input.jpg"
img = cv2.imread(img_path)

# hsv
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

# save grayscale image
gray_img = cv2.cvtColor(v, cv2.COLOR_GRAY2BGR)
cv2.imwrite("./output/hsv_gray.jpg", gray_img)

# v = 1 image
v1_img = img_hsv.copy()
v1_img[:, :, 2] = 1
v1_img = cv2.cvtColor(v1_img, cv2.COLOR_HSV2BGR)
cv2.imwrite("./output/hsv_v1.jpg", v1_img)


# lab
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

l, a, b = cv2.split(img_lab)

# save grayscale image
gray_img = cv2.cvtColor(l, cv2.COLOR_GRAY2BGR)
cv2.imwrite("./output/lab_gray.jpg", gray_img)

# l = 1 image
l1_img = img_lab.copy()
l1_img[:, :, 0] = 1
l1_img = cv2.cvtColor(l1_img, cv2.COLOR_Lab2BGR)
cv2.imwrite("./output/lab_l1.jpg", l1_img)