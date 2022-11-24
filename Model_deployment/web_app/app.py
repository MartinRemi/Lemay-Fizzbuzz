from flask import Flask, request, jsonify
from ml_model import MLModel

server = Flask(__name__)
model = MLModel()

def run_request():
	return model.predict(request.json['sentence'])

@server.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return 'The model is up and running. Send a POST request'
	else:
		return run_request()