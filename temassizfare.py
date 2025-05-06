# -*- coding: utf-8 -*-
import cv2
import time
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands= mpHand.Hands(static_image_mode=0,max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()


pTime = 0
cTime = 0

screen_w, screen_h = pyautogui.size()

while True:
    succes, img = cap.read()
    imgRGB =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlandmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handlandmarks, mpHand.HAND_CONNECTIONS)
            
            for id, landmark in enumerate(handlandmarks.landmark):
                print(id,landmark)
                #Her Sayının elde bir eklem karşılığı var
                #https://ai.google.dev/static/mediapipe/images/solutions/hand-landmarks.png?hl=tr
                
                h, w, c = img.shape
                cx, cy = int(landmark.x*w), int(landmark.y*h)
                
                if id==8:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                    mouse_x = int(landmark.x*screen_w)
                    mouse_y = int(landmark.y*screen_h)
                    pyautogui.moveTo(mouse_x,mouse_y)
                
                if id==4:
                    thumb_x,thumb_y = int(landmark.x*w),int(landmark.y*h)
                    
                    
            xdistance =abs(cx-thumb_x)
            ydistance =abs(cy-thumb_y)
            
            if xdistance < 30 and ydistance < 30:
                pyautogui.click()
                pyautogui.sleep(0.3)
            
            
    #FPS
    cTime = time.time()
    fps = 1 / (cTime- pTime)
    pTime = cTime
    
    cv2.putText(img, "FPS: "+str(int(fps)), (10,75), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 5)
    
    
    cv2.imshow("fare", img)
    cv2.waitKey(1)