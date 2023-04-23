import datetime
import hashlib
import random
import sys
import psycopg2

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
        database_connection = psycopg2.connect(
            host="127.0.0.1",
            database="sdi_db",
            user="sdi_user",
            password="sdi_password",
            port="5432",
        )

        # create a cursor object to execute SQL queries
        database_cursor = database_connection.cursor()

        for i in range(number_of_records):
            # generate fake data for UserAddress
            street = fake.street_address()
            city = fake.city()
            state = fake.state()
            country = fake.country()
            zip_code = fake.zipcode()
            database_cursor.execute("INSERT INTO api_useraddress (street, city, state, country, zip_code) VALUES (%s, %s, %s, %s, %s)", (street, city, state, country, zip_code))

        # generate fake data for UserProfile
            picture = None
            date_of_birth = fake.date_of_birth()
            phone = fake.phone_number()
            country_code = "+{}".format(random.randint(1, 999))
            created_at = fake.date_time_between(start_date='-1y', end_date='now')
            updated_at = created_at

            database_cursor.execute("INSERT INTO api_userprofile (profile_picture, date_of_birth, phone_number, country_code, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)", (picture, date_of_birth, phone, country_code, created_at, updated_at))

            # generate fake data for User
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = str(fake.random_int()) + fake.email()
            username = fake.user_name() + str(fake.random_int())
            password = hashlib.sha256("my_password".encode("utf-8")).hexdigest()
            address = i
            profile = i
            is_active = fake.boolean(chance_of_getting_true=80)
            confirmation_code = fake.uuid4() 
            confirmation_code_expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)
            created_at = fake.date_time_between(start_date='-1y', end_date='now')

            is_superuser = False
            is_staff = False
            date_joined = created_at

            database_cursor.execute("INSERT INTO api_user (first_name, last_name, email, username, address_id, profile_id, is_active, confirmation_code, confirmation_code_expiration, created_at, is_superuser, is_staff, date_joined, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, email, username, address.id if address else None, profile.id if profile else None, is_active, confirmation_code, confirmation_code_expiration, created_at, is_superuser, is_staff, date_joined, password))

        # commit the changes to the database and close the connection
        database_connection.commit()
        database_connection.close()

        return ("UserAddress, UserProfile and User tables populated successfully", "Number of rows inserted: {}".format(number_of_records*3))

    except psycopg2.Error as error:
        print("Error occurred while connecting to or working with the database.")
        print(error)
        return ("Error occurred while working with the database", "")


if __name__ == '__main__':
    output = generate_data()
    print(output)
    