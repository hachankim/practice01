import cv2
import numpy as np
cap = cv2.VideoCapture(0)  # 0번 카메라 (기본 웹캠)
colors = [(255, 0, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color = colors[0]
width = int(cap.get(3))
height = int(cap.get(4))
kernel = np.ones((5, 5), np.uint8)
canvas = np.zeros((height, width, 3), np.uint8)
previous_center_point = 0
i = 0
thickness = 2
if not cap.isOpened():
    print("Camera open failed!")
    exit()
while True:
    ret, frame = cap.read()  # 한 프레임 읽기
    if not ret: break
    frame = cv2.flip(frame, 1)
    lower_bound = np.array([70, 40, 100])
    upper_bound = np.array([100, 255, 255])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    contours, h = cv2.findContours(mask, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)

    mask = cv2.dilate(mask, kernel, iterations=1)

    if len(contours) > 0:
        cmax = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cmax)
        min_area = 1000
        if area > min_area:
            M = cv2.moments(cmax)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            if previous_center_point != 0:
                cv2.line(canvas, previous_center_point, (cX, cY), color, thickness)

            previous_center_point = (cX, cY)

    else:
        previous_center_point = 0

    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, canvas_binary = cv2.threshold(canvas_gray, 20, 255,
                                     cv2.THRESH_BINARY_INV)
    canvas_binary = cv2.cvtColor(canvas_binary, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, canvas_binary)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow('Camera', frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord('c'):
        canvas = np.zeros((height, width, 3), np.uint8)
        thickness = 2
    if key == ord('p'):
        i = (i + 1) % len(colors)
        color = colors[i]
    if key == ord('n'):
        thickness = max(1,(thickness - 1))
    if key == ord('m'):
        thickness = (thickness + 1)

cap.release()
cv2.destroyAllWindows()