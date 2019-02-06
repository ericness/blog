import numpy as np
import pandas as pd
from dask.distributed import Client, LocalCluster
import dask.dataframe as dd
import math


def roundup(x, base: int = 5):
    return int(math.ceil(x / float(base))) * base


if __name__ == "__main__":
    cluster = LocalCluster(diagnostics_port=0) #, processes=False)
    client = Client(cluster)

    df = dd.read_csv(
        #    's3://nyc-tlc/trip data/yellow_tripdata*.csv',
        #    storage_options={'anon': True, 'use_ssl': False}
        #     '/Users/ericness/github/ericness/blog/2019/01/intro_to_dask/data/yellow_tripdata*.csv'
        '/Users/ericness/github/ericness/blog/2019/01/intro_to_dask/data/yellow_tripdata_2018-04.csv'
    )

    cost_distribution = (
        df[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance', 'total_amount']]
            # .astype({'tpep_pickup_datetime': 'datetime64[ms]', 'tpep_dropoff_datetime': 'datetime64[ms]'})
            # .assign(drive_time=lambda df:(df.tpep_dropoff_datetime - df.tpep_pickup_datetime).dt.seconds // 300)
            # .assign(drive_time=lambda df: df.drive_time.apply(roundup, meta=pd.Series(data=[], dtype=np.float32)))
            # .assign(trip_distance=lambda df: df.trip_distance.apply(roundup, meta=pd.Series(data=[], dtype=np.float32)))
            # .query('drive_time <= 120 & trip_distance <= 50')
            # .drop(['tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)
            .round({'trip_distance': 0})
            # .groupby(['drive_time', 'trip_distance'])
            # .mean()
            # .rename(columns={'total_amount': 'avg_amount'})
    #         .compute()
    #         .reset_index()
    #         .pivot(
    #              index='drive_time',
    #              columns='trip_distance',
    #              values='avg_amount'
    #         )
    #         .fillna(0)
    )

    cost_distribution.visualize('execution_graph.svg')

    print(cost_distribution.to_string())
