import cv2

cap = cv2.VideoCapture(0)  # 0번 카메라 (기본 웹캠)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
mask_load = cv2.imread('tigermask.png',cv2.IMREAD_UNCHANGED)
b, g, r, a = cv2.split(mask_load)
a[:]=0
mask = cv2.merge([b,g,r,a])
if not cap.isOpened():
    print("Camera open failed!")
    exit()

while True:
    ret, frame = cap.read()  # 한 프레임 읽기
    if not ret: break
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces:
        masked = cv2.resize(mask, (w, h))
        frame[y:y + h, x:x + w] = masked[:, :, :3]
    cv2.imshow('Camera', frame)

    print(faces)
    if cv2.waitKey(10) == 27:  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()