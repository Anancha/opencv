import cv2 as cv

img = cv.imread('data/lena.jpg', 1)

img = cv.line(img, (0, 0), (255, 255), (0, 255, 0), 5)
''' เริ่มจาก 0,0  ไป 255,255 ตามด้วย code สี c]t ขนาด'''

img = cv.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

img = cv.rectangle(img, (0, 0), (510, 128), (0, 0, 255), 1)

img = cv.circle(img, (447, 63), 50, (0, 255, 0), -1)

font = cv.FONT_HERSHEY_PLAIN

img = cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 10, cv.LINE_AA)
cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
