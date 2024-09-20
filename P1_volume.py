# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:28:11 2022

@author: mkaab
"""

wCam, hCam = 1000, 480


import cv2
import time
import numpy as np
import handtrackingMODULE as hm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume




volPer=0
volBar=400
vol=0
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
cTime =0
pTime= 0
 
detector = hm.handDetector(detectionConfidence=0.6)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


volRange=volume.GetVolumeRange()

minvol=volRange[0]
maxvol=volRange[1]

 
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    
    lmList=detector.findPosition( img, handNo=0, draw=False)
    if len(lmList) !=0:        
        #print(lmList[4],lmList[8])
        
        x1,y1 = lmList[4][1], lmList[4][2]
        x2,y2 = lmList[8][1], lmList[8][2]
        #middle between both the points
        cx,cy = (x1+x2)//2, (y1+y2)//2
        
        cv2.circle(img, (x1,y1), 10, (125,100,50), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (125,100,50), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(125,100,50),3)
        cv2.circle(img, (cx,cy), 10, (150,150,100),cv2.FILLED)
        length = math.hypot(x2-x1,y2-y1)
        
        
        #hand range 25 to 300 and volume range is -96 to 0
        vol = np.interp(length,[20,200],[minvol,maxvol])
        volBar = np.interp(length,[20,200],[400,150])
        volPer = np.interp(length,[20,200],[0,100])
        
       
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)
                                         
                                         
                                         
                                         
        if length>200:
            cv2.circle(img, (cx,cy), 10, (0,0,250),cv2.FILLED)
                                 
        if length<50:
            cv2.circle(img, (cx,cy), 10, (0,0,250),cv2.FILLED)
            
    cv2.rectangle(img, (50,150), (85,400), (150,150,0),3)    
    cv2.rectangle(img, (50,int(volBar)), (85,400), (150,150,0), cv2.FILLED)  
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    
    cv2.putText(img, str(int(fps)), (20,80), cv2.FONT_HERSHEY_PLAIN, 2 , (300,10,75),3)
    cv2.putText(img, str(int(volPer)), (40,450), cv2.FONT_HERSHEY_PLAIN, 2 , (0,0,225),2)
    cv2.putText(img, str('%'), (100,450), cv2.FONT_HERSHEY_PLAIN, 2 , (0,0,225),2)
    
    cv2.imshow("image", img)
    
  
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break;
  
cap.release
cv2.destroyAllWindows()    