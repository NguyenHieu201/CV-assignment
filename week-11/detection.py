import cv2
import numpy as np
import matplotlib.pyplot as plt


from detector import *

# first_frame_center = (327, 543)
video_cap = cv2.VideoCapture("./input/marbleball.mp4")

while True:
    ret, frame = video_cap.read()
    if not ret:
        break
    find_circle(frame)