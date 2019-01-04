from dask.distributed import Client, LocalCluster
import dask.dataframe as dd

cluster = LocalCluster(diagnostics_port=0, n_workers=1, processes=False)
client = Client(cluster)

df = dd.read_csv(
    's3://nyc-tlc/trip data/yellow_tripdata_2018-01.csv',
    storage_options={'anon': True, 'use_ssl': False}
)

print(df.head())
