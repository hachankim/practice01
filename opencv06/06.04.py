import cv2

cap = cv2.VideoCapture(0)  # 0번 카메라 (기본 웹캠)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
if not cap.isOpened():
    print("Camera open failed!")
    exit()

while True:
    ret, frame = cap.read()  # 한 프레임 읽기
    if not ret: break
    out.write(frame)
    cv2.imshow('Camera', frame)
    if cv2.waitKey(10) == 27:  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()