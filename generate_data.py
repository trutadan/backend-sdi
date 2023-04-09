import random
import sqlite3
from faker import Faker
from typing import Tuple

import psycopg2

fake = Faker()

def generate_sql_file(n: int) -> Tuple[str, str]:
    # conn = sqlite3.connect('db.sqlite3')

    conn = psycopg2.connect(
        host="127.0.0.1",
        database="sdi_db",
        user="sdi_user",
        password="sdi_password",
        port="5432",
    )
    
    c = conn.cursor()

    # Reset sequence for id column in api_itemcategory table
    c.execute("DELETE FROM api_itemcategory")
    c.execute("ALTER SEQUENCE api_itemcategory_id_seq RESTART WITH 1")

    # Generate fake data for ItemCategory
    for i in range(n):
        name = fake.word() + str(i)
        subcategory = fake.word() + str(i) if random.choice([True, False]) else None
        c.execute("INSERT INTO api_itemcategory (name, subcategory) VALUES (%s, %s)", (name, subcategory))

    # Reset sequence for id column in api_item table
    c.execute("DELETE FROM api_item")
    c.execute("ALTER SEQUENCE api_item_id_seq RESTART WITH 1")

    # Generate fake data for Item
    for i in range(n):
        title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        category_id = random.randint(1, n)
        price = round(random.uniform(1, 100), 2)
        discount_price = round(price * random.uniform(0.1, 0.5), 2) if random.choice([True, False]) else None
        available_number = random.randint(0, 100)
        total_number = random.randint(100, 1000)
        description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        picture = None

        c.execute("INSERT INTO api_item (title, category_id, price, discount_price, available_number, total_number, description, picture) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                  (title, category_id, price, discount_price, available_number, total_number, description, picture))

    # Save the changes to the database and close the connection
    conn.commit()
    conn.close()

    return ("ItemCategory and Item tables populated successfully", "Number of rows inserted: {}".format(n*2))


generate_sql_file(1000)
