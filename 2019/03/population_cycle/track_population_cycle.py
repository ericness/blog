import numpy as np
from sklearn.datasets import make_regression
from matplotlib import pyplot

# generate regression dataset
X = np.linspace(0, 3)
y = np.sin(X)
# plot regression dataset
pyplot.scatter(X, y)

for i in range(5):
    skew = np.random.rand() / 2 + 0.5
    skew = skew if np.random.rand() > 0.5 else -skew
    y2 = np.sin(X - skew * np.sin(X)) * np.random.rand()
    pyplot.scatter(X, y2)
pyplot.show()
