import cv2

resim = cv2.imread("bebek.jpg")

meanFilter = cv2.blur(resim,(3,3))
meanFilter2 = cv2.blur(resim,(5,5))
meanFilter3 = cv2.blur(resim,(7,7))

medianFilter = cv2.medianBlur(resim,3)
medianFilter2 = cv2.medianBlur(resim,5)
medianFilter3 = cv2.medianBlur(resim,7)

gauss = cv2.GaussianBlur(resim,(3,3),0)
gauss2 = cv2.GaussianBlur(resim,(5,5),0)
gauss3 = cv2.GaussianBlur(resim,(7,7),0)

cv2.imshow("Orijinal",resim)
cv2.imshow("Mean Filter 1",meanFilter)
cv2.imshow("Mean Filter 2",meanFilter2)
cv2.imshow("Mean Filter 3",meanFilter3)

cv2.imshow("Median Filter 1",medianFilter)
cv2.imshow("Median Filter 2",medianFilter2)
cv2.imshow("Median Filter 3",medianFilter3)

cv2.imshow("Gauss 1",gauss)
cv2.imshow("Gauss 2",gauss2)
cv2.imshow("Gauss 3",gauss3)


cv2.waitKey(0)
cv2.destroyAllWindows()