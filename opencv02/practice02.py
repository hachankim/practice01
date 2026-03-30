import cv2
import numpy as np

src = cv2.imread('chroma.jpg')
lena = cv2.imread('lena.jpg')

src = cv2.resize(src, (512, 512))
lena = cv2.resize(lena, (512, 512))

mask = cv2.inRange(src, (0, 120, 0), (100, 255, 100))

mask_inv = cv2.bitwise_not(mask)

fg = cv2.bitwise_and(src, src, mask=mask_inv)
bg = cv2.bitwise_and(lena, lena, mask=mask)
dst = cv2.add(fg, bg)

cv2.imshow('1', mask)
cv2.imshow('2', fg)
cv2.imshow('3', bg)
cv2.imshow('4', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()