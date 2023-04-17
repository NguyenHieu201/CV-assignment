import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./input/CC_Hello.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
hue_label = np.zeros(shape=thresh.shape)

h, w = img.shape

equiv_table = {}
region_points = {}
region_value = 1

def get_label(equiv_table: dict, value: int) -> int:
    equiv_values = equiv_table[value]
    for val in equiv_values:
        equiv_values = equiv_values | equiv_table[val]
    return min(equiv_values)

for i in range(h):
    for j in range(w):
        # forground pixel
        if thresh[i, j] != 0:
            up_value = int(hue_label[i-1, j]) if (i-1 >= 0) else 0
            left_value = int(hue_label[i, j-1]) if (j-1 >= 0) else 0

            if (up_value == 0) and (left_value == 0):
                hue_label[i, j] = region_value
                equiv_table[region_value] = {region_value}
                region_points[region_value] = {(i, j)}
                region_value += 1
            elif (up_value == 0) and (left_value != 0):
                hue_label[i, j] = left_value
                region_points[left_value].add((i, j))
            elif (up_value != 0) and (left_value == 0):
                hue_label[i, j] = up_value
                region_points[up_value].add((i, j))
            else:
                if (up_value != left_value):
                    equiv_table[up_value] = equiv_table[up_value] | equiv_table[left_value]
                    equiv_table[left_value] = equiv_table[up_value] | equiv_table[left_value]
                hue_label[i, j] = min(equiv_table[up_value])
                region_points[hue_label[i, j]].add((i, j))

final_region = {}
mark = [0] * region_value
cnt_region = 0

for k in equiv_table.keys():
    if mark[k] == 0:
        equiv_values = equiv_table[k]
        final_region[cnt_region] = region_points[k]
        for value in equiv_table[k]:
            equiv_values = equiv_values | equiv_table[value]
        for value in equiv_values:
            final_region[cnt_region] = final_region[cnt_region] | region_points[value]
            mark[value] = 1
        mark[k] = 1
        cnt_region += 1

COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (128, 0, 0), (0, 128, 0), (0, 0, 128)
]

result_img = np.zeros((h, w, 3))

for region in range(cnt_region):
    color = COLORS[region]
    points = np.array(list(final_region[region]))
    points = (points[:, 0], points[:, 1])
    result_img[points] = color
cv2.imwrite("./output/ex4-result.jpg", result_img)