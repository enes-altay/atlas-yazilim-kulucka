import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret , goruntu = kamera.read()

    if not ret:
        print("Goruntu alinamadi")
        break

    cv2.rectangle(goruntu,(100,100),(400,400),(255,0,0),1)
    cv2.line(goruntu,(100,0),(200,250),(0,0,255),2)
    cv2.circle(goruntu,(50,50),25,(0,255,0),2)
    cv2.putText(goruntu,"Enes",(250,150),cv2.FONT_HERSHEY_COMPLEX,1,(255,10,10),1)

    cv2.imshow("A",goruntu)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()

cv2.destroyAllWindows()