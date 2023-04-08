from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/yahoo')
def out_json():
    if os.path.exists('./yahoo_finances/yahoo_finances/yahoo.json'):
        with open('./yahoo_finances/yahoo_finances/yahoo.json', 'r') as f:
           content = f.read()
           json_content = json.loads(content)
           return jsonify(json_content), 200, {'Content-Type': 'application/json; charset=utf-8'}

    else:
        json_content = {
            'error': True,
            'message': 'The file ./yahoo_finances/yahoo_finances/yahoo.json not exists'
        }
        return jsonify(json_content), 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run()