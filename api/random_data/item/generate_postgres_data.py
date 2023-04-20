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

        # generate fake data for ItemCategory
        for _ in range(number_of_records):
            name = fake.word() + " " + str(random.randint(1, number_of_records))
            subcategory = fake.word() + " " + str(random.randint(1, number_of_records)) if random.choice([True, False]) else None
            database_cursor.execute("INSERT INTO api_itemcategory (name, subcategory) VALUES (%s, %s)", (name, subcategory))

        # generate fake data for Item
        for _ in range(number_of_records):
            title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            category_id = random.randint(1, number_of_records)
            price = round(random.uniform(1, 100), 2)
            discount_price = round(price * random.uniform(0.1, 0.5), 2) if random.choice([True, False]) else None
            available_number = random.randint(0, 100)
            total_number = random.randint(100, 1000)
            description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
            picture = None

            database_cursor.execute("INSERT INTO api_item (title, category, price, discount_price, available_number, total_number, description, picture) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (title, category_id, price, discount_price, available_number, total_number, description, picture))

        # commit the changes to the database and close the connection
        database_connection.commit()
        database_connection.close()

        return ("ItemCategory and Item tables populated successfully", "Number of rows inserted: {}".format(number_of_records*2))
    
    except psycopg2.Error as error:
        print("Error occurred while connecting to or working with the database.")
        print(error)
        return ("Error occurred while working with the database", "")


if __name__ == '__main__':
    output = generate_data()
    print(output)
