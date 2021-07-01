import cv2 as cv

img = cv.imread("albert.jpg", 0)
print(img)

# Create New image
cv.imwrite("New-Abert1.jpg", img)

cv.waitKey(0)