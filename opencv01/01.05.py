import cv2
import sys

img = cv2.imread('lena.jpg')

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print("왼쪽 버튼 클릭:", x, y)
if img is None:
    print('이미지를 찾을수 없습니다.')
    sys.exit()





cv2.imshow('Lena girl', img)
cv2.setMouseCallback('Lena girl', mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()