import random
from matplotlib import pyplot as plt
import seaborn as sys
import numpy as np
def gradient_descent(epochs, rate, x_train, y_train, f1, f2, bias):
    n = float(len(x_train))
    w1 = random.random()
    w2 = random.random()
    if (bias == 1):
        biass = random.random()
    for i in range(epochs):
        predct_matrix = w1 * x_train[f1] + w2 * x_train[f2]
        y_pred = signum(predct_matrix)  # The current predicted value of Y
        D_w1 = (-2 / n) * sum((y_train - y_pred) * x_train[f1])  # Derivative wrt w1
        D_w2 = (-2 / n) * sum((y_train - y_pred) * x_train[f2])  # Derivative wrt w2
        if (bias == 1):
            D_bias = (-2 / n) * sum((y_train - y_pred))

        w1 = w1 - rate * D_w1  # Update w1
        w2 = w2 - rate * D_w2  # Update w2
        if (bias == 1):
            biass = biass - rate * D_bias

    if (bias == 1):
        return w1, w2, bias
    else:
        return w1, w2




def signum(input):
    input = np.array(input)
    n = len(input)
    for i in range(n):
        if (input[i] >= 0):
            input[i] = 1
        else:
            input[i] = -1

    return input

def confusion_Matrix(w1, w2, y_test, x_test, f1, f2, c1, c2):
    y_predicte = signum(w1 * x_test[f1] + w2 * x_test[f2])
    y_actual = y_test.to_numpy()
    TP = TN = FP = FN = P = N = 0
    for i in range(len(y_actual)):
        if (y_actual[i] == 1) and (y_predicte[i] == 1):
            TP += 1
            P += 1
        if (y_actual[i] == 1) and (y_predicte[i] == -1):
            FN += 1
            N += 1
        if (y_actual[i] == -1) and (y_predicte[i] == 1):
            FP += 1
            P += 1
        if (y_actual[i] == -1) and (y_predicte[i] == -1):
            TN += 1
            N += 1
    accuracy = (TP + TN) / (P + N)
    matrix = np.array([[TP, FN], [FP, TN]])
    x = [c1, c2]
    y = [c1, c2]
    plt.figure(figsize=(8, 6))
    x = sys.heatmap(matrix, xticklabels=x, yticklabels=y, annot=True)
    plt.show()


    return accuracy
