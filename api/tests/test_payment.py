from django.test import TestCase

from api.models import User, ItemCategory, Item, OrderItem, Order, Payment


class PaymentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name="Ana", last_name="Popescu", email="ana.popescu@example.com", username="ana_popescu")
        ItemCategory.objects.create(name="Protein Powder")
        Item.objects.create(title="Whey Protein Powder", category_id=1, price=300, discount_price=269, available_number=100, total_number=100, description="Double Rich Chocolate Protein Powder...")
        OrderItem.objects.create(item_id=1, order_id=1, quantity=3)
        Order.objects.create(user_id= 1, ordered_date= "2023-03-19T15:00:00Z")
        Payment.objects.create(order_id=1, timestamp="2023-03-19T15:00:57Z")

    def test_get_payment_method(self):
        payment = Payment.objects.get(order_id=1)
        expected_amount = 3*269
        computed_amount = payment.get_amount()
        self.assertEqual(expected_amount, computed_amount)

    def test_string_method(self):
        payment = Payment.objects.get(order_id=1)
        expected_payment_string = "payment for the user ana_popescu's order with the id #1 for the amount 807.00"
        self.assertEqual(str(payment), expected_payment_string)
