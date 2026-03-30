import cv2
import numpy as np

# 흰색 배경 생성 (512x512)
canvas = np.full((512, 512, 3), 255, dtype=np.uint8)
drow= False
# 그리기
def mouse_callback(event, x, y, flags, param):
    global drow
    if event == cv2.EVENT_LBUTTONDOWN:
        drow = True
    elif event == cv2.EVENT_LBUTTONUP:
        drow = False
    if event == cv2.EVENT_MOUSEMOVE:
        if drow:
            cv2.line(canvas, (x, y), (x+1, y+1), (0, 0, 0), 5)
            cv2.imshow('Canvas', canvas)
            print("왼쪽 버튼 클릭:", x, y)
while True:
    cv2.imshow('Canvas', canvas)
    cv2.setMouseCallback('Canvas', mouse_callback)
    if cv2.waitKey() == ord('q') or cv2.waitKey() == 0x1B :  # q를 누르면 종료
        break
    elif cv2.waitKey() == ord('c'):
        canvas = np.full((512, 512, 3), 255, dtype=np.uint8)


