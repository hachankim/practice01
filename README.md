### OPEN CV 패키지를 활용한 그림판
- 이 코드는 OPENCV 패키지를 이용한 그림판 그리기입니다.
사용자가 마우스 왼쪽 클릭을 누른 상태로 마우스를 움직이면 그림을 그리게 됩니다.
- 사용자가 그린 그림을 초기화 하고싶으면 키보드 c를 눌러 초기화 할수있습니다.
- 그림판의 종료 키는 키보드 q입니다.

### 코드 설명
```
import cv2
import numpy as np

canvas = np.full((512, 512, 3), 255, dtype=np.uint8) 
```
필요한 패키지와 그림판을 그릴 배경을 만듭니다.

````
drow= False
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
````
이벤트로 마우스가 클릭이 됬는지 확인하고 그상태에서 마우스가 움직이면 선을 그리게하는 함수를 만듭니다.
````
while True:
    cv2.imshow('Canvas', canvas)
    cv2.setMouseCallback('Canvas', mouse_callback)
    if cv2.waitKey() == ord('q') or cv2.waitKey() == 0x1B :  # q를 누르면 종료
        break
    elif cv2.waitKey() == ord('c'):
        canvas[:] = 255
````
종료부분과 초기화 부분을 만들어줍니다.