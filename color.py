import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)
lower_blue=np.array([78, 43, 46])
upper_blue=np.array([110, 255, 255])
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height =int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(1):
    ret, frame = cap.read()
    img=cap.read()
    cv2.imshow('Capture', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Mask', mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.rectangle(res, (0, height), (width , 0 ), (0, 255, 0), 5)
    cv2.imshow('Result', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()