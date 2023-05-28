from api.ml_models.predict_shipping_time.data_preprocessing import preprocess_data
from api.ml_models.predict_shipping_time.data_collection import get_data
from api.ml_models.predict_shipping_time.model_training import train_model
from api.ml_models.predict_shipping_time.model_evaluation import evaluate_model
from api.models.order import Order

from datetime import timedelta


def get_shipping_time_prediction(order_id):
    order = Order.objects.get(id=order_id)
    
    X, y = get_data()
    encoder, X_train, X_test, y_train, y_test = preprocess_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    city = encoder.transform([order.shipping_address.city])
    state = encoder.transform([order.shipping_address.state])
    prediction = model.predict([[city, state]])

    return timedelta(seconds=prediction.item())
