import pandas as pd
import plotly
import plotly.graph_objs as go
import typing


def graph_timelines(timelines: typing.Dict[int, pd.Series]):
    """
    Display each time series in a dict as a trace on a line graph.

    :param timelines:
        Dict of time line Series.
    """
    traces = []

    for key, data in timelines.items():
        traces.append(
            go.Scatter(x=data.index, y=data.values, name=f"Customer {key}")
        )

    plotly.offline.init_notebook_mode(connected=True)
    plotly.offline.plot(traces)


def graph_quantiles(quantiles: pd.DataFrame):
    """
    Display each quantile as a trace on a line graph.

    :param quantiles:
        DataFrame with a row for each quantile and each column as a point along
        the time line.
    """
    traces = []

    for pct in quantiles.index:
        trace = go.Scatter(
            x=quantiles.columns,
            y=quantiles.loc[pct],
            name=str(pct)
        )
        traces.append(trace)

    plotly.offline.init_notebook_mode(connected=True)
    plotly.offline.plot(traces)
