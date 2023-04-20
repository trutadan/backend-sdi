import psycopg2


def remove_data() -> str:
    connection_parameters = {
        "host": "127.0.0.1",
        "database": "sdi_db",
        "user": "sdi_user",
        "password": "sdi_password",
        "port": "5432",
    }

    with psycopg2.connect(**connection_parameters) as database_connection:
        with database_connection.cursor() as database_cursor:
            # Reset sequence for id column in api_itemcategory table
            database_cursor.execute("DELETE FROM api_itemcategory")
            database_cursor.execute("ALTER SEQUENCE api_itemcategory_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_item table
            database_cursor.execute("DELETE FROM api_item")
            database_cursor.execute("ALTER SEQUENCE api_item_id_seq RESTART WITH 1")

        database_connection.commit()

    return "ItemCategory and Item tables data removed successfully!"


if __name__ == "__main__":
    output = remove_data()
    print(output)
