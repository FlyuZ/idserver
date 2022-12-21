from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
import os
from id.inference import init_env, inference_single

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

OS_PATH = os.path.abspath(os.path.dirname(__file__) + '\\static') + '\\img' + '\\'


@app.route('/index', methods=["GET"])
def index():
    return "Welcome to API v1, try /hello."

@app.route('/uploadAndInfer', methods=['POST'])
def upload_and_infer():
    # 图片对象
    file_obj = request.files.get('file')
    # 图片名字
    file_name = request.form.get('fileName')
    # 图片类型
    # res = inference_single(file_obj)
    return '图片保存成功'


@app.route('/initIDenv/', methods=['GET'])
def init_id_env():
    # init_env("resnetst")
    return "success"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
