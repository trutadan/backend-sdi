import datetime
import random
import sqlite3
import sys

from faker import Faker
from typing import Tuple


fake = Faker()

def generate_data() -> Tuple[str, str]:
    if len(sys.argv) > 1:
        try:
            number_of_records = int(sys.argv[1])
        except ValueError:
            print("Invalid argument. Using default value of 1000000.")
            number_of_records = 1000000
    else:
        number_of_records = 1000000

    try:
        # establish a connection to the database
        database_connection = sqlite3.connect('db.sqlite3')

        # create a cursor object to execute SQL queries
        database_cursor = database_connection.cursor()

        # generate fake data for Coupon
        for _ in range(number_of_records):
            random_number = random.randint(1, 50)
            code = fake.word() + str(random_number)
            amount = random_number
            database_cursor.execute("INSERT INTO api_coupon (code, amount) VALUES (?, ?)", (code, amount))

        for i in range(number_of_records):
            # generate fake data for OrderAddress
            country = fake.country()
            state = fake.state()
            city = fake.city()
            street = fake.street_address()
            apartment = fake.building_number() if random.choice([True, False]) else None
            zip_code = fake.zipcode()

            database_cursor.execute("INSERT INTO api_orderaddress (country, state, city, street, apartment, zip_code) VALUES (?, ?, ?, ?, ?, ?)",
                    (country, state, city, street, apartment, zip_code))

            # generate fake data for Order
            user_id = random.randint(1, number_of_records)
            start_date = fake.date_between(start_date=datetime.datetime.now() - datetime.timedelta(days=3*365), end_date=datetime.datetime.now())
            days_to_add = random.randint(2, 5)
            ordered_date = start_date + datetime.timedelta(days=days_to_add)
            shipping_address_id = i
            billing_address_id = i
            coupon_id = random.randint(1, number_of_records) if random.choice([True, False]) else None

            received = random.choice([True, False])
            if (received == False):
                ordered_date = None
                being_delivered = random.choice([True, False])
                refund_requested = False
                refund_granted = False

            else:
                being_delivered = False
                refund_requested = random.choice([True, False])
                if (refund_requested == True):
                    refund_granted = random.choice([True, False])
                else:
                    refund_granted = False

            database_cursor.execute("INSERT INTO api_order (user, order_placed_date, received_date, shipping_address, billing_address, coupon, delivered_status, received, refund_requested, refund_granted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (user_id, start_date, ordered_date, shipping_address_id, billing_address_id, coupon_id, being_delivered, received, refund_requested, refund_granted))
            
            # generate fake data for OrderItem
            item_id = random.randint(1, number_of_records)
            order_id = random.randint(1, number_of_records)
            quantity = random.randint(1, 10)

            database_cursor.execute("INSERT INTO api_orderitem (item, order_number, quantity) VALUES (?, ?, ?)",
                    (item_id, order_id, quantity))

            # generate fake data for Payment
            order_id = i
            payment_date = fake.date_time_between('-1y', '+1y', tzinfo=None)

            database_cursor.execute("INSERT INTO api_payment (order_number, timestamp) VALUES (?, ?)",
                    (order_id, payment_date))

            # generate fake data for Refund
            if random.choice([True, False]) == True:
                order_id = i
                reason = fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None)
                accepted = random.choice([True, False])

                database_cursor.execute("INSERT INTO api_refund (order_number, reason, status) VALUES (?, ?, ?)",
                        (order_id, reason, accepted))

        # commit the changes to the database and close the connection
        database_connection.commit()
        database_connection.close()

        return ("Coupon, OrderAddress, Order, OrderItem, Payment and Refund tables populated successfully", "Number of rows inserted: {}".format(number_of_records*2))
    
    except sqlite3.Error as error:
            print("Error occurred while connecting to or working with the database.")
            print(error)
            return ("Error occurred while working with the database", "")


if __name__ == '__main__':
    output = generate_data()
    print(output)
