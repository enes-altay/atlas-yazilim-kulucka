import cv2
import numpy as np

image=cv2.imread("gurultulu.png")

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(image,kernel,iterations=1)

dilation=cv2.dilate(image,kernel,iterations=1)

opening=cv2.morphologyEx(image, cv2.MORPH_OPEN,kernel)

closing=cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)

gradyan=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)

tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)

blackhat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("orjinal", image)
cv2.imshow("dilation", dilation)
cv2.imshow("erosion",erosion)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradyan",gradyan)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()