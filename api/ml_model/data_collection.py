import pandas as pd


def get_data_from_csv(filename):
    data = pd.read_csv(filename)

    X = data[['shipping_address_city', 'shipping_address_state']]
    y = data['shipping_duration']

    print(f'Successfully read {len(data)} rows from CSV file')

    return X, y
