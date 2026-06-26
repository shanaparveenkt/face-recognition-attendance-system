import smtplib
from email.mime.text import MIMEText

def send_email(parent_email, student_name):
    sender = "YOUR_EMAIL"
    password = "YOUR_APP_PASSWORD"


    subject = "Attendance Notification"
    body = f"""
Hello Parent,

This is to inform you that {student_name} has been marked present today.

Regards,
Attendance System
"""

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = parent_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, parent_email, msg.as_string())
        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Email error:", e)