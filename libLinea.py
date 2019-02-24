import numpy as np
import cv2

def negro(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #negro
    lower_hsv = np.array([0,0,0],dtype=np.uint8)
    higher_hsv = np.array([255,255,30],dtype=np.uint8)
    
    
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    kernel = np.ones((4,4),np.uint8)
    mascara=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mascara=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
    M=cv2.add(mascara,mascara)
    blur = cv2.bilateralFilter(M,9,75,75)
    
    ret,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    return contours[0]

def verde(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #negro
    lower_hsv = np.array([28,84,45],dtype=np.uint8)
    higher_hsv = np.array([100,255,210],dtype=np.uint8)
    
    
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    kernel = np.ones((4,4),np.uint8)
    mascara=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mascara=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
    M=cv2.add(mascara,mascara)
    blur = cv2.bilateralFilter(M,9,75,75)
    
    ret,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    return contours[0]