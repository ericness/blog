import pandas as pd
from dask import dataframe as dd

BUCKET = 'my-bucket'
FILE_KEY = 'test-*.json'
KMS_KEY_ID = 'my-key-id'

df = dd.from_pandas(
    pd.DataFrame(
        data={
            'a': range(1000),
            'b': range(1000)
        }
    ),
    npartitions=4
)

filename = f's3://{BUCKET}/{FILE_KEY}'

df.to_json(
    filename=filename,
    storage_options={
        's3_additional_kwargs': {
            'ServerSideEncryption': 'aws:kms',
            'SSEKMSKeyId': KMS_KEY_ID
        }
    }
)
