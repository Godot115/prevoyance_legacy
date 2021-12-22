from flask import Flask, render_template, request, make_response, json
from DoseResponse import FirstOrder

app = Flask(__name__)


@app.route('/Design', methods=['GET', 'POST'])
def design():  # put application's code here
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        model = str(request.form.get('model'))
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
        points = FirstOrder.createInitialPoints(lowerBoundary,upperBoundary)
        if model == 'model3':
            optimalDesign = FirstOrder.firstOrderModel3(points, lowerBoundary, upperBoundary, plus_minus_sign,
                                                        iterateTimes, grid, *args)
        else:
            optimalDesign = FirstOrder.firstOrder(points, lowerBoundary, upperBoundary, model, iterateTimes,
                                                  grid, *args)
        response = make_response(json.dumps(optimalDesign))
        response.mimetype = 'application/json'
        return response


if __name__ == '__main__':
    app.run()
