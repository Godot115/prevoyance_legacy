import math

import numpy as np


def partiala(x, *args):
    a = args[0]
    b = args[1]
    return math.exp(x / b)


def partialb(x, *args):
    a = args[0]
    b = args[1]
    return -1 * ((a * x * math.exp(x / b)) / (b ** 2))


def vectorOfPartialDerivative(x, plus_minus_sign, *args):
    """
    :param x: value of the design point
    :return: f(x,Theta).T
    [[∂η(x,Theta) / ∂θ1],
     [∂η(x,Theta) / ∂θ2],
     ..................
     [∂η(x,Theta) / ∂θm]]
    """
    return np.array([[partiala(x, *args),
                      partialb(x, *args)]]).T


def informationMatrix(designPoints, plus_minus_sign, *args):
    """
    :param designPoints: design points
    :return:
    """
    weights = [1 / len(designPoints) for i in range(len(designPoints))]

    result = np.zeros((2, 2))
    for i in range(len(designPoints)):
        result += vectorOfPartialDerivative(designPoints[i], plus_minus_sign, *args) * \
                  vectorOfPartialDerivative(designPoints[i], plus_minus_sign, *args).T * \
                  weights[i]
    return np.array(result)


def inverseInformationMatrix(informationMatrix):
    return np.linalg.inv(informationMatrix)


def variance(x, vectorOfPartialDerivative, inverseInformationMatrix, plus_minus_sign, *args):
    left = np.matmul(vectorOfPartialDerivative(x, plus_minus_sign, *args).T, inverseInformationMatrix)
    result = np.matmul(left, vectorOfPartialDerivative(x, plus_minus_sign, *args))
    return result[0][0]
