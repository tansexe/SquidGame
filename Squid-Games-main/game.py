import cv2 as cv
import mediapipe as mp 
import numpy as np 
import math
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)
def prepare_target_image():
    target_image =cv.imread('Triangle.jpg')
    target_image = cv.resize(target_image, (512,512))


    blank = np.zeros([1080,1440,3],dtype=np.uint8)
    blank.fill(255)
    blank_height, blank_width, blank_c = blank.shape
    blank_cy, blank_cx = blank_height // 2, blank_width // 2
    blank[blank_cy - (512//2):blank_cy + (512//2), blank_cx - (512//2):blank_cx + (512//2)] = 'target_image'
    return blank 
def preprocess_target_image(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 30, 100)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 150, np.array([]), 50, 10)
    line_1_x1 = []
    line_1_x2 = []
    line_1_y1 = []
    line_1_y2 = []
    line_2_x1 = []
    line_2_x2 = []
    line_2_y1 = []
    line_2_y2 = []
    line_3_x1 = []
    line_3_x2 = []
    line_3_y1 = []
    line_3_y2 = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            if((y2-y1)/(x2-x1)) > 0:
                line_1_x1.append(x1)
                line_1_x2.append(x2)
                line_1_y1.append(y1)
                line_1_y2.append(y2)

            elif((y2-y1)/(x2-x1)) < 0:
                line_2_x1.append(x1)
                line_2_x2.append(x2)
                line_2_y1.append(y1)
                line_2_y2.append(y2)

            else:
                line_3_x1.append(x1)
                line_3_x2.append(x2)
                line_3_y1.append(y1)
                line_3_y2.append(y2) 

    line_1_x1_mean = np.mean(line_1_x1)
    line_1_x2_mean = np.mean(line_1_x2)
    line_1_y1_mean = np.mean(line_1_y1)
    line_1_y2_mean = np.mean(line_1_y2)
    line_2_x1_mean = np.mean(line_2_x1)
    line_2_x2_mean = np.mean(line_2_x2)
    line_2_y1_mean = np.mean(line_2_y1)
    line_2_y2_mean = np.mean(line_2_y2)
    print("Mean of x1 in line 1: ", line_1_x1_mean)
    print("Mean of x2 in line 1: ", line_1_x2_mean)
    print("Mean of y1 in line 1: ", line_1_y1_mean)
    print("Mean of y2 in line 1: ", line_1_y2_mean)
    print("Mean of x1 in line 2: ", line_2_x1_mean)
    print("Mean of x2 in line 2: ", line_2_x2_mean)
    print("Mean of y1 in line 2: ", line_2_y1_mean)
    print("Mean of y2 in line 2: ", line_2_y2_mean)
    print("Mean of x1 in line 3: ", line_3_x1_mean)
    print("Mean of x2 in line 3: ", line_3_x2_mean)
    print("Mean of y1 in line 3: ", line_3_y1_mean)
    print("Mean of y2 in line 3: ", line_3_y2_mean)

def check_collision(a, b, c, x, y, radius):
      

    dist = ((abs(a * x + b * y + c)) /
            math.sqrt(a * a + b * b))
    if (radius >= dist):
        return True
    else:
        return False 
    
