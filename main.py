from HAND_TRACKING_MODULE import HandTracker
import cv2

def main():
    cap=cv2.VideoCapture(0)
    while True:
        _,img=cap.read()
        tracker=HandTracker()
        tracker.find_hands(img)
        li=tracker.findPosition(img,draw=False)
        if len(li):
            print(li[4])
        cv2.imshow("Live",img)
        key=cv2.waitKey(1)
        if key==ord("q"):
            break


if __name__ == "__main__":
    main()
