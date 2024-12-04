from flask import Flask, render_template, Response
import cv2
import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def generate_frame():
    

    current_dir = os.path.dirname(os.path.abspath(__file__))
    detector = cv2.CascadeClassifier(os.path.join(current_dir, 'Haarcascades', 'haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.join(current_dir, 'Haarcascades', 'haarcascade_eye.xml'))

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

            for (x, y, w, h) in faces:
                # Draw rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Region of interest for eyes
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                # Detect eyes within the face ROI
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Encode the frame to JPEG
            # Encoding and yielding the frame
            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            else:
                print("Failed to encode frame!")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
