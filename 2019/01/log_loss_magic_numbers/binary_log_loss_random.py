from sklearn.metrics import log_loss

actual = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
predictions = [
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
]

print(log_loss(actual, predictions))
