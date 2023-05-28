from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def preprocess_data(X, y):
    # Convert categorical variables into numerical representations
    encoder = LabelEncoder()

    # Convert the QuerySet to a list of dictionaries
    X_list = list(X)  
    X_dict = {
        'city': [item['shipping_address__city'] for item in X_list],
        'state': [item['shipping_address__state'] for item in X_list]
    }
    X_encoded = {
        'city': encoder.fit_transform(X_dict['city']),
        'state': encoder.fit_transform(X_dict['state'])
    }

    # Convert y to a list of durations
    y_list = list(y)
    y_durations = [item['shipping_duration'] for item in y_list]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_durations, test_size=0.2, random_state=42)

    return encoder, X_train, X_test, y_train, y_test
