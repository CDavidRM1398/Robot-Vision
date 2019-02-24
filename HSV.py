import cv2
import numpy as np

def callback(x):
    
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.namedWindow('image1')
cv2.namedWindow('image2')

ilowH = 0
ihighH = 179
ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
#negro
cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)
cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)
cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)
cv2.createTrackbar('kernel','image',1,20,callback)

#verde
cv2.createTrackbar('lowH1','image1',ilowH,179,callback)
cv2.createTrackbar('highH1','image1',ihighH,179,callback)
cv2.createTrackbar('lowS1','image1',ilowS,255,callback)
cv2.createTrackbar('highS1','image1',ihighS,255,callback)
cv2.createTrackbar('lowV1','image1',ilowV,255,callback)
cv2.createTrackbar('highV1','image1',ihighV,255,callback)
cv2.createTrackbar('kernel1','image1',1,20,callback)

#naranja
cv2.createTrackbar('lowH2','image2',ilowH,179,callback)
cv2.createTrackbar('highH2','image2',ihighH,179,callback)
cv2.createTrackbar('lowS2','image2',ilowS,255,callback)
cv2.createTrackbar('highS2','image2',ihighS,255,callback)
cv2.createTrackbar('lowV2','image2',ilowV,255,callback)
cv2.createTrackbar('highV2','image2',ihighV,255,callback)
cv2.createTrackbar('kernel2','image2',1,20,callback)



while(1):
    ret,rframe = cap.read()
    frame = rframe[240:480, 0:640]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    # get current positions of four trackbars 1
    #negro
    ilowH = cv2.getTrackbarPos('lowH','image')
    ilowS = cv2.getTrackbarPos('lowS','image')
    ilowV = cv2.getTrackbarPos('lowV','image')
    ihighH = cv2.getTrackbarPos('highH','image')
    ihighS = cv2.getTrackbarPos('highS','image')
    ihighV = cv2.getTrackbarPos('highV','image')
    kernel=cv2.getTrackbarPos('kernel','image')
    
    #verde
    ilowH1 = cv2.getTrackbarPos('lowH1','image1')
    ilowS1 = cv2.getTrackbarPos('lowS1','image1')
    ilowV1 = cv2.getTrackbarPos('lowV1','image1')
    ihighH1 = cv2.getTrackbarPos('highH1','image1')
    ihighS1 = cv2.getTrackbarPos('highS1','image1')
    ihighV1 = cv2.getTrackbarPos('highV1','image1')
    kernel1=cv2.getTrackbarPos('kernel1','image1')
    
    #naranja
    ilowH2 = cv2.getTrackbarPos('lowH2','image2')
    ilowS2 = cv2.getTrackbarPos('lowS2','image2')
    ilowV2 = cv2.getTrackbarPos('lowV2','image2')
    ihighH2 = cv2.getTrackbarPos('highH2','image2')
    ihighS2 = cv2.getTrackbarPos('highS2','image2')
    ihighV2 = cv2.getTrackbarPos('highV2','image2')
    kernel2=cv2.getTrackbarPos('kernel2','image2')
    
    #negro
    lower_hsv = np.array([ilowH, ilowS, ilowV],dtype=np.uint8)
    higher_hsv = np.array([ihighH, ihighS, ihighV],dtype=np.uint8)
    maskb = cv2.inRange(hsv, lower_hsv, higher_hsv)
    
    #verde
    verde_bajo = np.array([ilowH1, ilowS1, ilowV1],dtype=np.uint8)
    verde_alto = np.array([ihighH1, ihighS1, ihighV1],dtype=np.uint8)
    maskg = cv2.inRange(hsv, verde_bajo, verde_alto)
    
    #naranja
    naranja_bajo = np.array([ilowH2, ilowS2, ilowV2],dtype=np.uint8)
    naranja_alto = np.array([ihighH2, ihighS2, ihighV2],dtype=np.uint8)
    masko = cv2.inRange(hsv, naranja_bajo, naranja_alto)

    
    kernel = np.ones((kernel,kernel),np.uint8)
    kernelv = np.ones((kernel1,kernel1),np.uint8)
    kerneln = np.ones((kernel2,kernel2),np.uint8)
    mascara=cv2.morphologyEx(maskb, cv2.MORPH_CLOSE, kernel)
    mascara=cv2.morphologyEx(maskb, cv2.MORPH_OPEN, kernel)
    mascara1=cv2.morphologyEx(maskg, cv2.MORPH_CLOSE, kernelv)
    mascara1=cv2.morphologyEx(maskg, cv2.MORPH_OPEN, kernelv)
    mascara2=cv2.morphologyEx(masko, cv2.MORPH_CLOSE, kerneln)
    mascara2=cv2.morphologyEx(masko, cv2.MORPH_OPEN, kerneln)
    
    M1=cv2.add(mascara,mascara1)
    M=cv2.add(M1,mascara2)    
   
    cv2.imshow('M', M)
    cv2.imshow('Negro', mascara)
    cv2.imshow('Verde', mascara1)
    cv2.imshow('Naranja', mascara2)
    
    #print (ilowH, ilowS, ilowV)

    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()