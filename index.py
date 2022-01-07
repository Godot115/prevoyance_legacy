import matplotlib.pyplot as plt
from flask import Flask, render_template, request, make_response, json, jsonify, send_file

from DoseResponse import FirstOrder
from DoseResponse import plotOfFunction

app = Flask(__name__)


@app.route('/Design', methods=['GET'])
def design():  # put application's code here
    if request.method == 'GET':
        return render_template("index.html")


@app.route('/Compute', methods=['POST'])
def compute():
    model = request.form.get('model')
    a = float(request.form.get('a'))
    b = float(request.form.get('b'))
    c = float(request.form.get('c'))
    d = float(request.form.get('d'))
    args = (a, b, c, d)
    plus_minus_sign = request.form.get('plus_minus_sign')
    lowerBoundary = float(request.form.get('lowerBoundary'))
    upperBoundary = float(request.form.get('upperBoundary'))
    grid = int(request.form.get('grid'))
    iterateTimes = int(request.form.get('iterateTimes'))
    points = FirstOrder.createInitialPoints(lowerBoundary, upperBoundary)
    print(model)
    optimalDesign = FirstOrder.firstOrder(points, lowerBoundary, upperBoundary,
                                          plus_minus_sign, model, iterateTimes,
                                          grid, *args)
    # response = dict(optimalDesign)
    # response = make_response(json.dumps(response))
    # response.mimetype = 'application/json'
    return jsonify(optimalDesign)


@app.route('/Plot', methods=['POST'])
def plotFunction():
    plt.clf()
    model = str(request.form.get('model'))
    a = float(request.form.get('a'))
    b = float(request.form.get('b'))
    c = float(request.form.get('c'))
    d = float(request.form.get('d'))
    args = (a, b, c, d)
    plus_minus_sign = request.form.get('plus_minus_sign')
    lowerBoundary = float(request.form.get('lowerBoundary'))
    upperBoundary = float(request.form.get('upperBoundary'))
    figure = plotOfFunction.plotFunc(model, plus_minus_sign, lowerBoundary, upperBoundary, *args)
    image = plotOfFunction.imgToBase64(figure)
    return jsonify(image)

if __name__ == '__main__':
    app.run()
