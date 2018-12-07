import os, sys
from flask import Flask, request, jsonify, json
from flask_cors import CORS
from fetch_and_parse import parse


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    CORS(app, supports_credentials=True)

    @app.route('/', methods = ['POST'])
    def api_root():
        if request.headers['Content-Type'] == 'application/json':
            message = parse(request.json['image'])
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

    @app.route('/upload', methods = ['POST'])
    def upload():
        print("NOTE: request.get_json():", request.get_json(), '\n\n')
        print("NOTE: request.data:", request.data, '\n\n')
        print("NOTE: request.headers", request.headers, '\n\n')
        print('NOTE: request.__dict__:', request.__dict__, '\n\n')
        print('NOTE: request.form:', request.form, '\n\n')
        print('NOTE: request.args:', request.args, '\n\n')
        print('NOTE: request.files:', request.files, '\n\n')
        print('NOTE: request.values:', request.values, '\n\n')

        sys.stdout.flush()

        message = {
                'status': 200,
                'caption': 'not yet set up to return caption',
        }
        resp = jsonify(message)
        resp.status_code = 200

        return resp

    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    create_app().run(host='0.0.0.0', port=port, debug=True)
