import cv2

cam = cv2.VideoCapture(cv2.CAP_V4L2)

while True:
    check, frame = cam.read()
    if check:
        cv2.imshow('video', frame)
    else:
        break

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()