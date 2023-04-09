import cv2

img = cv2.imread("./input/input.jpg")
b, g, r = cv2.split(img)

# histogram equalization
b = cv2.equalizeHist(b)
g = cv2.equalizeHist(g)
r = cv2.equalizeHist(r)

# final image
final = cv2.merge([b, g, r])
cv2.imwrite("./output/output_equal.jpg", final)