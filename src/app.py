import pickle
import numpy as np
from flask import Flask, request
from split_time_predictor import SplitTimePredictor

split_predictor = None
app = Flask(__name__)


def load_model():
    global split_predictor
    split_predictor = SplitTimePredictor()


@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    if request.method == 'POST':
        data = eval(request.get_data())
        prediction = split_predictor.predict_finishing_time(data)
    return prediction


if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=80)