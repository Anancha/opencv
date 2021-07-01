import cv2 as cv

img = cv.imread("albert.jpg", 0)
print(img)


cv.imshow("Image", img)
cv.waitKey(delay=0)

cv.destroyAllWindows()
