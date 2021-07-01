import cv2 as cv

face_casecade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture("output.avi")

while cap.isOpened():
    _, frame = cap.read()
    gray_img: None = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detect: None = face_casecade.detectMultiScale(gray_img, 1.1, 4)

    for (x, y, w, h) in face_detect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)

        cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break
cap.release()
cv.destroyAllWindows()
