from django.contrib import admin

from api.models.user_address import UserAddress
from api.models.user import User
from api.models.user_profile import UserProfile
from api.models.item import Item
from api.models.order_item import OrderItem
from api.models.order_address import OrderAddress
from api.models.payment import Payment
from api.models.coupon import Coupon
from api.models.order import Order
from api.models.refund import Refund
from api.models.cart_item import CartItem
from api.models.cart import Cart

# Register your models here.
admin.site.register(UserAddress)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(OrderAddress)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(Refund)
admin.site.register(CartItem)
admin.site.register(Cart)