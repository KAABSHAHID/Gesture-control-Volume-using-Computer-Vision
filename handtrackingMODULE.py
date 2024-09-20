

import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.modelComplex, self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        print(self.results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img,handlms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            my_Hand=self.results.multi_hand_landmarks[handNo]
            

            for id, lm in enumerate(my_Hand.landmark):
                

                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                    
               
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 10, (125,100,50), cv2.FILLED)
                
        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList= detector.findPosition(img)
        if len(lmList) !=0:
            print(lmList[4])
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        img=cv2.flip(img,1)

        cv2.putText(img, str(int(fps)), (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 2, (300, 10, 75), 1)

        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
