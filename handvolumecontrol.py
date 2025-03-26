import cv2
import time
import numpy as np

#####################################################3
wcam, hcam = 640, 480
##########################################33#########3


cap = cv2.VideoCapture(0)
cap.set, (3, wcam)
cap.set(4, hcam)
cap.set(5, wcam)
pTime = 0
while True:
    sucess, img = cap.read()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS : {int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('video', img)
    cv2.waitKey(1)