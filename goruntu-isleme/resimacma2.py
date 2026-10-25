import cv2
import numpy as np

image1 = cv2.imread("kusResmi.jpg")

cv2.imshow("Kus",image1)

print("Boyut: ",image1.size)
print("Data type: ",image1.dtype)
print("Shape: ",image1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()