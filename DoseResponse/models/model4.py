import math

import numpy as np


# a,b,c


def partialaNegative(x, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    return math.exp(-x / b) * (c * math.exp(x / b) - c + 1)


def partialbNegative(x, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    return -(a * c - a) * x * math.exp(-x / b) / b ** 2


def partialcNegative(x, *args):
    a = args[0]
    b = args[1]
    c = args[2]
    return math.exp(-x / b) * (a * math.exp(x / b) - a)


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
                      partialcNegative(x, *args)]]).T


def informationMatrix(designPoints, *args):
    """
    :param designPoints: design points
    :param weights: weights of the design points
    :return: information matrix
    """
    weights = [1 / len(designPoints) for i in range(len(designPoints))]
    result = np.zeros((3, 3))
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
