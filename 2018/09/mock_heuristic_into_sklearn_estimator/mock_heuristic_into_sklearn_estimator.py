import numpy as np

from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


class MockBinaryClassifier(BaseEstimator):
    """Class to emulate a predictive model using a simple heuristic."""

    def __init__(self):
        """Set the classes for binary classification"""
        self.n_classes_ = 2
        self.classes_ = np.array([0, 1])

    def fit(
        self,
        features: np.ndarray,
        target: np.ndarray,
        sample_weight: np.ndarray = None
    ):
        """
        Mocks out the fit function for a standard scikit-learn estimator. Since
        the heuristic doesn't rely on any previous data, the function simply
        returns self.

        :param features:
            Ignored.
        :param target:
            Ignored.
        :param sample_weight:
            Ignored.
        :return:
            Returns the estimator without any changes.
        """
        return self

    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Emulate a machine learning model's behavior. This function will return
        the most probable class for each instance.

        Only looks at first feature.

        If features less than or equal to 0 at a
        given index, it will return a class 0. If features
        is greater than zero at a given index, it will return a class 1.

        :param features:
            Ndarray that corresponds to features used in a classification model.
        :return:
            Predicted probabilities for all classes for all instances of
            features.
        """

        return np.where(features[:, 0] > 0, 1, 0)


model = MockBinaryClassifier()

test_feature = np.array([[0], [0.5], [3], [-1]])

predictions = model.predict(test_feature)

print(predictions)


train_feature = np.zeros_like(test_feature)
train_target = np.zeros_like(test_feature)

pipe = Pipeline([
    ('scale', MinMaxScaler(feature_range=(0, 1))),
    ('mock', MockBinaryClassifier())
])

pipe_predictions = pipe.fit(train_feature, train_target).predict(test_feature)

print(pipe_predictions)
