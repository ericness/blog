import pandas as pd

df = pd.DataFrame(
    data={
        'a': range(5),
        'b': range(5)
    }
)

print(df.to_string())
print()
print(f'Row Index Name: {df.index.name}')
print(f'Column Index Name: {df.columns.name}')
