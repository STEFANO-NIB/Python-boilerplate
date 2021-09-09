from src import app
from flask import jsonify
import os
import sys

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'src'))


@app.route('/', methods=['GET'])
def index():
    return jsonify('This ran successfully'), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
