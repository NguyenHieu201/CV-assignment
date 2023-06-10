import numpy as np
import cv2
    
def find_circle(img):
    blank_img = cv2.inRange(img, (25, 48, 170), (57, 103, 209))
    
    x, y = np.where(blank_img == 255)
    
    # center_x, center_y = int((min_x + max_x) / 2), int((min_y + max_y) / 2)

    # cv2.circle(img, (center_y, center_x), 10, (0, 255, 0), 2)
    
    contours, hierarchy = cv2.findContours(blank_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    
    center = 0
    num_point = 0
    for contour in contours:
        center = center + np.sum(contour, axis=0)
        num_point += contour.shape[0]
        
    print(center / num_point)
    
    cv2.imshow("Detected", img)
    # cv2.imshow("Blank", blank_img)
    cv2.waitKey()
    
    

    