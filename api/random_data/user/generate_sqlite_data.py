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

        # generate fake data for UserAddress
        for _ in range(number_of_records):
            street = fake.street_address()
            city = fake.city()
            state = fake.state()
            country = fake.country()
            zip_code = fake.zipcode()
            database_cursor.execute("INSERT INTO api_useraddress (street, city, state, country, zip_code) VALUES (?, ?, ?, ?, ?)", (street, city, state, country, zip_code))

        # generate fake data for UserProfile
        for _ in range(number_of_records):
            picture = None
            date_of_birth = fake.date_of_birth()
            phone = fake.phone_number()
            country_code = "+{}".format(random.randint(1, 999))
            created_at = fake.date_time_between(start_date='-1y', end_date='now')
            updated_at = created_at

            database_cursor.execute("INSERT INTO api_userprofile (picture, date_of_birth, phone, country_code, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)", (picture, date_of_birth, phone, country_code, created_at, updated_at))

        # generate fake data for User
        for _ in range(number_of_records):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            username = fake.user_name()
            address = random.randint(1, number_of_records) if random.choice([True, False]) else None
            profile = random.randint(1, number_of_records) if random.choice([True, False]) else None
            created_at = fake.date_time_between(start_date='-1y', end_date='now')

            database_cursor.execute("INSERT INTO api_user (first_name, last_name, email, username, address_id, profile_id, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, username, address.id if address else None, profile.id if profile else None, created_at))

        # commit the changes to the database and close the connection
        database_connection.commit()
        database_connection.close()

        return ("UserAddress, UserProfile and User tables populated successfully", "Number of rows inserted: {}".format(number_of_records*3))

    except sqlite3.Error as error:
        print("Error occurred while connecting to or working with the database.")
        print(error)
        return ("Error occurred while working with the database", "")


if __name__ == '__main__':
    output = generate_data()
    print(output)
    