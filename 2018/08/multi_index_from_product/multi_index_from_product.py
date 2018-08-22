from datetime import datetime
import pandas as pd

basic_index = pd.MultiIndex.from_product([[1, 2, 3], ['a', 'b', 'c']])
print(basic_index.values)

orders = pd.DataFrame(
    data={
        'customer': [1, 2, 3, 2, 3, 1, 1],
        'order_date': [
            datetime(2018, 1, 3),
            datetime(2018, 1, 5),
            datetime(2018, 1, 7),
            datetime(2018, 1, 8),
            datetime(2018, 1, 9),
            datetime(2018, 1, 10),
            datetime(2018, 1, 10)
        ],
        'amount': [25, 42, 116, 21, 83, 4, 67]
    }
)

print(orders)

daily_orders = orders.groupby(['customer', 'order_date']).sum()
print(daily_orders)

unique_customers = daily_orders.index.unique(level='customer')

date_range = pd.DatetimeIndex(
    start=datetime(2018, 1, 1),
    end=datetime(2018, 1, 10),
    freq='D'
)

customer_date_index = (
    pd.MultiIndex
    .from_product(
        iterables=[unique_customers, date_range],
        names=['customer', 'order_date']
    )
)

print(customer_date_index.values[:5])

daily_orders = daily_orders.reindex(customer_date_index, fill_value=0)

daily_orders['running_amount'] = (
    daily_orders
    .reindex()
    .groupby('customer')
    .cumsum()
)

print(daily_orders)
