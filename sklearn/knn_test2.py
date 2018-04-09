from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=1250, n_features=4, n_informative=2, n_redundant=2, random_state=0)
X_train, X_test, y_train, y_test = tts(X, y, random_state=0)

k_list = range(1, 11)
train_accuracy = []
test_accuracy = []

for k in k_list:
    model = knn(n_neighbors=k)
    model.fit(X_train, y_train)
    train_accuracy.append(model.score(X_train, y_train))
    test_accuracy.append(model.score(X_test, y_test))

plt.plot(k_list, train_accuracy, label="train")
plt.plot(k_list, test_accuracy, label="test")
plt.xlabel("n_neighbor")
plt.ylabel("accuracy")
plt.title("KNN Test by Iris Data")
plt.show()
