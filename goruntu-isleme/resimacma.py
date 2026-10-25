import cv2
import numpy as np

resim = cv2.imread("IUC.png",0)

cv2.imshow("IUC Logo",resim)

cv2.imwrite("siyahbeyaziuc.png",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
