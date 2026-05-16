# Face Recognition Based Attendance System

## 📌 Overview
This project is an AI-based attendance system that uses face recognition to automatically mark attendance using a webcam.

## 🚀 Features
- Real-time face detection using OpenCV
- Face recognition using trained model
- Automatic attendance marking in CSV
- Web interface using Flask + HTML
- Live webcam integration

## 🛠️ Tech Stack
- Python
- OpenCV
- Flask
- HTML/CSS
- Haar Cascade Classifier

## 📂 Project Structure
- app.py → main backend
- static/ → trained model + face images
- templates/ → frontend UI
- Attendance/ → attendance records

## ▶️ How to Run
```bash
pip install -r requirements.txt
python app.py

# face-recognition-based-attendance-system  

Do visit my blog for better explanations: https://machinelearningprojects.net/face-recognition-based-attendance-system/

![Face Recognition Based Attendance System](ss.png)
http://127.0.0.1:5000


📊 Results

This section demonstrates the working output of the Face Recognition Attendance System.

🖥️ 1. User Interface (Home Page)

The system provides a simple web interface built using Flask where users can register and start attendance.


<img width="1918" height="875" alt="ui_face_rec" src="https://github.com/user-attachments/assets/8b827287-1c10-4671-864c-59d012401657" />

👤 2. User Registration

A new user is added by capturing multiple face images through the webcam. These images are stored in the dataset for training the model.



Uploading user_registration.mp4…



📸 3. Live Attendance Marking

Once the face is recognized in real-time, the system automatically marks attendance with timestamp.


<img width="1915" height="871" alt="attendance_marked png" src="https://github.com/user-attachments/assets/748eea6b-2182-4d9a-80c1-13b2b633e081" />


📊 4. Attendance Output

Attendance is stored in a CSV file which can be exported and viewed easily.

Example format:

Name	Roll	Time
Neha	101	10:45:12
NEHA VARDHINI J K	12	14:34:44
[Attendance-05_16_26.csv](https://github.com/user-attachments/files/27852336/Attendance-05_16_26.csv)
Name,Roll,Time

agnes,120,13:34:45
Maha,1982,13:34:50
krishna,1978,13:34:51

NEHA VARDHINI J K,12,14:34:44



