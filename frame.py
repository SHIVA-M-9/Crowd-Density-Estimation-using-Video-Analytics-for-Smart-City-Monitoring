import cv2
import os

base_path = os.path.dirname(os.path.abspath(__file__))
face_path = os.path.join(base_path, 'haarcascade_frontalface_default.xml')
eye_path = os.path.join(base_path, 'haarcascade_eye_tree_eyeglasses.xml')

face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)

cap = cv2.VideoCapture(0)  # for webcam

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

while cap.isOpened():
    ret, img = cap.read()
    if not ret or img is None:
        print("Error: Couldn't read frame or end of video.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey ,ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    cv2.imshow('img', img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
