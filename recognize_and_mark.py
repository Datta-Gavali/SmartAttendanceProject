import cv2
import os
import django
from datetime import date
import time

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from attendance.models import Student, Attendance

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

attendance_marked = False

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera Error")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in faces:

        student_id, confidence = recognizer.predict(gray[y : y + h, x : x + w])

        # print("ID:", student_id, "Confidence:", confidence)

        # STRICT MATCH
        if confidence < 85:

            try:
                student = Student.objects.get(id=student_id)

                # Check duplicate attendance
                already_marked = Attendance.objects.filter(
                    student=student, date=date.today()
                ).exists()

                if already_marked:
                    status = "Already Marked"

                else:
                    Attendance.objects.create(student=student)
                    status = "Attendance Saved"
                    attendance_marked = True

                name = student.name

            except Student.DoesNotExist:
                name = "Unknown"
                status = "Student Not Found"

        else:
            name = "Unknown"
            status = "Face Not Matched"

        # Draw face box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Show name
        cv2.putText(
            frame, name, (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
        )

        # Show status
        cv2.putText(
            frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2
        )

    cv2.imshow("Smart Attendance", frame)

    # Close after successful attendance
    if attendance_marked:
        print("Attendance Saved Successfully")
        time.sleep(2)
        break

    # Manual close
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Closing Camera")
        break

cap.release()
cv2.destroyAllWindows()
