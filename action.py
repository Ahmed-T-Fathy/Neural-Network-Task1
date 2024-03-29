import pandas as pa
import numpy as np
import functions as fun
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


def run(rate, f1, f2, c1, c2, epochs, bias=0):
    data = pa.read_csv("penguins.csv", usecols=['species', f1, f2])
    data = data[(data['species'] == c1) | (data['species'] == c2)]

    ##encoding and preprocessing
    label1_peng = [c1, 1]
    label2_peng = [c2, -1]
    data.replace([label1_peng[0], label2_peng[0]], [label1_peng[1], label2_peng[1]], True)

    if (f1 == "gender" or f2 == "gender"):
        data.fillna('male', inplace=True)
        label1_gen = ['male', 0]
        label2_gen = ['female', 1]
        data.replace([label1_gen[0], label2_gen[0]], [label1_gen[1], label2_gen[1]], True)

    ##class1
    c1 = data[(data['species'] == label1_peng[1])]
    c1 = c1.sample(frac=1)
    c1_y = c1['species']
    c1_x = c1.drop('species', axis=1, inplace=False)
    c1_x_train, c1_x_test, c1_y_train, c1_y_test = train_test_split(c1_x, c1_y, test_size=0.4, shuffle=True,
                                                                    random_state=10)

    ##class2
    c2 = data[data['species'] == label2_peng[1]]
    c2 = c2.sample(frac=1)
    c2_y = c2['species']
    c2_x = c2.drop('species', axis=1, inplace=False)
    c2_x_train, c2_x_test, c2_y_train, c2_y_test = train_test_split(c2_x, c2_y, test_size=0.4, shuffle=True,random_state=10)
    ##final data
    x_train = pa.concat([c1_x_train, c2_x_train])
    y_train = pa.concat([c1_y_train, c2_y_train])
    x_test = pa.concat([c1_x_test, c2_x_test])
    y_test = pa.concat([c1_y_test, c2_y_test])

    ##plot data
    plt.figure(figsize=(8, 6))
    plt.scatter(c1_x[f1], c1_x[f2], marker='+', color='green')
    plt.scatter(c2_x[f1], c2_x[f2], marker='_', color='red')
    plt.show()
    ##model
    line = fun.gradient_descent(epochs, rate, x_train, y_train, f1, f2,bias)
    accurcy = fun.confusion_Matrix(line[0], line[1], y_test, x_test, f1, f2, label1_peng[0], label2_peng[0])
    # plot line
    min_f1 = min(data[f1])
    max_f1 = max(data[f1])
    x_values = [(min_f1 - 1), (max_f1 + 1)]
    if(bias==1):
        y_values = - (line[2]+np.multiply(line[0], x_values)) / line[1]
    else:
      y_values = - (np.multiply(line[0], x_values)) / line[1]
    plt.figure(figsize=(8, 6))
    plt.scatter(c1_x[f1], c1_x[f2], marker='+', color='green')
    plt.scatter(c2_x[f1], c2_x[f2], marker='_', color='red')

    plt.plot(x_values, y_values, label='Decision Boundary')
    plt.show()
    return accurcy
