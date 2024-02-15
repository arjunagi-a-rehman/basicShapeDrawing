from flask import Flask, jsonify, request,render_template
from flask_cors import CORS
from flask_pymongo import PyMongo
from werkzeug.exceptions import HTTPException

app = Flask(__name__,template_folder='templates')
CORS(app)
app.config['MONGO_URI'] = 'mongodb+srv://rehmanarjunagi:Abdul123@cluster0.qu7wfai.mongodb.net/shapes?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

from src.controller import shapeController