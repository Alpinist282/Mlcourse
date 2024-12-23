import pandas as pd
class MyLineReg:
    def __init__(self, n_iter=100, learning_rate=0.1, weights = None):
        self.n_iter = n_iter
        self.learning_rate = learning_rate
        self.weights = weights

    def fit(self, X, y, verbose = False):
        X
        return None
        #unit_column = [1, 1, 1]
    def __str__(self):
        return f"MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}"

# X = pd.DataFrame({"B":[1, 2, 3]})
# y = pd.Series()
# unit_column = [1, 1, 1]
# X.insert(loc=0, column="A", value=unit_column)