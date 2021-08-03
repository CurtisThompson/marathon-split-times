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
    #curl -X POST 127.0.0.1:5000/predict -H "Content-Type: application/json" -d "['14:10', '14:10']"
    if request.method == 'POST':
        data = eval(request.get_data())
        prediction = split_predictor.predict_finishing_time(data)
    return prediction


if __name__ == '__main__':
    load_model()
    app.run()