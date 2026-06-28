import cv2
import os
import time

folder = "dataset/1"

if not os.path.exists(folder):
    os.makedirs(folder)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not opening")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for x, y, w, h in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face = frame[y : y + h, x : x + w]

        file_name = f"{folder}/{count}.jpg"
        cv2.imwrite(file_name, face)

        print("Saved:", file_name)

        count += 1

        # wait 2.5 seconds
        time.sleep(2.5)

        break

    # show count on screen
    cv2.putText(
        frame,
        f"Images Captured: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Face Capture", frame)

    if count >= 20:
        print("20 images captured successfully")
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
