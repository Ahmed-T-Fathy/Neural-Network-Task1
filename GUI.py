import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import action
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def create_label(window, txt, font, fontSize, row, column, padx=0, pady=0, sticky='w'):
    ttk.Label(window, text=txt, font=(font, fontSize)).grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)


def create_combox(window, values, width, row, column, padx, pady):
    feature = ttk.Combobox(window, width=width)
    feature['values'] = values
    feature.grid(row=row, column=column, padx=padx, pady=pady, sticky='w')
    feature.current()
    return feature


def check_features(self, event=None):
    if (feature1.get() == feature2.get()):
        messagebox.showinfo("Error!!", "choose same feature not valid")
        feature1.current(0)
        feature2.current(1)


def check_classes(self, event=None):
    if (class1.get() == class2.get()):
        messagebox.showinfo("Error!!", "choose same class not valid")
        class1.current(0)
        class2.current(1)



def bias_btn_checked():
    biasbtn = bias_btn_var.get()
    return biasbtn


def make_Classification():
    if learningRate.get() and feature1.get() and feature2.get() and class1.get() and class2.get() and epochs.get():
        accuracy = action.run(float(learningRate.get()), feature1.get(), feature2.get(), class1.get(), class2.get(),
                              int(epochs.get()),
                              bias_btn_var.get())
        accuracy_value.set(accuracy)
    else:
        messagebox.showinfo('Error !!!', 'the is missed data')
    return "accuracy"


mainWindow = tk.Tk()
mainWindow.title("Task 1 NN")
mainWindow.geometry("1100x900")

# selecting the two features
create_label(mainWindow, "Select two features:", 'Helvatical bold', 20, 0, 0, padx=20, pady=20)

features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'gender', 'body_mass_g']
# feature 1
create_label(mainWindow, "feature 1:", 'Helvatical', 15, 1, 1, padx=0, pady=0)
feature1 = create_combox(mainWindow, features, 27, 2, 1, 0, 5)
feature1.bind("<<ComboboxSelected>>", check_features)

# feature 2
create_label(mainWindow, "feature 2:", 'Helvatical', 15, 1, 3, padx=0, pady=0)
feature2 = create_combox(mainWindow, features, 27, 2, 3, 0, 5)
feature2.bind("<<ComboboxSelected>>", check_features)

# selecting the two classes
create_label(mainWindow, "Select two classes :", 'Helvatical bold', 20, 3, 0, padx=20, pady=20)

classes = ['Adelie', 'Gentoo', 'Chinstrap']

# class 1
create_label(mainWindow, "class 1:", 'Helvatical', 15, 4, 1, padx=0, pady=0)
class1 = create_combox(mainWindow, classes, 27, 5, 1, 0, 5)
class1.bind("<<ComboboxSelected>>", check_classes)

# class 2
create_label(mainWindow, "class 2:", 'Helvatical', 15, 4, 3, padx=0, pady=0)
class2 = create_combox(mainWindow, classes, 27, 5, 3, 0, 5)
class2.bind("<<ComboboxSelected>>", check_classes)

# getting the learning rate
create_label(mainWindow, "Enter learning rate:", 'Helvatical bold', 20, 6, 0, padx=20, pady=20)
learningRate = ttk.Entry(mainWindow, width=25)
learningRate.grid(row=6, column=1, padx=0, pady=0)

# getting the epochs
create_label(mainWindow, "Enter number of epochs:", 'Helvatical bold', 20, 7, 0, padx=20, pady=20)
epochs = ttk.Entry(mainWindow, width=25)
epochs.grid(row=7, column=1, padx=0, pady=0)

# check the Bias
create_label(mainWindow, "Bias:", 'Helvatical bold', 20, 8, 0, padx=20, pady=20)
bias_btn_var = tk.IntVar()
ttk.Checkbutton(mainWindow, text="Bias", variable=bias_btn_var, command=bias_btn_checked, onvalue=1,
                offvalue=0).grid(row=8, column=1)

# run classifier btn
ttk.Button(mainWindow, text="Run Classifier", width=30, command=make_Classification) \
    .grid(row=9, column=1, padx=65, pady=20)

# accuracy value txt box
create_label(mainWindow, "Accuracy :", 'Helvatical bold', 20, 10, 0, padx=20, pady=20)
accuracy_value = tk.StringVar()
accuracyEntry = ttk.Entry(mainWindow, width=25, textvariable=accuracy_value)
accuracyEntry.config(state='disabled')
accuracyEntry.grid(row=10, column=1, padx=0, pady=0, sticky='w')


mainWindow.mainloop()
