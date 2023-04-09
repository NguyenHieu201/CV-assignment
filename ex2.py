import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./input/input.jpg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_img)

low, high = 80, 120
hand_area = (h >= low) & (h <= high)
hand_area = ~hand_area

hsv_img[hand_area, 2] = 0
save_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

cv2.imwrite("./output/output_hand.jpg", save_img)
