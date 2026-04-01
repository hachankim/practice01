import cv2
import sys

img = cv2.imread('lena.jpg')

if img is None:
    print('이미지를 찾을수 없습니다.')
    sys.exit()
cv2.imshow('Lena girl', img)
cv2.waitKey(0)
cv2.destroyAllWindows()