# y = a exp(x/b) a>0
import time
import matplotlib.pyplot as plt
import numpy as np
import base64

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
        return a * (c - (c - 1) * np.exp(-x / b))
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
    path = "./templates/"+int(time.time()).__repr__()+".png"
    plt.savefig(path)
    return path

def imgToBase64(path):
    with open(path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)  # base64编码
        return str(base64_data, 'utf-8')
# plotFunc("model5", "negative", 1e-1, 2500, 349.026, 1067.043, 0.76332, 2.60551)
