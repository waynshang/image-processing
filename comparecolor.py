import cv2
import numpy as np
 
#cap = cv2.imread("C:\\Users\\06006685\\Pictures\\pip3.jpg")  # 或传入0，使用摄像头
 
while(True):
 
    # 读取一帧
    frame = cv2.imread("C:\\Users\\06006685\\Pictures\\pip5.jpg")
    
 
    # 把 BGR 转为 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([70,10,46])
    upper_blue = np.array([130,255,255])
 
    # HSV中黑色范围
    lower_black = np.array([0,0,0]) 
    upper_black = np.array([180,255,43])
    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
 
    # 获得黑色区域的mask
    mask = cv2.inRange(hsv, lower_black, upper_black)
 
    # 和原始图片进行and操作，获得黑色区域
    res_blue = cv2.bitwise_and(frame,frame, mask= mask_blue)
    res_black = cv2.bitwise_and(frame,frame, mask= mask)
    #cv2.imshow('mask_blue)',mask_blue)
    cv2.imshow('blue',res_blue)
 
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame',frame)
    #cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
    #cv2.imshow('mask',mask)
    cv2.namedWindow('black', cv2.WINDOW_NORMAL)
    cv2.imshow('black',res_black)
 
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv2.destroyAllWindows()

