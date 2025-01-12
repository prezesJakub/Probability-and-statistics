import pandas
from sklearn.model_selection import train_test_split


def load_mushroom_data():
    data = pandas.read_csv("data/mushrooms.csv")
    return data


def load_iris_data():
    from sklearn.datasets import load_iris
    iris = load_iris()
    data = pandas.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    data['target'] = data['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    return data


def split_data(data, target_column, test_size=0.3):
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    return X_train, X_test, y_train, y_test
