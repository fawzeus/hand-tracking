import cv2
import mediapipe as mp
import time



class HandTracker:
    def __init__(self,mode=False,Max_hands=2,detect_conf=0.5,track_conf=0.5):
        self.mode=mode
        self.MaxHands=Max_hands
        self.dectect_conf=detect_conf
        self.track_conf=track_conf

        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.MaxHands,self.dectect_conf,self.track_conf)
        self.mpdraw = mp.solutions.drawing_utils


    def find_hands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)

        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,hand,self.mpHands.HAND_CONNECTIONS)

        return img


    def findPosition(self,img,Handnum=0,draw=True):
        lmList=[]
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                for id,lm in enumerate(hand.landmark):
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    #print(id,cx,cy)
                    lmList.append([id,cx,cy])
                    if draw:
                        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
        return lmList


