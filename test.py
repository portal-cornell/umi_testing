import cv2

cap = cv2.VideoCapture()

if cap.isOpened():
    print("Camera is opened")
else:
    print("Camera is not opened")

cap.release()