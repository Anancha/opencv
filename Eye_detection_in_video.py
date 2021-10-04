import cv2 as cv

eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv.VideoCapture("BNK48.mp4")
#cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    eye_detect = eye_cascade.detectMultiScale(gray_img)
    
    for (x, y, w, h) in eye_detect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv.imshow("Eye Detection", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

