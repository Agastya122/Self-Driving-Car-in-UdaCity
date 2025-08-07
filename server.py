import socketio
import eventlet
import eventlet.wsgi
from flask import Flask
from io import BytesIO
import base64
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam
import cv2 as cv

sio = socketio.Server()
app = Flask(__name__)

speed_limit = 20
model = load_model('self_drive.h5', compile = False)
model.compile(optimizer=Adam(learning_rate=1e-4), loss=MeanSquaredError)

def preprocess(image):
    image = np.array(image)
    image = image[60:135, :, :]
    image = cv.cvtColor(image, cv.COLOR_RGB2YUV)
    image = cv.GaussianBlur(image, (3,3), 0)
    image = cv.resize(image, (200, 66))
    image = image/255.0
    return image

@sio.on('telemetry')
def telemetry(sid, data):
    
    image_str = data["image"]
    image = Image.open(BytesIO(base64.b64decode(image_str)))
    speed = float(data['speed'])
    image_array = preprocess(image)
    steering_angle = float(model.predict(image_array[None, :, :, :], batch_size=1)[0])

    throttle = 1.0 - speed/speed_limit

    print(f"Steering Angle: {steering_angle:.4f}, Throttle: {throttle}")
    send_control(steering_angle, throttle)


@sio.on('connect')
def connect(sid, environ):
    print("Connected to simulator.")
    send_control(0, 0)

def send_control(steering_angle, throttle):
    sio.emit(
        "steer",
        data={
            'steering_angle': str(steering_angle),
            'throttle': str(throttle)
        },
        skip_sid=True
    )

if __name__ == '__main__':
    app = socketio.WSGIApp(sio, app)
    print("Server is running at http://0.0.0.0:4567")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 4567)), app)
