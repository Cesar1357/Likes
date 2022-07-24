import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips = [8, 12, 16, 20]
thumb_tip = 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            # Acceder a los puntos de referencia por su posición
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

               
            if  lm_list[4].y < lm_list[1].y:
                cv2.putText(img,"Me gusta",(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
                print("Me gusta")
            elif  lm_list[4].y > lm_list[1].y:
                cv2.putText(img,"No me gusta",(20,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
                print("No me gusta")

                
           


            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))


    cv2.imshow("Rastreo de manos", img)

    cv2.waitKey(1)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cv2.destroyAllWindows()
    
    
