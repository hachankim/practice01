import cv2
import sys

import numpy as np


img = cv2.imread('letter.jpg')
dst_size = cv2.resize(img, (640,640))
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("왼쪽 버튼 클릭:", x, y)

if img is None:
    print('이미지를 찾을수 없습니다.')
    sys.exit()

pts1 = np.float32([[482,212],[21,258],[19,563],[600,481]])
pts2 = np.float32([[0,0],[0,640],[640,640],[640,0]])

cv2.circle(dst_size, (482,212), 20, (255,0,0),-1)
cv2.circle(dst_size, (21,258), 20, (0,255,0),-1)
cv2.circle(dst_size, (19,563), 20, (0,0,255),-1)
cv2.circle(dst_size, (600,481), 20, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(dst_size, M, (640,640))

cv2.imshow('after_letter', dst)
cv2.imshow('letter', dst_size)
cv2.setMouseCallback('letter', mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()