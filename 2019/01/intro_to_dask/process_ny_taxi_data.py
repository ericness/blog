import numpy as np
import pandas as pd
from dask.distributed import Client
import dask.dataframe as dd
import math


def roundup(x, base: int = 5):
    """Round `x` up to nearest `base`"""
    return int(math.ceil(x / float(base))) * base


def round_series_up(s: dd.Series) -> dd.Series:
    """Apply roundup function to all elements of `s`"""
    return s.apply(roundup, meta=pd.Series(data=[], dtype=np.float32))


def transform_dask_dataframe(df: dd.DataFrame) -> dd.DataFrame:
    """Process NYC taxi data"""
    return (
        df[[
            'tpep_pickup_datetime', 'tpep_dropoff_datetime',
            'trip_distance', 'total_amount'
        ]]
        .astype({
            'tpep_pickup_datetime': 'datetime64[ms]',
            'tpep_dropoff_datetime': 'datetime64[ms]'
        })
        .assign(drive_time=(lambda df: (
            df.tpep_dropoff_datetime - df.tpep_pickup_datetime).dt.seconds
            // 300))
        .assign(drive_time=lambda df: round_series_up(df.drive_time))
        .assign(trip_distance=lambda df: round_series_up(df.trip_distance))
        .query('drive_time <= 120 & trip_distance <= 50')
        .drop(['tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)
        .round({'trip_distance': 0})
        .groupby(['drive_time', 'trip_distance'])
        .mean()
        .rename(columns={'total_amount': 'avg_amount'})
    )


def compute_final_dataframe(df: dd.DataFrame) -> pd.DataFrame:
    """Execute dask task graph and compute final results"""
    return (
        df
        .compute()
        .reset_index()
        .pivot(
             index='drive_time',
             columns='trip_distance',
             values='avg_amount'
        )
        .fillna(0)
    )


if __name__ == "__main__":
    client = Client()

    taxi_data = dd.read_csv(
        's3://nyc-tlc/trip data/yellow_tripdata_2018-04.csv',
        storage_options={'anon': True, 'use_ssl': False}
    )

    transformed_data = transform_dask_dataframe(taxi_data)
    fare_distribution = compute_final_dataframe(transformed_data)

    print(fare_distribution.to_string())
