import cv2

def tracking(video_path, s0=(327, 543), v=(10, 10), a=(10, 10)):
    video = cv2.VideoCapture(video_path)
    t = 0
    while True:
        st = (0, 0)
        ret, frame = video.read()
        if not ret:
            break
        
        st[0] = s0[0] + v[0] * t + 0.5 * a[0] * t * t
        st[1] = s0[1] + v[1] * t + 0.5 * a[1] * t * t
        
        t += 1
        
        cv2.circle(frame, st, 18, (0, 255, 0), 0)
        cv2.imshow("Tracking", frame)
        