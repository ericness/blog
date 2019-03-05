import pandas as pd

df = pd.DataFrame(
    data=1,
    index=pd.RangeIndex(5, name='row_name'),
    columns=pd.Index(data=['a', 'b'], name='col_name')
)

print(df.to_string())
print()
print(f'Row Index Name: {df.index.name}')
print(f'Column Index Name: {df.columns.name}')
