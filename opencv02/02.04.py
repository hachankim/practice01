import cv2

img = cv2.imread('lena.jpg')

b,g,r = cv2.split(img)

dst = cv2.merge((r,b,g))
cv2.imshow('src', b)
cv2.imshow('src2', g)
cv2.imshow('src3', r)
cv2.imshow('src4', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()