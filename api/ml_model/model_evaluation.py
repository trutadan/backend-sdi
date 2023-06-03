import torch
import torch.nn as nn


def evaluate_model(model, X_test, y_test):
    with torch.no_grad():
        print("Evaluating model...")
        
        y_pred = model(X_test).squeeze().numpy()

        mse = nn.MSELoss()
        mae = nn.L1Loss()

        loss = mse(torch.tensor(y_pred), y_test)
        mae_value = mae(torch.tensor(y_pred), y_test)

        print(f'Test Loss: {loss:.4f}')
        print(f'Test MAE: {mae_value:.4f}')

        return y_pred
