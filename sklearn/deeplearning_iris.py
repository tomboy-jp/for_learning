import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

# matplotlibのスタイルを指定。
plt.style.use('ggplot')

# irisデータの読み込み。
data = load_iris()
# 特徴とラベルを格納。
X, y = data['data'], data['target']
# 標準化のコード。精度が悪化したため、今回は未使用。
# X = (X - X.mean(axis=0)) / X.std(axis=0)

# pcaを使って主成分分析。特徴を二次元に落とし込む。
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# トレインデータとテストデータを4:1に分割。
X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.25, random_state=0)

# relu関数とtanh関数を比較するためのリスト。
activation_type = ["relu", "tanh"]
# alpha値を比較するためのリスト。
alpha = [0.001, 0.01, 0.1, 1]
# 画像サイズの指定と分割。
fig, axes = plt.subplots(2, 4, figsize=(20, 8))

# (2通りの活性化関数 * 4通りのalpha値) = 8通りの結果を描画して出力。
for axx, ac in zip(axes, activation_type):
    for ax, al in zip(axx, alpha):
        model = MLPClassifier(solver="lbfgs", random_state=0, hidden_layer_sizes=[10], activation=ac, alpha=al)
        model.fit(X_train, y_train)
        ax.scatter(X_test[:,0], X_test[:,1], c=y_test, alpha=0.6)
        ax.set_title("ac_type:{}, alpha:{}, score:{:.3f}".format(ac, str(al), model.score(X_test,y_test)))

plt.pause(20)
