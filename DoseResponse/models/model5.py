import math

import numpy as np


# a[c-(c-1)exp(-(x/b)^d)]
# a = args[0]
# b = args[1]
# c = args[2]
# d = args[3]


def partialaNegative(x, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]

    return math.exp(-((x / b) ** d)) * (c * math.exp((x / b) ** d) - c + 1)


def partialbNegative(x, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    return -b ** (-d - 1) * (a * c - a) * d * x ** d * math.exp(-((x / b) ** d))


def partialcNegative(x, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    return math.exp(-((x / b) ** d)) * (a * math.exp((x / b) ** d) - a)


def partialdNegative(x, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    return math.exp(-((x / b) ** d)) * (
            (a * c - a) * x ** d * math.log(x) + (a * math.log(b) - a * math.log(b) * c) * x ** d) / b ** d


def vectorOfPartialDerivative(x, *args):
    """
    :param x: value of the design point
    :return: f(x,Theta).T
    [[∂η(x,Theta) / ∂θ1],
     [∂η(x,Theta) / ∂θ2],
     ..................
     [∂η(x,Theta) / ∂θm]]
    """
    return np.array([[partialaNegative(x, *args),
                      partialbNegative(x, *args),
                      partialcNegative(x, *args),
                      partialdNegative(x, *args)]]).T


def informationMatrix(designPoints, *args):
    """
    :param designPoints: design points
    :return: information matrix
    """
    weights = [1 / len(designPoints) for i in range(len(designPoints))]
    result = np.zeros((4, 4))
    for i in range(len(designPoints)):
        result += vectorOfPartialDerivative(designPoints[i], *args) * \
                  vectorOfPartialDerivative(designPoints[i], *args).T * \
                  weights[i]
    return np.array(result)


def inverseInformationMatrix(informationMatrix):
    return np.linalg.inv(informationMatrix)


def variance(x, vectorOfPartialDerivative, inverseInformationMatrix, *args):
    left = np.matmul(vectorOfPartialDerivative(x, *args).T, inverseInformationMatrix)
    result = np.matmul(left, vectorOfPartialDerivative(x, *args))
    return result[0][0]
