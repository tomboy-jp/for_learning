from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# matplotlibのスタイルを指定。
plt.style.use('ggplot')

# irisデータの読み込み。
data = load_iris()
# 特徴とラベルを格納。
X, y = data['data'], data['target']

# スケール変換
ss = StandardScaler()
X = ss.fit_transform(X)

# よしなに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0)

# GridSearch用の辞書を作成
param_grid = {"activation":["relu", "tanh"], "alpha":[0.001, 0.01, 0.1, 1], "hidden_layer_sizes":[[10],[30,10],[10,30,10]]}

# モデルを内包したGridSearchのインスタンスを生成。
model_gs = GridSearchCV(MLPClassifier(), param_grid, cv=5)
model_gs.fit(X_train, y_train)

# 結果を出力
print("Test Score is {:.3f}".format(model_gs.score(X_test, y_test)))
print("Best Param is {}".format(model_gs.best_params_))
print("Best Cross Validation Score is {:.3f}".format(model_gs.best_score_))
