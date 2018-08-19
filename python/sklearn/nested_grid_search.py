from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import ParameterGrid, StratifiedKFold
import numpy as np

def nested_cv(X, y, inner_cv, outer_cv, Classifier, parameter_grid):
    outer_scores = []
    for training_samples, test_samples in outer_cv.split(X, y):
        best_params = {}
        best_score = -np.inf

        for parameters in parameter_grid:
            cv_scores = []

            for inner_train, inner_test in inner_cv.split(X[training_samples], y[training_samples]):
                model = Classifier(**parameters)
                model.fit(X[inner_train], y[inner_train])
                score = model.score(X[inner_test], y[inner_test])
                cv_scores.append(score)

            mean_score = np.mean(cv_scores)

            if mean_score > best_score:
                best_score = mean_score
                best_params = parameters

        model = Classifier(**best_params)
        model.fit(X[training_samples], y[training_samples])

        outer_scores.append(model.score(X[test_samples], y[test_samples]))

    return np.array(outer_scores)

param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}

iris = load_iris()
scores = nested_cv(iris.data, iris.target, StratifiedKFold(5), StratifiedKFold(5), SVC, ParameterGrid(param_grid))

print("Cross-Varidation scores:{}".format(scores))
