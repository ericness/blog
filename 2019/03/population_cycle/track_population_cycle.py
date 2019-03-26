from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

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

INTERPOLATION_POINTS = 40

data = []


for i in range(1):

    df = generator.generate_time_series(
        series_id=i,
        start_date=START_DATE,
        start_date_offset=START_DATE_OFFSET,
        end_date_offset=END_DATE_OFFSET,
        end_date_min_offset=END_DATE_MIN_OFFSET,
        value_scale=VALUE_SCALE,
        noise_scale=NOISE_SCALE,
        noise_segments=NOISE_SEGMENTS
    )

    print(df.info())

    #trace = go.Scatter(x=df.index.get_level_values('date'), y=df['value'])
    #data.append(trace)

    df_std = standardizer.standardize_timeline(df.droplevel('id'))

    trace = go.Scatter(x=df_std.index, y=df_std['value'])
    data.append(trace)

    df_int = interpolator.interpolate_time_series(df_std['value'], n_points=INTERPOLATION_POINTS)

    print(df_int.head())

    trace = go.Scatter(x=df_int.index, y=df_int.values)
    data.append(trace)

plotly.offline.init_notebook_mode(connected=True)
plotly.offline.plot(data)
