### getPerspectiveTransform 연습과제
- 이 코드는 getPerspectiveTransform 함수를 이용하여 기울어진 그림을 정방향으로 변환하는 코드입니다.
### 코드 설명
```
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
```
필요한 패키지와 그림크기를 재조정하고 변환 시킬 좌표를 구합니다.

````
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
````
구한 좌표와 변환시킬 좌표를 변수에 저장하고 cv2.getPerspectiveTransform을 통해 변환 행렬 M을 구하고, cv2.warpPerspective로 최종 결과물을 생성합니다.

