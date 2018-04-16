import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# matplotlibのスタイルを指定。
plt.style.use('ggplot')

# irisデータの読み込み。
data = load_iris()
# 特徴とラベルを格納。
X, y = data['data'], data['target']

# スケール変換 試したら精度が下がったので今回は未使用
# ss = StandardScaler()
# X = ss.fit_transform(X)

# pcaを使って主成分分析。特徴量を二次元に落とし込む。
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 特徴データを3:1に分割し、訓練データ、試験データとして格納。
X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.25, random_state=0)

# 活性化関数reluとtanhを比較するためのリスト。
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
        ax.scatter(X_test[:,0], X_test[:,1], c=model.predict(X_test), alpha=0.6)
        ax.set_title("ac_type:{}, alpha:{}, score:{:.3f}".format(ac, str(al), model.score(X_test,y_test)))

plt.pause(20)
