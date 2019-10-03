import numpy as np
import pandas as pd
import random

print("hw0")
#filename = 'arrhythmia.data'
filename = 'test.txt'

def import_data(file):
    X = []
    y = []
    with open(file, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.replace('\n','');      
            tmp = [np.nan if e=='?' else int(e) for e in line.split(',')]
            dimension = len(tmp)
            X.append(tmp[0:dimension-2])
            y.append(tmp[dimension-1])
    return X , y

def discard_missing( X , y ):
    for xx,yy in zip(reversed(X),reversed(y)):
        for j in range(len(xx)):
            if xx[j] is np.nan:
                X.remove(xx)
                y.remove(yy)
                break
    print(X)
    print(y)
    return X , y

def impute_missing( X ):
    print("%%%%%%%%%%%%%%%%%")
    data = pd.DataFrame(X)
    print(data)
    x=[]
    x=data.fillna(data.median())
    print(x)

def train_test_split(X,y,t_f):
    rs = []
    rs = random.sample(range(len(X)),t_f)
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    rs.sort(reverse=True)
    for i in rs:
        X_train.append(X[i])
        y_train.append(y[i])
        X.remove(X[i])
        y.remove(y[i])
    X_test = X
    y_test = y
    print("X_train***********")
    print(X_train)
    print("y_train***********")
    print(y_train)
    print("X_test***********")
    print(X_test)
    print("y_test***********")
    print(y_test)


X = []
y = []
X,y = import_data(filename)
print(X)
print(y)
#X,y=discard_missing(X,y)
#impute_missing(X)
train_test_split(X,y,2)
