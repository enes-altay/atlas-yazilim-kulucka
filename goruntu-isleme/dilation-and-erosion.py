import cv2
import numpy as np

resim = cv2.imread("gurultulu.png")
kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(resim,kernel,iterations = 1)
erosion = cv2.erode(resim,kernel,iterations = 1)
son = cv2.erode(dilation,kernel,iterations=2)
son2 = cv2.dilate(son,kernel, iterations=1)

cv2.imshow("Orijinal",resim)
cv2.imshow("Dilation",dilation)
cv2.imshow("Erosion",erosion)

cv2.imshow("Temiz en son",son2)

cv2.waitKey(0)
cv2.destroyAllWindows()