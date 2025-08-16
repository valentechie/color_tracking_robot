#  Color Tracking Robot

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Language](https://img.shields.io/badge/Pyhton-darkblue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

📚 **Table of Contents**

- [Introduction](#-introduction)
- [Demo](#-demo)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [File Overview](#-file-overview)
- [Project Context](#-project-context)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Introduction

Python project for real-time color-based object tracking using OpenCV.  
Detects and follows objects of a chosen color in live video.  

Perfect as a first step into computer vision, image processing, and robotics. Easy to extend for simulated or physical robots, and for educational experiments.

---

## 🎬 Demo

![Demo GIF](demo.gif) <!-- Add your demo gif or image here -->

---

## 🛠️ Requirements

- Python 3.8+
- OpenCV (`opencv-python`)
- NumPy

---

## 📦 Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/valentechie/color_tracking_robot.git
```

2️⃣ Navigate to the project folder:

```bash
cd color_tracking_robot
```

3️⃣ Install dependencies:

```bash
pip install opencv-python numpy
```

---

## 🕹️ Usage

Run the main script:

```bash
python color_object_tracker.py
```

- Use your webcam to start tracking.
- Default color can be changed in the script (HSV values).
- Press **`q`** to exit.

---

## 📁 File Overview

- **`color_object_tracker.py`**: Main tracking logic.
- **`README.md`**: Project documentation.
- **`requirements.txt`**: List of Python dependencies.

---

## 🎓 Project Context

Developed as a robotics and computer vision learning tool.  
Great for experimenting with image segmentation, contour detection, and real-time tracking.  
Inspired by hands-on projects and practical robotics integrations.

---

## 🤝 Contributing

Contributions are welcome!

- Fork this repository
- Open issues for bugs, ideas, or improvements
- Submit pull requests to enhance the project

---

## 📄 License

This project is licensed under the [MIT](LICENSE).