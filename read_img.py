import cv2 as cv

img = cv.imread("data/lena.jpg", 1)   # 1: color, 0: gray

print(img)


cv.imshow("Image", img)
cv.waitKey(delay=0)

cv.destroyAllWindows()
