import os
from flask import Flask, request, jsonify, json
from flask_cors import CORS
from ocr import read_text_from_image
from fetch import get_data


def create_app():
    # create and configure the app
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    @app.route('/', methods = ['POST'])
    def api_root():
        if request.headers['Content-Type'] == 'application/json':
            img_path = get_data(request.json['image'])
            message = read_text_from_image(img_path)
            message['img_path'] = request.json['image']
            resp = jsonify(message)
            resp.status_code = message['status']
        else:
            message = {
                    'status': 415,
                    'caption': 'Unsupported media type',
                    'img_path': img_path
            }
            resp = jsonify(message)
            resp.status_code = 415

        return resp
    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    create_app().run(host='0.0.0.0', port=port)
