from dask.distributed import Client, LocalCluster
import dask.dataframe as dd

cluster = LocalCluster(diagnostics_port=0, n_workers=1, processes=False)
client = Client(cluster)

df = dd.read_csv(
#    's3://nyc-tlc/trip data/yellow_tripdata*.csv',
#    storage_options={'anon': True, 'use_ssl': False}
     '/Users/ericness/github/ericness/blog/2019/01/intro_to_dask/data/yellow_tripdata*.csv'
)

print(df)

cost_distribution = (
     df[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance', 'total_amount']]
     .astype({'tpep_pickup_datetime': 'datetime64[ms]', 'tpep_dropoff_datetime': 'datetime64[ms]'})
     .assign(drive_time=lambda df: (df.tpep_dropoff_datetime - df.tpep_pickup_datetime).dt.seconds // 300)
     .drop(['tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)
     .round({'trip_distance': 0})
     .groupby(['drive_time', 'trip_distance'])
     .mean()
     .rename(columns={'total_amount': 'avg_amount'})
)



print(
     cost_distribution
     .compute()
     .reset_index()
     .pivot(
          index='trip_distance',
          columns='drive_time',
          values='avg_amount',
          fill_value=0
     )
)
