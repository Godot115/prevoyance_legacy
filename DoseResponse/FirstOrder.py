import random
import sys
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from DoseResponse.models import model2
from DoseResponse.models import model3
from DoseResponse.models import model4
from DoseResponse.models import model5


# from models import model2
# from models import model3
# from models import model4
# from models import model5


def createInitialPoints(lowerBoundary, upperBoundary):
    initialPointsNumber = 10
    points = [random.uniform(lowerBoundary, upperBoundary) for i in range(initialPointsNumber)]
    points.sort()
    return points


def cluster(newPoint, currentPoints, designSpace):
    """
    add new point to the current points and cluster them
    :param newPoint: new point
    :param currentPoints: list of current design points
    :param designSpace: the length of design space
    """
    threshold = designSpace / 50
    for i in range(len(currentPoints)):
        if abs(newPoint - currentPoints[i]) < threshold:
            currentPoints[i] = newPoint
    currentPoints.append(newPoint)
    currentPoints.sort()
    return currentPoints


def delMinimalPoints(designPoints, threshold):
    """
    Delete points that occur less than the threshold
    :param designPoints:
    :param threshold:
    :return:
    """
    dels = []
    for i in designPoints:
        if i[1] < threshold:
            dels.append(i)
    for i in dels:
        designPoints.remove(i)
    designPoints.sort(key=lambda x: x[0])
    return designPoints


def formatResult(designPoints):
    """
    format the result into a list of tuples
    :param designPoints:
    :return:
    """
    designPoints = Counter(designPoints)
    designPoints = designPoints.items()
    numbers = 0
    for i in designPoints:
        numbers += i[1]
    result = []
    for i in designPoints:
        result.append((i[0], i[1] / numbers))
    return result


def firstOrder(designPoints, lowerBoundary, upperBoundary,
               model: str,
               maxIteration=100, grid=1000, *args):
    """
    First order alrogithm
    :param designPoints:
    :param lowerBoundary:
    :param upperBoundary:
    :param model:
    :param maxIteration:
    :param grid:
    :param args:
    :return:
    """
    designSpace = np.linspace(lowerBoundary, upperBoundary, num=grid)
    if model == "Model2":
        model = model2
    elif model == "Model4":
        model = model4
    elif model == "Model5":
        model = model5
    initialPoints = []
    for i in designPoints:
        initialPoints.append(i)
    informationMatrix = model.informationMatrix(designPoints, *args)
    invInformationMatrix = model.inverseInformationMatrix(informationMatrix)
    i = 0
    x = []
    y = []
    while i < maxIteration:
        if i < 50 and i >= 40:
            if initialPoints[0] in designPoints:
                designPoints.remove(initialPoints[0])
            initialPoints.remove(initialPoints[0])
            informationMatrix = model.informationMatrix(designPoints, *args)
            invInformationMatrix = model.inverseInformationMatrix(informationMatrix)
        i += 1
        maxVariance = sys.float_info.min
        maxVariancePoint = random.uniform(0, 1000)
        for j in range(len(designSpace)):
            dVariance = model.variance(designSpace[j], model.vectorOfPartialDerivative
                                       , invInformationMatrix, *args)
            if dVariance > maxVariance:
                maxVariance = dVariance
                maxVariancePoint = designSpace[j]
        designPoints = cluster(maxVariancePoint, designPoints, upperBoundary - lowerBoundary)
        # print(i.__repr__() + "th iratathion, Max d: ", maxVariance)
        informationMatrix = model.informationMatrix(designPoints, *args)
        invInformationMatrix = model.inverseInformationMatrix(informationMatrix)

    # plot
    for point in range(len(designSpace)):
        variance = model.variance(designSpace[point], model.vectorOfPartialDerivative
                                  , invInformationMatrix, *args)
        x.append(designSpace[point])
        y.append(variance)
    plt.plot(x, y)
    # plt.show()

    result = formatResult(designPoints)
    return result


def firstOrderModel3(designPoints, lowerBoundary, upperBoundary,
                     plus_minus_sign="positive",
                     maxIteration=100, grid=1000, *args):
    """
    first order algorithm for model 3
    :param designPoints:
    :param lowerBoundary:
    :param upperBoundary:
    :param plus_minus_sign:
    :param maxIteration:
    :param grid:
    :param args:
    :return:
    """
    designSpace = np.linspace(lowerBoundary, upperBoundary, num=grid)
    model = model3

    if plus_minus_sign != "positive":
        plus_minus_sign = "negative"
    initialPoints = []
    for i in designPoints:
        initialPoints.append(i)
    informationMatrix = model.informationMatrix(designPoints, plus_minus_sign, *args)
    invInformationMatrix = model.inverseInformationMatrix(informationMatrix)
    i = 0
    x = []
    y = []
    while i < maxIteration:
        if i < 50 and i >= 40:
            if initialPoints[0] in designPoints:
                designPoints.remove(initialPoints[0])
            initialPoints.remove(initialPoints[0])
            informationMatrix = model.informationMatrix(designPoints, plus_minus_sign, *args)
            invInformationMatrix = model.inverseInformationMatrix(informationMatrix)
        i += 1
        maxVariance = sys.float_info.min
        maxVariancePoint = random.uniform(0, 1000)
        for j in range(len(designSpace)):
            dVariance = model.variance(designSpace[j], model.vectorOfPartialDerivative
                                       , invInformationMatrix, plus_minus_sign, *args)
            if dVariance > maxVariance:
                maxVariance = dVariance
                maxVariancePoint = designSpace[j]
        designPoints = cluster(maxVariancePoint, designPoints, upperBoundary - lowerBoundary)
        # print(i.__repr__() + "th iratathion, Max d: ", maxVariance)
        informationMatrix = model.informationMatrix(designPoints, plus_minus_sign, *args)
        invInformationMatrix = model.inverseInformationMatrix(informationMatrix)

    # plot
    for point in range(len(designSpace)):
        variance = model.variance(designSpace[point], model.vectorOfPartialDerivative
                                  , invInformationMatrix, plus_minus_sign, *args)
        x.append(designSpace[point])
        y.append(variance)
    plt.plot(x, y)
    # plt.show()

    result = formatResult(designPoints)

    return result

# if __name__ == "__main__":
#     lowerBoundary = 0.000001
#     upperBoundary = 1500
#     grid = 1000
#     iterateTimes = 1000
#     plus_minus_sign = "positive"
#     model = "Model5"
#     points = createInitialPoints(lowerBoundary, upperBoundary)
#     a = 349.02687
#     b = 1067.04343
#     c = 0.76332
#     d = 2.60551
#     args = (a, b, c, d)
#     if model == "model3":
#         optimalPoints = firstOrderModel3(points, lowerBoundary, upperBoundary,
#                                          "negative",
#                                          iterateTimes, grid, *args)
#     else:
#         optimalPoints = firstOrder(points, lowerBoundary, upperBoundary,
#                                    model,
#                                    iterateTimes, grid, *args)
#     print(optimalPoints)
