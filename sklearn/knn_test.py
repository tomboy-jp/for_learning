import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

k_list = range(1, 11)
accuracy = []

for k in k_list:
    model = KNeighborsClassifier(n_neighbors=int(k))
    model.fit(X_train, y_train)
    accuracy.append(model.score(X_test, y_test))

plt.plot(k_list, accuracy)
plt.xlabel("n_neighbor")
plt.ylabel("accuracy")
plt.title("KNN Test by Iris Data")
plt.show()
