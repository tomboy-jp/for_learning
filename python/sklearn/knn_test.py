from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# サンプルデータを作成。
X, y = make_classification(n_samples=1250, n_features=4, n_informative=2, n_redundant=2, random_state=0)
# よしなに分割。
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# for文を回す準備。
k_list = range(1, 11)
train_accuracy = []
test_accuracy = []

# k近傍法の参照とするデータの数を変化させ、1個から10個までのスコアを抽出。
for k in k_list:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    train_accuracy.append(model.score(X_train, y_train))
    test_accuracy.append(model.score(X_test, y_test))

# 訓練データと試験データの違いをグラフに描画
plt.plot(k_list, train_accuracy, label="train")
plt.plot(k_list, test_accuracy, label="test")
plt.xlabel("n_neighbor")
plt.ylabel("accuracy")
plt.title("KNN Test by Iris Data")
plt.legend()
plt.pause(10)
