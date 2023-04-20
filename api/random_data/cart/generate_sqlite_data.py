import random
import sys
import sqlite3

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
        database_connection = sqlite3.connect("db.sqlite3")

        # create a cursor object to execute SQL queries
        database_cursor = database_connection.cursor()

        # generate fake data for Cart
        for _ in range(number_of_records):
            user_id = random.randint(1, number_of_records)
            date_created = fake.date_between(start_date='-1y', end_date='today')
            database_cursor.execute("INSERT INTO api_cart (user_id, date_created) VALUES (?, ?)",
                    (user_id, date_created))

        # generate fake data for CartItem
        for _ in range(number_of_records):
            item_id = random.randint(1, number_of_records)
            cart_id = random.randint(1, number_of_records)
            quantity = random.randint(1, 10)
            database_cursor.execute("INSERT INTO api_cartitem (item_id, cart_id, quantity) VALUES (?, ?, ?)", (item_id, cart_id, quantity))

        # commit the changes to the database and close the connection
        database_connection.commit()
        database_connection.close()

        return ("CartItem and Cart tables populated successfully", "Number of rows inserted: {}".format(number_of_records*2))

    except sqlite3.Error as error:
        print("Error occurred while connecting to or working with the database.")
        print(error)
        return ("Error occurred while working with the database", "")


if __name__ == '__main__':
    output = generate_data()
    print(output)
