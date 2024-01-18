import numpy as np
import cv2 as cv

img = cv.imread('su hyeok.jpg')


img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)

cv.rectangle(img, (0,0),(100,100), color=(0,0,255), thickness=5)
cv.imshow('Img of Su hyeok',img)
cv.waitKey(0) 


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if(cv.waitkey(20)) & 0xFF==ord('t'):
       break

    capture.release()
    cv.destroyAllWindows() 