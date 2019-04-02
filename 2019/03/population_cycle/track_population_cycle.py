from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import displayer
import interpolator
import standardizer
import generator

START_DATE = datetime(2018, 1, 1)
START_DATE_OFFSET = 90
END_DATE_OFFSET = 90
END_DATE_MIN_OFFSET = 60
VALUE_SCALE = 1.5
NOISE_SCALE = 0.3
NOISE_SEGMENTS = 12

INTERPOLATION_POINTS = 20

POPULATION_COUNT = 20

if __name__ == '__main__':

    customer_activity = {}
    for customer_id in range(POPULATION_COUNT):

        customer_activity[customer_id] = generator.generate_time_series(
            start_date=START_DATE,
            start_date_offset=START_DATE_OFFSET,
            end_date_offset=END_DATE_OFFSET,
            end_date_min_offset=END_DATE_MIN_OFFSET,
            value_scale=VALUE_SCALE,
            noise_scale=NOISE_SCALE,
            noise_segments=NOISE_SEGMENTS
        )

    displayer.graph_raw_timelines(customer_activity)

    customer_activity_std = {
        customer_id: standardizer.standardize_timeline(activity)
        for customer_id, activity in customer_activity.items()
    }

    #trace = go.Scatter(x=df_std.index, y=df_std['value'], name="activity")
    #data.append(trace)

    customer_activity_int = {
        customer_id: interpolator.interpolate_time_series(
            activity, n_points=INTERPOLATION_POINTS
        )
        for customer_id, activity in customer_activity_std.items()
    }
    #print(df_int.head())

    customer_activity_df = pd.DataFrame(customer_activity_int).T

    print(customer_activity_df.head())

    interpolated_percentiles = (
        customer_activity_df
            .quantile(q=[0.25, 0.5, 0.75], axis=0)
    )

    print(interpolated_percentiles)

    # data = []
    #
    # for customer_id, activity in customer_activity_std.items():
    #
    #     trace = go.Scatter(
    #         x=activity.index, y=activity.values, name=str(customer_id)
    #     )
    #     data.append(trace)
    #
    # plotly.offline.init_notebook_mode(connected=True)
    # plotly.offline.plot(data)

    data = []

    for pct in [0.25, 0.50, 0.75]:
        trace = go.Scatter(
            x=interpolated_percentiles.columns,
            y=interpolated_percentiles.loc[pct],
            name=str(pct)
        )
        data.append(trace)

