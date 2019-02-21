import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret,rframe = cap.read()
    frame=rframe[240:480, 0:640]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #negro
    lower_hsv = np.array([28,84,45],dtype=np.uint8)
    higher_hsv = np.array([100,255,210],dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    kernel = np.ones((9,9),np.uint8)
    mascara=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mascara=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
    M=cv2.add(mascara,mascara)
    blur = cv2.bilateralFilter(M,9,75,75)
    
    ret,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    try:
        cnt = contours[0]
        area = cv2.contourArea(cnt)
        if area > 3007.5 :
            M = cv2.moments(cnt) 
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame,[box],0,(0,255,0),2) 
            print (area)
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
    except IndexError as er:
        print('Handling run-time error:', er)
    
    cv2.imshow('M', frame)
    #cv2.imshow('Negro', M)
    #cv2.imshow('Verde', mascara1)
    #cv2.imshow('Naranja', mascara2)

    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()