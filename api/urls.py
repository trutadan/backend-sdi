from django.urls import path
from api.views.confirm_register_view import ConfirmRegisterView
from api.views.login_view import LoginView
from api.views.logout_view import LogoutView
from api.views.register_view import RegisterView

from api.views.user_address_view import UserAddressList, UserAddressDetail
from api.views.user_view import UserList, UserDetail, UserView
from api.views.user_profile_view import UserProfileList, UserProfileDetail
from api.views.item_view import ItemList, ItemDetail
from api.views.item_order_view import ItemOrderList, ItemOrderDetail
from api.views.item_cart_view import ItemCartList, ItemCartDetail
from api.views.order_address_view import OrderAddressList, OrderAddressDetail
from api.views.payment_view import PaymentList, PaymentDetail
from api.views.coupon_view import CouponList, CouponDetail
from api.views.order_view import OrderList, OrderDetail
from api.views.order_item_view import OrderItemList, OrderItemDetail
from api.views.refund_view import RefundList, RefundDetail
from api.views.cart_view import CartList, CartDetail
from api.views.cart_item_view import AddMultipleItemsToCartView, CartItemList, CartItemDetail
from api.views.item_category_view import ItemCategoryAutocomplete, ItemCategoryList, ItemCategoryDetail
from api.views.most_sold_items_view import MostSoldItemsView
from api.views.average_category_price_view import AverageCategoryPriceView


urlpatterns = [
    path('user-address/', UserAddressList.as_view()),
    path('user-address/<int:pk>/', UserAddressDetail.as_view()),

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()), 

    path('user-profile/', UserProfileList.as_view()),
    path('user-profile/<int:pk>/', UserProfileDetail.as_view()), 

    path('register/', RegisterView.as_view()),
    path('register/confirm/<str:confirmation_code>/', ConfirmRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()), 
    path('item/most-sold/', MostSoldItemsView.as_view()),
    path('item/<int:pk>/order/', ItemOrderList.as_view()),
    path('item/<int:pk>/order/<int:order_pk>/', ItemOrderDetail.as_view()),
    path('item/<int:pk>/cart/', ItemCartList.as_view()),
    path('item/<int:pk>/cart/<int:cart_pk>/', ItemCartDetail.as_view()),

    path('order-address/', OrderAddressList.as_view()),
    path('order-address/<int:pk>/', OrderAddressDetail.as_view()), 

    path('payment/', PaymentList.as_view()),
    path('payment/<int:pk>/', PaymentDetail.as_view()), 

    path('coupon/', CouponList.as_view()),
    path('coupon/<int:pk>/', CouponDetail.as_view()), 

    path('order/', OrderList.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view()), 
    path('order/<int:pk>/item/', OrderItemList.as_view()),
    path('order/<int:pk>/item/<int:item_pk>/', OrderItemDetail.as_view()),

    path('refund/', RefundList.as_view()),
    path('refund/<int:pk>/', RefundDetail.as_view()), 

    path('cart/', CartList.as_view()),
    path('cart/<int:pk>/', CartDetail.as_view()), 
    path('cart/<int:pk>/item/', CartItemList.as_view()), 
    path('cart/<int:pk>/item/<int:item_pk>/', CartItemDetail.as_view()), 
    path('cart/<int:pk>/item/add-multiple/', AddMultipleItemsToCartView.as_view()),

    path('item-category/', ItemCategoryList.as_view()),
    path('item-category/<int:pk>/', ItemCategoryDetail.as_view()),
    path('item-category/average-price/', AverageCategoryPriceView.as_view()),
    path('item-category/autocomplete/', ItemCategoryAutocomplete.as_view()),
]