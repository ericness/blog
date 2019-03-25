from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import standardizer
import generator

START_DATE = datetime(2018, 1, 1)
START_DATE_OFFSET = 90
END_DATE_OFFSET = 90
END_DATE_MIN_OFFSET = 60
VALUE_SCALE = 1.5
NOISE_SCALE = 0.3
NOISE_SEGMENTS = 12


data = []


for i in range(10):

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

    trace = go.Scatter(x=df.index.get_level_values('date'), y=df['value'])
    data.append(trace)


plotly.offline.init_notebook_mode(connected=True)
plotly.offline.plot(data)
