import cv2
import numpy as np
from scipy import signal
import time

img = cv2.imread("./input/input.jpg", 0)
K1 = cv2.imread("./input/K1.png", 0)
K2 = cv2.imread("./input/K2.png", 0)

kernel1 = K1 / K1.sum()
kernel2 = K2 / K2.sum()

start = time.time()
img1 = signal.convolve(img, kernel1, mode="same", method="direct")
B2 = signal.convolve(img1, kernel2, mode="same", method="direct")
cv2.imwrite("./output/B2.jpg", B2)
end = time.time()
print(f"Running time convolution: {end - start}")


start = time.time()
img1 = signal.convolve(img, kernel1, mode="same", method="fft")
B1 = signal.convolve(img1, kernel2, mode="same", method="fft")
end = time.time()

cv2.imwrite("./output/B1.jpg", B1)
print(f"Running time fftconvolve: {end - start}")