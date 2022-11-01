import numpy as np
import random

def gradient_descent(epochs, rate, x_train, y_train, f1, f2):
    n = float(len(x_train))
    w1 = random.random()
    w2 = random.random()
    for i in range(epochs):
        predct_matrix = w1 * x_train[f1] + w2 * x_train[f2]
        y_pred = signum(predct_matrix)  # The current predicted value of Y
        D_w1 = (-2/n) *sum((y_train - y_pred) * x_train[f1])  # Derivative wrt w1
        D_w2 =(-2/n) * sum((y_train - y_pred) * x_train[f2])  # Derivative wrt w2
        w1 = w1 - rate * D_w1  # Update w1
        w2 = w2 - rate * D_w2  # Update w2
    return w1,w2


def signum(input):
    input=np.array(input)
    n = len(input)
    for i in range(n):
        if (input[i] >= 0):
           input[i] = 1
        else:
            input[i] = -1


    return input
