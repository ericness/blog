import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline


def interpolate_time_series(time_series: pd.Series, n_points: int) -> pd.Series:
    """
    Interpolate the pattern in the standardized time series data into `n_points`
    number of values at equal intervals between 0 and 1.

    :param time_series:
        Time series data to model interpolated points on. The time series must
        be standardized to have index values between 0 and 1.
    :param n_points:
        Number of points to interpolate for.
    :return:
        Series with index `n_points` values between 0 and 1 and the values set
        as the interpolated values.
    """
    spline = CubicSpline(time_series.index, time_series.values)

    interpolation_points = np.linspace(0, 1, n_points).round(5)

    return pd.Series(
        data=spline(interpolation_points),
        index=interpolation_points
    )
