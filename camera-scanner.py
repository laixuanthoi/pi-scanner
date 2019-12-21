import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break
    # cv2.imshow("frame", frame)
    print("okkkk")
    cv2.waitKey(1)
