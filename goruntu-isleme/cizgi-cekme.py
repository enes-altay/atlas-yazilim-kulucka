import cv2 
import numpy as np

resim = np.zeros((500,500,3),dtype="uint8")

cv2.line(resim,(0,0),(100,100),(55,67,90),3)
cv2.circle(resim,(150,150),25,(187,122,40),2)
cv2.putText(resim,"Enes",(300,300),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)

cv2.imshow("Deneme",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()