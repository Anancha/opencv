import cv2 as cv

img = cv.imread("abert.jpg", 0)

cv.imshow("Image", img)
e = cv.waitKey()

if e == 27:
    cv.destroyAllWindows()
elif e == ord("s"):
    cv.imwrite("The-New_Albert.jpg", img)
    cv.destroyAllWindows()

# Test upload to github  Anucha  5555555
