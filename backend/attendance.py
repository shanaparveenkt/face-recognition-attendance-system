import cv2
from database import cursor, db
from datetime import datetime
from email_service import send_email

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("../model/trainer.yml")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)

marked_today = set()

while True:
    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        student_id, confidence = recognizer.predict(face)

        if confidence < 70:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            # Check if attendance already exists today
            cursor.execute(
                "SELECT * FROM attendance WHERE student_id=%s AND date=%s",
                (student_id, date)
            )
            result = cursor.fetchone()

            if result is None and student_id not in marked_today:
                query = """
                INSERT INTO attendance (student_id, date, time, status)
                VALUES (%s,%s,%s,%s)
                """
                values = (student_id, date, time, "Present")
                cursor.execute(query, values)
                db.commit()
                
                cursor.execute(
                     "SELECT name, parent_email FROM students WHERE id=%s",
                     (student_id,)
                )

                student = cursor.fetchone()

                if student:
                     student_name = student[0]
                     parent_email = student[1]
                     
                     send_email(parent_email, student_name)


                marked_today.add(student_id)

                print(f"Attendance marked for {student_id}")

            cv2.putText(frame, f"ID: {student_id}", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()