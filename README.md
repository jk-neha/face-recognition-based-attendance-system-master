# 🎓 Face Recognition Based Attendance System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**An intelligent, automated attendance management system powered by real-time face recognition.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure) • [Contributing](#-contributing)

</div>

---

## 📌 Overview

The **Face Recognition Based Attendance System** automates the process of marking student or employee attendance using live facial recognition. By replacing manual roll-calls and ID-card swipes, it reduces human error, prevents proxy attendance, and logs records instantly into a structured CSV file.

Built with Python, OpenCV, and the `face_recognition` library, this system can recognize multiple faces in real time via a webcam feed.

---

## ✨ Features

- 🔍 **Real-Time Face Detection** — Detects and recognizes faces live via webcam
- 📋 **Automated Attendance Logging** — Marks attendance with timestamp into a CSV file
- 👤 **Multi-Face Support** — Recognizes multiple registered individuals simultaneously
- 🧠 **Face Encoding Storage** — Encodes and stores face data for fast, accurate matching
- 📁 **CSV Report Generation** — Generates date-wise attendance sheets automatically
- 🚫 **Proxy Prevention** — Physical presence required; no manual overrides
- 🖥️ **Simple GUI Interface** — Easy-to-use interface for registration and attendance marking

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.7+ |
| Face Recognition | `face_recognition` (dlib-based) |
| Computer Vision | OpenCV (`cv2`) |
| Data Storage | CSV files |
| GUI | Tkinter |
| Numerical Computing | NumPy |

---

## 📁 Project Structure

```
face-recognition-attendance-system/
│
├── TrainingImage/              # Stores captured face images for training
├── TrainingImageLabel/         # Encoded face data (trainer.yml)
├── StudentDetails/             # CSV file with registered student records
├── Attendance/                 # Date-wise attendance CSV files
│
├── haarcascade_frontalface_default.xml   # Haar Cascade for face detection
│
├── AtalRecognition.py          # Core face recognition logic
├── training.py                 # Model training script
├── automaticAttedance.py       # Automated attendance marking
├── app.py                      # Main application / GUI entry point
│
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- A working webcam

### Step 1 — Clone the Repository

```bash
git clone https://github.com/jk-neha/face-recognition-based-attendance-system-master.git
cd face-recognition-based-attendance-system-master
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `dlib` and `face_recognition` may require additional system packages. On Ubuntu/Debian:
> ```bash
> sudo apt-get install build-essential cmake libopenblas-dev liblapack-dev
> ```
> On Windows, consider using pre-built wheels from [this guide](https://github.com/ageitgey/face_recognition/blob/master/README.md#installation).

### Step 3 — Run the Application

```bash
python app.py
```

---

## 🚀 Usage

### 1. Register a New Student/Employee

1. Launch the application via `python app.py`
2. Enter the **ID** and **Name** of the individual
3. Click **"Take Images"** — the system captures 50–100 face samples via webcam
4. Click **"Train Model"** to generate the facial encoding

### 2. Mark Attendance

1. Click **"Automatic Attendance"**
2. The webcam activates and scans for registered faces in real time
3. Recognized individuals are automatically marked **Present** with a timestamp
4. Attendance is saved to `Attendance/<date>.csv`

### 3. View Attendance Records

- Open the generated `.csv` files inside the `Attendance/` folder
- Each file is named by date (e.g., `Attendance_16-05-2026.csv`) and contains:

| ID | Name | Date | Time |
|----|------|------|------|
| 101 | Neha Sharma | 16-05-2026 | 09:03:21 |

---

## 📸 Demo

> _Add a screenshot or GIF of your running application here._

```
[ Screenshot Placeholder ]
```

To add a demo image:
```markdown
![Demo](results\ui_face_rec.png)
```

---

## 🔧 Configuration

You can adjust the following parameters in the source files:

| Parameter | File | Default | Description |
|-----------|------|---------|-------------|
| Sample images count | `app.py` | `50` | Number of images captured per person |
| Recognition tolerance | `AtalRecognition.py` | `0.6` | Lower = stricter matching |
| Camera index | `app.py` | `0` | Change if using an external webcam |

---

## 🐛 Known Issues & Limitations

- Performance may degrade in low-light environments
- Accuracy can be affected by significant changes in appearance (e.g., masks, glasses)
- Currently supports local storage only (no database integration)
- Designed for single-camera setups

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m 'Add: your feature description'`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

Please ensure your code follows PEP 8 style guidelines and includes relevant comments.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition) — for the face recognition library
- [OpenCV](https://opencv.org/) — for real-time computer vision capabilities
- [dlib](http://dlib.net/) — for the underlying facial landmark detection

---

<div align="center">

Made with ❤️ | If you found this useful, please ⭐ star the repository!

</div>
