from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api
import os
import base64
import cv2
# from id.inference import init_env, inference_single
from id.video import Camera

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

OS_PATH = os.path.abspath(os.path.dirname(__file__) + '\\static') + '\\'


@app.route('/index', methods=["GET"])
def index():
    return "Welcome to API v1, try /hello."

@app.route('/uploadAndInfer', methods=['POST'])
def upload_and_infer():
    file_obj = request.files.get('file')
    file_name = request.form.get('fileName')
    # res = inference_single(file_obj)
    return 'success'


@app.route('/initIDenv/', methods=['GET'])
def init_id_env():
    gallery = request.values.get('gallery')
    print(gallery)
    # init_env("resnetst")
    return "success"

def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


# @app.route('/video_feed')
# def video_feed():
#     """Video streaming route. Put this in the src attribute of an img tag."""
#     return Response(gen(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed', methods=['GET'])
def video_feed():
    img = cv2.imread(OS_PATH + '1.jpg')
    import random
    if(random.randint(0, 1) == 0):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_base64 = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
    return jsonify({"imgbase64": img_base64, "id": "100"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
