from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import base64

import sys
import os

sys.path.append(os.path.abspath("./Model"))
from load.py import *

app = Flask(__name__)
global model, graph
model, graph = init()


def convertImage(imgData):
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.decodebytes(imgstr))


@app.route('/')
def index():
    return render_template("index3.html")


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    imgData = request.get_data()
    convertImage(imgData)
    print
    "debug"
    x = imread('output.png', mode='L')
    x = np.invert(x)
    x = imresize(x, (28, 28))
    x = x.reshape(1, 28, 28, 1)
    print
    "debug2"
    # in our computation graph
    with graph.as_default():
        out = model.predict(x)
        print(out)
        print(np.argmax(out, axis=1))
        print
        "debug3"
        # convert the response to a string
        response = np.array_str(np.argmax(out, axis=1))
        return response


if __name__ == "__main__":
    # decide what port to run the app in
    port = int(os.environ.get('PORT', 5000))
    # run the app locally on the givn port
    app.run(host='127.0.0.1', port=port)
# optional if we want to run in debugging mode
# app.run(debug=True)
