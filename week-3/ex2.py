import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./input/input.jpg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)

low, high = 0, 50
hand_area = ((h >= low) & (h <= high)) | (h >= 100)
hand_area = ~hand_area

hsv_img[hand_area, 2] = 0
save_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

cv2.imwrite("./output/output_hand.jpg", save_img)


# value, bins = np.histogram(h, 256, [0, 256])
# plt.plot(range(256), value)
# plt.show()
