import torch

from data_collection import get_data_from_csv
from data_preprocessing import preprocess_data
from database_export import export_orders_from_sqlite_to_csv
from model_training import train_model
from model_evaluation import evaluate_model


def save_model(csv_filename, model_filename):
    export_orders_from_sqlite_to_csv(csv_filename)
    X, y = get_data_from_csv(csv_filename)
    
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    
    torch.save(model.state_dict(), model_filename)
    print(f"Model saved as '{model_filename}'")


if __name__ == "__main__":
    csv_filename = "api/ml_model/orders.csv"
    model_filename = "api/ml_model/model.pth"

    save_model(csv_filename, model_filename)