from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd


def generate_time_series(
    start_date: datetime,
    start_date_offset: int,
    end_date_offset: int,
    end_date_min_offset: int,
    value_scale: float,
    noise_scale: float,
    noise_segments: int,
) -> pd.Series:
    """
    Generate a time series of values that ascends, reaches a peak and then
    descends. Noise is also included in the values.

    :param start_date:
        Date to start time series.
    :param start_date_offset:
        Maximum number of days to offset the actual start date from
        `start_date`. Actual offset will be randomly set between 0 and this
        parameter.
    :param end_date_offset:
        Maximum number of days to offset the end date from
        `start_date`. Actual offset will be randomly set between
        `end_date_min_offset` and `end_date_min_offset` plus this parameter.
    :param end_date_min_offset:
        Minimum number of days between start date and end date.
    :param value_scale:
        Amount to scale y values.
    :param noise_scale:
        Magnitude of noise in y.
    :param noise_segments:
        Number of segments to include in noise. Lower values smooth out the
        noise and higher values create more variation.
    :return:
    """
    series_start_date = start_date + timedelta(
        days=int(np.random.rand() * start_date_offset)
    )
    series_end_date = series_start_date + timedelta(
        days=int(np.random.rand() * end_date_offset) + end_date_min_offset
    )
    n_days = (series_end_date - series_start_date).days + 1
    X = np.linspace(0, np.pi, num=n_days)
    X_coarse = np.linspace(0, np.pi, num=noise_segments)

    skew = np.random.rand() / 2
    skew = skew if np.random.rand() > 0.5 else -skew
    y_skew = np.sin(X - skew * np.sin(X))
    y_magnitude = value_scale * (np.random.rand() + 0.5) * y_skew
    y_noise = (
        np.interp(
            X,
            X_coarse,
            np.random.normal(scale=noise_scale, size=noise_segments),
        )
        + y_magnitude
    )
    y = y_noise.clip(min=0)

    return pd.Series(
        data=y,
        index=pd.date_range(start=series_start_date, end=series_end_date),
        name="date",
    )
