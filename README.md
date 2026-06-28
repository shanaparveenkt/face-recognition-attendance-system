<div align="center"> # 🎯 AI-Powered Face Recognition Attendance System ### Intelligent Attendance Management using AI, Computer Vision & Automation Automate student attendance using real-time face recognition, database integration, and instant parent email notifications. ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white) ![AI](https://img.shields.io/badge/AI-Powered-success?style=for-the-badge) </div> --- # 📌 Overview The **AI-Powered Face Recognition Attendance System** is a smart attendance management solution that automates attendance marking using real-time face recognition technology. The system captures live video via webcam, detects and recognizes student faces using **LBPH (Local Binary Pattern Histogram)** with **OpenCV**, marks attendance automatically in a **MySQL database**, prevents duplicate entries for the same day, and sends instant email notifications to parents. This project combines: ✔ Artificial Intelligence ✔ Computer Vision ✔ Database Management ✔ Automation into a practical real-world application. --- # ✨ Features ✅ Real-time face detection using webcam ✅ Face recognition using LBPH algorithm ✅ Automatic attendance marking ✅ Duplicate attendance prevention (one attendance per day) ✅ Parent email notification system ✅ MySQL database integration ✅ Fast and efficient attendance tracking --- # 🛠 Tech Stack | Category | Technologies | |----------|--------------| | Language | Python | | Computer Vision | OpenCV, LBPH | | Database | MySQL | | Backend | Flask | | Email Service | SMTP | | Core Concepts | AI, Automation, Computer Vision | --- # 📂 Project Structure ```bash ATTENDANCE_SYSTEM/ │ ├── backend/ │ ├── app.py │ ├── database.py │ ├── attendance.py │ ├── face_trainer.py │ ├── email_service.py │ ├── model/ │ └── trainer.yml │ ├── requirements.txt ├── .gitignore └── README.md 

⚙ System Workflow

Step 1 — Student Registration

Student details stored in MySQL:

Student ID

Name

Roll Number

Parent Email

Step 2 — Dataset Collection

Each student has a dedicated image folder.

student_images/ ├── 101/ ├── 102/ └── 103/ 

Step 3 — Model Training

Train LBPH face recognizer:

python face_trainer.py 

Output:

trainer.yml 

Step 4 — Face Recognition

Webcam captures live video

Haar Cascade detects faces

LBPH recognizes student faces

Step 5 — Attendance Marking

When a student is recognized:

✔ Student identified
✔ Attendance stored in MySQL
✔ Duplicate prevention applied

Step 6 — Email Notification

Parent receives instant attendance notification.

Example:

Subject: Attendance Notification Hello Parent, This is to inform you that your child has been marked present today. Regards, Attendance System 

🚀 Installation

Clone Repository

git clone https://github.com/YOUR_USERNAME/face-recognition-attendance-system.git cd face-recognition-attendance-system 

Create Virtual Environment

python -m venv venv 

Activate:

venv\Scripts\activate 

Install Dependencies

pip install -r requirements.txt 

🗄 Database Setup

CREATE DATABASE attendance_system; USE attendance_system; 

Students Table:

CREATE TABLE students ( id INT PRIMARY KEY, name VARCHAR(100), roll_no VARCHAR(50), parent_email VARCHAR(100) ); 

Attendance Table:

CREATE TABLE attendance ( id INT AUTO_INCREMENT PRIMARY KEY, student_id INT, date DATE, time TIME, status VARCHAR(20), FOREIGN KEY (student_id) REFERENCES students(id) ); 

Constraint:

ALTER TABLE attendance ADD CONSTRAINT unique_attendance UNIQUE(student_id, date); 

▶ Running the Project

Train model:

python face_trainer.py 

Run attendance system:

python attendance.py 

📈 Future Enhancements

Admin Dashboard

Attendance Analytics

Export Reports

Unknown Face Detection

Multi-Camera Support

Deep Learning Models (CNN / FaceNet)

🎯 Use Cases

🏫 Schools
🎓 Colleges
🏢 Offices
📚 Coaching Centers
🏛 Institutions

📚 Learning Outcomes

Computer Vision

Face Recognition

Database Integration

Python Automation

Real-Time AI Applications

👩‍💻 Author

Shana Parveen

Data Science Enthusiast | AI & Analytics Learner | Passionate about building intelligent real-world solutions

⭐ If you found this project useful, consider giving it a star.

```
