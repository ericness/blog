import pandas as pd

customers = pd.DataFrame(
    data={
        'customer_id': ['1', '2', '3', '4'],
        'customerName': ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    }
)

orders = (
    pd.DataFrame(
        data={
            'order_id': ['100', '101', '102', '103', '104'],
            'customer_id': ['1', '1', '3', '4', '4'],
            'product': [
                'Firebolt',
                'Pewter Cauldron',
                'Dragon Hide Gloves',
                'Polyjuice Potion',
                'Weasley Is Our King Buttons',
            ],
            'quantity': [1, 18, 10, 6, 120]
        }
    )
    .astype({'quantity': 'Int64'})
)

print(orders.to_string(), '\n')
print(orders.info(), '\n')

customer_orders = customers.merge(orders, on='customer_id', how='left')

print(customer_orders.to_string(), '\n')
print(customer_orders.info())
