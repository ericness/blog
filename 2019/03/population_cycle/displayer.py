import pandas as pd
import plotly
import plotly.graph_objs as go
import typing


def graph_raw_timelines(timelines: typing.Dict[int, pd.Series]):

    traces = []

    for key, data in timelines.items():
        traces.append(
            go.Scatter(
                x=data.index,
                y=data.values,
                name=f'Customer {key}'
            )
        )

    plotly.offline.init_notebook_mode(connected=True)
    plotly.offline.plot(traces)
