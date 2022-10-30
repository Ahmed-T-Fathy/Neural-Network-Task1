import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def create_label(window,txt,font,fontSize,row,column,padx=0,pady=0):
    ttk.Label(window, text=txt, font=(font, fontSize)).grid(row=row,column=column,padx=padx,pady=pady)
def create_combox(window,values,width,row,column,padx,pady):
    feature = ttk.Combobox(window, width=width)
    feature['values'] = values
    feature.grid(row=row, column=column, padx=padx, pady=pady)
    feature.current()
    return feature
def check_features(self, event=None):
    if(feature1.get()==feature2.get()):
        messagebox.showinfo("Error!!","choose same feature not valid")
        feature1.current(0)
        feature2.current(1)

def check_classes(self, event=None):
    if(class1.get()==class2.get()):
        messagebox.showinfo("Error!!","choose same class not valid")
        class1.current(0)
        class2.current(1)

mainWindow=tk.Tk()
mainWindow.title("Task 1 NN")
mainWindow.geometry("1100x900")


create_label(mainWindow,"Select two features:",'Helvatical bold',20,0,0,padx=20,pady=20)

create_label(mainWindow,"feature 1:",'Helvatical',15,1,0,padx=0,pady=0)

features=['bill_length_mm','bill_depth_mm','flipper_length_mm','gender','body_mass_g']

feature1=create_combox(mainWindow,features,27,1,1,0,0)
feature1.bind("<<ComboboxSelected>>",check_features)

create_label(mainWindow,"feature 2:",'Helvatical',15,1,3,padx=20,pady=0)

feature2=create_combox(mainWindow,features,27,1,4,0,0)
feature2.bind("<<ComboboxSelected>>",check_features)

create_label(mainWindow,"Select two classes :",'Helvatical bold',20,2,0,padx=20,pady=20)

create_label(mainWindow,"class 1:",'Helvatical',15,3,0,padx=0,pady=0)
classes=['Adelie','Gentoo','Chinstrap']

class1=create_combox(mainWindow,classes,27,3,1,0,0)
class1.bind("<<ComboboxSelected>>",check_classes)

create_label(mainWindow,"class 2:",'Helvatical',15,3,3,padx=20,pady=0)

class2=create_combox(mainWindow,classes,27,3,4,0,0)
class2.bind("<<ComboboxSelected>>",check_classes)


create_label(mainWindow,"Enter learning rate:",'Helvatical bold',20,4,0,padx=20,pady=20)
learningRate=ttk.Entry(mainWindow,width=25).grid(row=4,column=1,padx=0,pady=0)

create_label(mainWindow,"Enter number of epochs:",'Helvatical bold',20,5,0,padx=20,pady=20)
epochs=ttk.Entry(mainWindow,width=25).grid(row=5,column=1,padx=0,pady=0)

create_label(mainWindow,"Bias:",'Helvatical bold',20,6,0,padx=20,pady=20)
biasbtn=''
bias_btn_var= tk.StringVar()
def bias_btn_checked():
    biasbtn=bias_btn_var.get()
    print(biasbtn)

ttk.Checkbutton(mainWindow, text="Bias", variable=bias_btn_var,command=bias_btn_checked,onvalue='checked',offvalue='not checked').grid(row=6,column=1)


mainWindow.mainloop()















#def hellocallback():
#     msg=messagebox.showinfo("tarek message",monthchoosen.get())
# B=ttk.Button(mainWindow,text="say hello",width=10,command=hellocallback)
# B.grid(row=1,column=2)
# print(monthchoosen.get())