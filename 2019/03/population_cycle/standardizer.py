import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def standardize_timeline(time_series: pd.Series) -> pd.Series:
    """
    Replace datetime index with a standardized timeline on the interval 0 to 1.

    :param time_series:
        Series of values to standardize index of. Index must be DateTime type.
    :return:
        Series with the same values and the datetime index replaced with floats
        between 0 and 1.
    """
    datetime_index = time_series.index.tolist()
    epoch_index = np.array([t.timestamp() for t in datetime_index])
    standardized_index = MinMaxScaler().fit_transform(
        epoch_index.reshape(-1, 1)
    )
    return time_series.set_axis(standardized_index[:, 0], inplace=False)
