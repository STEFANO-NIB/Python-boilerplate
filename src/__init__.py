from flask import Flask, request, jsonify
import os
import glob
import importlib
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Find all files postfixed with '_controller' in order to add to the route
for f in glob.glob(
    os.path.dirname(__file__) +
    "/**/*_controller.py",
        recursive=True):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
