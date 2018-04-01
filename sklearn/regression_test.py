import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

test_data = load_iris()

train_X, test_X, train_y, test_y = train_test_split(test_data.data, test_data.target, random_state=0)

model = LinearRegression()
model.fit(train_X, train_y)

score = model.score(test_X, test_y)
print(score)
