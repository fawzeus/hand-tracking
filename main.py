from time import clock
from HAND_TRACKING_MODULE import HandTracker
import cv2
import pyautogui
from math import sqrt
import numpy as np
import autopy


def main():
    cap=cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    w,h=autopy.screen.size()
    zone=100   # zone of the mouse
    smoothing=5
    plocx,plocy=0,0
    clockx,clocky=0,0
    #print(w,h)
    while True:
        _,img=cap.read()
        #img = cv2.flip(img,1)
        tracker=HandTracker()
        tracker.find_hands(img)
        li=tracker.findPosition(img,draw=False)
        if len(li):
            cv2.rectangle(img,(zone,zone),(640-zone,480-zone),(230,255,0),2)
            #print(li[4])
            _,x4,y4=li[4]
            _,x8,y8=li[8]
            if li[8][2] < li[6][2]:
                xmouse=np.interp(x8,(zone,640-zone),(0,w))
                ymouse=np.interp(y8,(zone,480-zone),(0,h))
                
                clockx=plocx+(xmouse-plocx)/smoothing
                clocky=plocy+(ymouse-plocy)/smoothing


                dist = sqrt((x4-x8)*(x4-x8) + (y4-y8)*(y4-y8))
                print(dist)
                autopy.mouse.move(w-clockx,clocky)
                cv2.circle(img,(x8,y8),15,(230,255,0),cv2.FILLED)
                plocx,plocy=clockx,clocky
                if dist<20:
                    autopy.mouse.click()
        cv2.imshow("Live",img)
        key=cv2.waitKey(1)
        if key==ord("q"):
            break


if __name__ == "__main__":
    main()
