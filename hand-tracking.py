import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)


current_time=0
previous_time=0
mpHands=mp.solutions.hands
hands=mpHands.Hands(False,4,0.5,0.5)
mpdraw = mp.solutions.drawing_utils
while True:
    _,img=cap.read()
    
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            for id,lm in enumerate(hand.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                #print(id,cx,cy)
            mpdraw.draw_landmarks(img,hand,mpHands.HAND_CONNECTIONS)

    current_time=time.time()
    fps=1/(current_time-previous_time)
    previous_time=current_time
    #print(int(fps))

    cv2.imshow("Live",img)
    key=cv2.waitKey(1)
    if key== ord("q"):
        print("Byee")
        break
