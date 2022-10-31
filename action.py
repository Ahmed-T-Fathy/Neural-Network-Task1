import pandas as pa
from sklearn.model_selection import train_test_split
def run(rate,f1,f2,c1,c2,epochs,bias=0):
    data = pa.read_csv("penguins.csv",usecols=['species',f1,f2])
    data=data[(data['species'] == c1) | (data['species'] == c2)]

    ##encoding and preprocessing
    label1_peng=[c1,0]
    label2_peng=[c2,1]
    data.replace([label1_peng[0],label2_peng[0]],[label1_peng[1],label2_peng[1]],True )

    if(f1=="gender" or f2=="gender"):
        data.fillna('male',inplace=True)
        label1_gen = ['male', 0]
        label2_gen = ['female', 1]
        data.replace([label1_gen[0], label2_gen[0]], [label1_gen[1], label2_gen[1]], True)


    ##class1
    c1=data[(data['species'] == label1_peng[1])]
    c1 = c1.sample(frac=1)
    c1_y = c1['species']
    c1_x=c1.drop('species',axis=1, inplace=False)
    c1_x_train,c1_x_test, c1_y_train, c1_y_test  = train_test_split(c1_x, c1_y, test_size=0.4, shuffle=True, random_state=10)


    ##class2
    c2=data[data['species'] == label2_peng[1]]
    c2 = c2.sample(frac=1)
    c2_y = c2['species']
    c2_x = c2.drop('species',axis=1, inplace=False)
    c2_x_train,c2_x_test, c2_y_train, c2_y_test = train_test_split(c2_x, c2_y, test_size=0.4, shuffle=True, random_state=10)


    ##final data
    x_train=pa.concat([c1_x_train,c2_x_train])
    y_train=pa.concat([c1_y_train,c2_y_train])
    x_test=pa.concat([c1_x_test,c2_x_test])
    y_test=pa.concat([c1_y_test,c2_y_test])






#run(0,'gender','flipper_length_mm','Chinstrap','Adelie',0,0)
