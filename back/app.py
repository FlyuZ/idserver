from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

OS_PATH = os.path.abspath(os.path.dirname(__file__) + '\\static') + '\\img' + '\\'


@app.route('/', methods=["GET"])
def index():
    return "Welcome to API v1, try /hello."

@app.route('/uploadImage', methods=['POST'])
def upload_image():
    # 图片对象
    file_obj = request.files.get('file')
    # 图片名字
    file_name = request.form.get('fileName')
    # 图片保存的路径
    save_path = OS_PATH + str(file_name)
    # 保存
    file_obj.save(save_path)
    return '图片保存成功'

@app.route('/getImage/', methods=['GET'])
def get_image():
    file_name = request.args.get('fileName')
    # 图片保存的路径
    save_path = OS_PATH + str(file_name)
    # 读取图片
    with open(save_path, 'rb') as f:
        img = f.read()
    return img

class Hello(Resource):
    @staticmethod
    def get():
        return "[get] hello flask"

    @staticmethod
    def post():
        return "[post] hello flask"


api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
