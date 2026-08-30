#Implement perceptron learning model on Iris dataset

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris=load_iris()

X=iris.data
y=iris.target

mask=(y==0) | (y==1)

X=X[mask]
y=y[mask]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

learning_rate=0.01
epochs=100

weights = np.zeros(X_train.shape[1])
bias = 0

for epoch in range(epochs):

    for i in range(len(X_train)):

        z=np.dot(X_train[i], weights) + bias

        if z >= 0:
            prediction = 1
        else:
            prediction = 0

        error=y_train[i]-prediction

        weights=weights+learning_rate*error*X_train[i]

        bias=bias+learning_rate*error

y_pred = []

for i in range(len(X_test)):

    z=np.dot(X_test[i], weights)+bias

    if z >= 0:
        prediction=1
    else:
        prediction=0

    y_pred.append(prediction)

accuracy=accuracy_score(y_test, y_pred)

print("Final Weights:", weights)
print("Final Bias:", bias)
print("Predictions:", y_pred)
print("Actual:", y_test)
print("Accuracy:", accuracy * 100, "%")