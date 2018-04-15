import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

plt.style.use('ggplot')

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data['data'], data['target'], random_state=0)

activation_type = ["relu", "tanh"]
alpha = [0.001, 0.01, 0.1, 1]
fig, axes = plt.subplots(2, 4, figsize=(20, 8))

for axx, ac in zip(axes, activation_type):
    for ax, al in zip(axx, alpha):
        model = MLPClassifier(solver="lbfgs", random_state=0, hidden_layer_sizes=[10], activation=ac, alpha=al)
        model.fit(X_train, y_train)
        ax.scatter(X_test[:,0], X_test[:,1], c=y_test, alpha=0.6)
        ax.set_title("ac_type:{0} alpha:{1}\nscore{2}".format(ac, str(al), str(model.score(X_test,y_test))))

plt.pause(20)
