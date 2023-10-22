# cameraDisplay.py
# import the opencv library
# Import necessary libraries
from flask import Flask, render_template, Response
import cv2

# Initialize the Flask app
app = Flask(__name__)

# define a video capture object
vid = cv2.VideoCapture(0)

while True:

    # Capture the video frame
    # by frame
    # ret, frame = vid.read()

    def gen_frames():
        while True:
            success, video_frame = vid.read()  # read the camera frame
            frame = cv2.flip(video_frame, 1)
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


    @app.route('/')
    def index():
        return render_template('cameraSample.html')


    @app.route('/video_feed')
    def video_feed():
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


    if __name__ == "__main__":
        app.run(debug=True)

