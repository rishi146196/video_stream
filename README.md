# video_stream

---

# Flask Webcam Face and Eye Detection App

This is a Flask-based web application that uses OpenCV to detect faces and eyes from a live webcam feed. The application processes video frames in real time, drawing rectangles around detected faces and eyes, and streams the processed video to a web page.

## Features
- Real-time face and eye detection using Haar cascades from OpenCV.
- Live video feed streamed directly to a web browser.
- Simple and lightweight Flask-based web server.

## Requirements
The application requires the following dependencies:
- Python 3.x
- Flask
- OpenCV

All required libraries can be installed via the `requirement.txt` file.

## Installation
1. Clone this repository or download the source code.
2. Ensure you have Python 3 installed on your system.
3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```
4. Ensure Haarcascade XML files for face and eye detection are located in a folder named `Haarcascades` in the same directory as the application script (`app.py`).

## Usage
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open a web browser and navigate to `http://127.0.0.1:5000/` to view the live video stream with face and eye detection.

## File Descriptions
- `app.py`: Main application script containing Flask routes and OpenCV logic.
- `requirement.txt`: List of Python dependencies for the project.

## Notes
- Ensure your webcam is connected and accessible for the application.
- This project uses Haar cascades for face and eye detection. You can replace them with other detection models if needed.

---
