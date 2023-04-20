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
            # Reset sequence for id column in api_cartitem table
            database_cursor.execute("DELETE FROM api_cartitem")
            database_cursor.execute("ALTER SEQUENCE api_cartitem_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_cart table
            database_cursor.execute("DELETE FROM api_cart")
            database_cursor.execute("ALTER SEQUENCE api_cart_id_seq RESTART WITH 1")

        database_connection.commit()

    return "CartItem and Cart tables data removed successfully!"


if __name__ == "__main__":
    output = remove_data()
    print(output)
