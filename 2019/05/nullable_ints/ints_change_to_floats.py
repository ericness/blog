import pandas as pd

customers = pd.DataFrame(
    data={
        'customerId': ['1', '2', '3', '4'],
        'customerName': ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    }
)

orders = pd.DataFrame(
    data={
        'orderId': ['100', '101', '102', '103', '104'],
        'customerId': ['1', '1', '3', '4', '4'],
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

print(customers.merge(orders, on='customerId', how='left'))
