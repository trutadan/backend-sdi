import torch
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_data(X, y):
    # Apply LabelEncoder to categorical variables
    label_encoder = LabelEncoder()
    X['shipping_address_city'] = label_encoder.fit_transform(X['shipping_address_city'])
    X['shipping_address_state'] = label_encoder.fit_transform(X['shipping_address_state'])

    with open('api/ml_model/encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)

    print("Encoder saved as encoder.pkl")

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Convert data to PyTorch tensors
    X_train = torch.tensor(X_train.values, dtype=torch.float32)
    y_train = torch.tensor(y_train.values, dtype=torch.float32)
    X_test = torch.tensor(X_test.values, dtype=torch.float32)
    y_test = torch.tensor(y_test.values, dtype=torch.float32)

    print("Successfully preprocessed data")

    return X_train, X_test, y_train, y_test