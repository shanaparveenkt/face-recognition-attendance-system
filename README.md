# 🎯 AI-Powered Face Recognition Attendance System

An intelligent attendance management system that automates student attendance using **Computer Vision**, **Machine Learning**, **MySQL**, and **Email Automation**. The system recognizes students in real time through facial recognition, automatically marks attendance, stores records securely in a database, prevents duplicate attendance, and instantly notifies parents via email.

---

# 📌 Problem Statement

Traditional attendance systems are manual, time-consuming, and prone to human error. Maintaining accurate attendance records while ensuring timely communication with parents can be challenging for educational institutions.

This project addresses these challenges by developing an AI-powered attendance management system that:

- Recognizes students in real time using face recognition
- Automatically marks attendance
- Stores attendance records securely in a MySQL database
- Prevents duplicate attendance for the same day
- Sends instant attendance notifications to parents

---

# 💡 Solution Overview

The Face Recognition Attendance System leverages Computer Vision and Machine Learning to automate attendance tracking.

### System Workflow

```text
Webcam Capture
      ↓
Face Detection (Haar Cascade)
      ↓
Face Recognition (LBPH)
      ↓
Attendance Validation
      ↓
Store Attendance in MySQL
      ↓
Email Notification to Parent
```

The result is a fast, reliable, and fully automated attendance management workflow.

---

# 🚀 Key Features

- ✅ Real-time face detection using webcam
- ✅ Face recognition using the LBPH algorithm
- ✅ Automated attendance marking
- ✅ MySQL database integration
- ✅ Duplicate attendance prevention (one attendance per student per day)
- ✅ Automatic email notifications to parents
- ✅ Secure and efficient attendance tracking
- ✅ Scalable architecture for schools and colleges

---

# 🛠 Technology Stack

## Programming Language

- Python

## Libraries & Frameworks

- OpenCV
- NumPy
- Flask
- Flask-CORS
- MySQL Connector

## Database

- MySQL

## Computer Vision & AI

- Haar Cascade Classifier
- LBPH Face Recognizer

## Email Service

- SMTP (Gmail App Password Authentication)

---

# 🏗 System Architecture

```text
Student Face
      ↓
Webcam Capture
      ↓
Face Detection (Haar Cascade)
      ↓
Face Recognition (LBPH)
      ↓
Attendance Validation
      ↓
Store in MySQL Database
      ↓
Email Notification to Parent
```

---

# 📂 Project Structure

```text
ATTENDANCE_SYSTEM/
│
├── backend/
│   ├── app.py
│   ├── attendance.py
│   ├── database.py
│   ├── email_service.py
│   ├── face_trainer.py
│   ├── model/
│   │   └── trainer.yml
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

# ⚙ Workflow

## Step 1: Student Registration

Student information is stored in the MySQL database.

Required details:

- Student ID
- Student Name
- Roll Number
- Parent Email

---

## Step 2: Dataset Collection

Multiple facial images are collected for each student.

Example:

```text
student_images/
├── 101/
├── 102/
└── 103/
```

These images are used to train the face recognition model.

---

## Step 3: Model Training

Train the LBPH face recognition model.

```bash
python face_trainer.py
```

Output:

```text
trainer.yml
```

---

## Step 4: Face Detection

The webcam continuously captures live video input.

Using the Haar Cascade Classifier:

- Detects faces
- Extracts facial regions
- Sends detected faces to the recognition model

---

## Step 5: Face Recognition

The detected faces are processed by the trained LBPH Face Recognizer.

The model:

- Predicts the Student ID
- Calculates the confidence score
- Identifies the student

---

## Step 6: Attendance Marking

If recognition is successful:

- Student ID is identified
- Attendance is marked automatically
- Duplicate attendance is prevented

Attendance is restricted to **one entry per student per day**, ensuring accurate and reliable attendance records.

---

## Step 7: Email Notification

After successful attendance marking:

- Parent email is retrieved from the MySQL database
- An attendance confirmation email is sent automatically

Example:

```text
Subject: Attendance Notification

Hello Parent,

This is to inform you that your child has been marked present today.

Regards,
Attendance System
```

---

# 🗄 Database Schema

## Students Table

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    roll_no VARCHAR(50),
    parent_email VARCHAR(100)
);
```

---

## Attendance Table

```sql
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    time TIME,
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

---

## Unique Constraint

Prevents duplicate attendance records.

```sql
ALTER TABLE attendance
ADD CONSTRAINT unique_attendance
UNIQUE(student_id, date);
```

---

# ⚡ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/face-recognition-attendance-system.git

cd face-recognition-attendance-system
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

---

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

## Train the Face Recognition Model

```bash
python face_trainer.py
```

---

## Start the Attendance System

```bash
python attendance.py
```

---

# 📈 Business Impact

This system improves institutional efficiency by:

- Reducing manual attendance workload
- Increasing attendance accuracy
- Eliminating proxy attendance
- Providing real-time communication with parents
- Saving time and administrative effort
- Automating the complete attendance process

---

# 🔍 Challenges Solved

- Real-time face detection
- Accurate face recognition
- Duplicate attendance prevention
- MySQL database integration
- Automated email notifications
- End-to-end attendance automation

---

# 🚀 Future Enhancements

- 📊 Attendance Dashboard
- 📈 Attendance Analytics
- 📄 PDF & Excel Report Generation
- 🚨 Unknown Face Alerts
- 📷 Multi-Camera Support
- ☁ Cloud Deployment
- 🧠 FaceNet / CNN-based Recognition
- 📱 Mobile Application

---

# 🎯 Use Cases

- Schools
- Colleges
- Universities
- Coaching Centers
- Offices
- Educational Institutions

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Computer Vision
- Machine Learning
- Face Recognition
- Database Management
- Python Automation
- Real-Time AI Systems
- Backend Development
- Email Automation

---

# 👩‍💻 Author

**Shana Parveen KT**

**Data Analyst | Data Science Enthusiast | AI & Business Intelligence Learner**

Passionate about building intelligent, data-driven solutions using Artificial Intelligence, Machine Learning, Computer Vision, and Data Analytics to solve real-world problems.

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates me to build more AI-powered and data-driven projects!

**⭐ Don't forget to star the repository if you found it helpful!**
