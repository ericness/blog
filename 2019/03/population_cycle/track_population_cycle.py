from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

data = []

for i in range(10):
    start_date = datetime(2018, 1, 1) + timedelta(days=int(np.random.rand() * 90))
    end_date = start_date + timedelta(days=int(np.random.rand() * 90) + 60)

    n_days = (end_date - start_date).days + 1
    X = np.linspace(0, 3.1415, num=n_days)
    X_coarse = np.linspace(0, 3.1415, num=12)

    skew = np.random.rand() / 2
    skew = skew if np.random.rand() > 0.5 else -skew
    y_skew = np.sin(X - skew * np.sin(X))
    y_magnitude = 1.5 * (np.random.rand() + 0.5) * y_skew
    y_noise = np.interp(X, X_coarse, np.random.normal(scale=0.3, size=12)) + y_magnitude
    y = y_noise.clip(min=0)

    df = pd.DataFrame(
        data={'value': y},
        index=pd.MultiIndex.from_product(
            [pd.date_range(start=start_date, end=end_date), [i]],
            names=['date', 'customer']
        )
    )

    trace = go.Scatter(x=df.index.get_level_values('date'), y=df['value'])
    data.append(trace)


plotly.offline.init_notebook_mode(connected=True)
plotly.offline.plot(data)
