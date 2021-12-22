# y = a exp(x/b) a>0

import matplotlib.pyplot as plt
import numpy as np


def chooseModel(x, model, plus_minus_sign, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    if model == "model2":
        return a * np.exp(x / b)
    elif model == "model3":
        if plus_minus_sign == "positive":
            return a * np.exp((x / b) ** d)
        else:
            return a * np.exp(-(x / b) ** d)
    elif model == "model4":
        if plus_minus_sign == "positive":
            return a * (c - (c - 1) * np.exp(x / b))
        else:
            return a * (c - (c - 1) * np.exp(-x / b))
    else:
        if plus_minus_sign == "positive":
            return a * (c - (c - 1) * np.exp((x / b) ** d))
        else:
            return a * (c - (c - 1) * np.exp(-(x / b) ** d))


def plotFunc(model, plus_minus_sign, lowerboundary, upperboundary, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    x = np.arange(lowerboundary, upperboundary, 0.01)
    y = chooseModel(x, model, plus_minus_sign, a, b, c, d)
    plt.xlim((lowerboundary - (lowerboundary / 100), upperboundary + (upperboundary / 100)))
    plt.ylim((min(y) - (min(y) / 100), max(y) + (max(y) / 100)))
    plt.xlabel("Dose")
    plt.ylabel("Effect")
    plt.plot(x, y, color='red')
    plt.show()


plotFunc("model5", "negative", 1e-1, 2500, 349.026, 1067.043, 0.76332, 2.60551)
