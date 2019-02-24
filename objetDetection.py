import cv2
#import numpy as np
import libLinea as lib

cap = cv2.VideoCapture(1)


while(1):
    ret,rframe = cap.read()
    frame1=rframe[0:240, 0:640]
    frame=rframe[240:480, 0:640]
    
    try:
        cnt = lib.verde(frame)
        area = cv2.contourArea(cnt)
        MV = cv2.moments(cnt)
        cxV = int(MV['m10']/MV['m00'])
        if area>3000.5:
            if cxV<320:
                print("izquierda")
            else:
                print("derecha")
                
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
    except IndexError:
        try:
            cntN=lib.negro(frame)
            MN = cv2.moments(cntN) 
            cxN = int(MN['m10']/MN['m00'])
            if cxN < 213.5 :
                print("derecha")
            elif cxN < 426.5 :
                print("adelante")
            else :
                print("izquierda")
                
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
        except IndexError:
            try:
                cntN1=lib.negro(frame1)
                areaN1 = cv2.contourArea(cntN1)
                if areaN1>100:
                    print("no objeto")
            except ZeroDivisionError as err:
                print('Handling run-time error:', err)
            except IndexError:
                print("objeto")
                

    
    cv2.imshow('M', frame)
    #cv2.imshow('Negro', M)
    #cv2.imshow('Verde', mascara1)
    #cv2.imshow('Naranja', mascara2)

    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

