import pickle
import torch
import torch.nn as nn

from datetime import timedelta

from api.models import Order


def get_shipping_time_prediction(order_id):
    order = Order.objects.get(id=order_id)

    with open('api/ml_model/encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)
    model_state_dict = torch.load("api/ml_model/model.pth")

    model = nn.Sequential(
        nn.Linear(2, 64),
        nn.ReLU(),
        nn.Linear(64, 64),
        nn.ReLU(),
        nn.Linear(64, 1)
    )
    model.load_state_dict(model_state_dict)
    model.eval()

    # Fit the encoder with the available data
    city_data = [order.shipping_address.city]
    state_data = [order.shipping_address.state]
    encoder.fit(city_data + state_data)

    city = encoder.transform(city_data)
    state = encoder.transform(state_data)

    input_data = torch.tensor([[city, state]], dtype=torch.float32)
    input_data = input_data.view(1, 2)

    with torch.no_grad():
        prediction = model(input_data)

    return prediction.item()