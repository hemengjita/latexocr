import base64

from PIL import Image
from flask import Flask, render_template, request, jsonify
import requests
from io import BytesIO

app = Flask(__name__)

MODEL_API_ENDPOINT = "http://172.16.185.157:8502/predict/"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    # 从请求中获取Base64编码的图片数据
    image_data_base64 = request.json["image_data"]
    image_data = base64.b64decode(image_data_base64)


    # 使用BytesIO对象作为BufferedReader发送请求
    buffered_image = BytesIO(image_data)
    # print(buffered_image)
    # 使用图片数据发送请求到模型API
    response = requests.post(MODEL_API_ENDPOINT, files={'file': buffered_image})
    # 检查模型API的响应状态
    if response.status_code == 200:
        latex_result = response.text
        # latex_result = response.json()

        structured_data = {
            "latex_code": latex_result
        }
        print(structured_data)
        return jsonify(structured_data)
    else:
        return jsonify(error="Model prediction failed."), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8501)
