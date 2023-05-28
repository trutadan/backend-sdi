from api.authentication import CustomUserAuthentication
from api.ml_models.predict_shipping_time.real_time_prediction import estimate_delivery_date
from api.permissions import IsAdmin, IsModeratorWithNoDeletePrivilege
from api.models.order import Order
from api.views.user_view import AuthenticatedUserInformationView

from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
@authentication_classes([CustomUserAuthentication])
@permission_classes([AuthenticatedUserInformationView, IsAdmin|IsModeratorWithNoDeletePrivilege])
def delivery_date_view(request, order_id):
    try:
        # Retrieve the estimated location and delivery date
        delivery_date = estimate_delivery_date(order_id)

        # Convert the delivery date to a formatted string
        formatted_delivery_date = delivery_date.strftime("%Y-%m-%d")

        # Return the estimated location and delivery date as JSON response
        return JsonResponse({'delivery_date': formatted_delivery_date})
    except Order.DoesNotExist:
        # Handle the case where the order with the given ID does not exist
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        # Handle any other exceptions that may occur
        return JsonResponse({'error': str(e)}, status=500)
