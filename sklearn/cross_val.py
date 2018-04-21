import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
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

# cross_val_score
cvs = [3, 4, 5, 6]

# 活性化関数reluとtanhを比較するためのリスト。
activation_type = ["relu", "tanh"]

# alpha値を比較するためのリスト。
alpha = [0.001, 0.01, 0.1, 1]

# 4種類のCV値で公差集計
# (2通りの活性化関数 * 4通りのalpha値) = 8通りの結果を描画して出力。
for ac in activation_type:
    for al in alpha:
        for cv in cvs:
            model = MLPClassifier(solver="lbfgs", random_state=0, hidden_layer_sizes=[10], activation=ac, alpha=al)
            score = cross_val_score(model, X, y, cv=cv)
            print("Activation:{}\nalpha:{}\ncv:{}\nscore:{:.3f}\n".format(ac, al, cv, score.mean()))
