import numpy as np
from sklearn.datasets import make_regression
from matplotlib import pyplot

# generate regression dataset
X = np.linspace(0, 3.1415, num=20)

for i in range(5):
    skew = np.random.rand() / 2 + 0.5
    skew = skew if np.random.rand() > 0.5 else -skew
    y = (np.sin(X - skew * np.sin(X)) * 2 * np.random.rand() + np.random.normal(scale=0.1, size=20)).clip(min=0)
    pyplot.scatter(X, y)
pyplot.show()
