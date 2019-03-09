import pandas as pd


def display_dataframe(df: pd.DataFrame):
    """Displays a `pandas.DataFrame` with index names"""
    print(
        f'{df.to_string()}\n\n'
        f'Row Index Name: {df.index.name}\n'
        f'Column Index Name: {df.columns.name}\n'
    )


df_simple = pd.DataFrame(
    data={
        'a': range(5),
        'b': range(5)
    }
)

display_dataframe(df_simple)

df_named = pd.DataFrame(
    data=[[i, i] for i in range(5)],
    index=pd.RangeIndex(5, name='row_name'),
    columns=pd.Index(data=['a', 'b'], name='col_name')
)

display_dataframe(df_named)

df_to_pivot = pd.DataFrame(
    data={
        'customer': [10, 11, 10, 11, 12, 12],
        'product': ['phone', 'phone', 'tv', 'laptop', 'tv', 'phone'],
        'amount': [5.0, 10.0, 7.0, 12.0, 3.0, 9.0]
    }
)

display_dataframe(df_to_pivot)

df_pivoted = (
    df_to_pivot
    .pivot(index='customer', columns='product', values='amount')
    .fillna(0)
)

display_dataframe(df_pivoted)

df_renamed = (
    df_pivoted
    .rename_axis(index='account')
    .rename_axis(columns='device')
)

display_dataframe(df_renamed)

df_renamed_none = (
    df_pivoted
    .rename_axis(index=None)
    .rename_axis(columns=None)
)

display_dataframe(df_renamed_none)

