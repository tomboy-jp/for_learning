from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

test_data = load_iris()

train_X, test_X, train_y, test_y = train_test_split(test_data.data, test_data.target, random_state=0)

models = {}

models["Liner"] = LinearRegression()
models["Lasso"] = Lasso()
models["Ridge"] = Ridge()
models["ElNet"] = ElasticNet()

for label, model in models.items():
    model.fit(train_X, train_y)
    score = model.score(test_X, test_y)
    print("{}:\t{: 0.5f}".format(label, score))
