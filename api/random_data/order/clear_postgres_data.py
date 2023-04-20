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
            # Reset sequence for id column in api_coupon table
            database_cursor.execute("DELETE FROM api_coupon")
            database_cursor.execute("ALTER SEQUENCE api_coupon_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_orderaddress table
            database_cursor.execute("DELETE FROM api_orderaddress")
            database_cursor.execute("ALTER SEQUENCE api_orderaddress_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_order table
            database_cursor.execute("DELETE FROM api_order")
            database_cursor.execute("ALTER SEQUENCE api_order_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_orderitem table
            database_cursor.execute("DELETE FROM api_orderitem")
            database_cursor.execute("ALTER SEQUENCE api_orderitem_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_payment table
            database_cursor.execute("DELETE FROM api_payment")
            database_cursor.execute("ALTER SEQUENCE api_payment_id_seq RESTART WITH 1")
            
            # Reset sequence for id column in api_refund table
            database_cursor.execute("DELETE FROM api_refund")
            database_cursor.execute("ALTER SEQUENCE api_refund_id_seq RESTART WITH 1")

        database_connection.commit()

    return "Coupon, OrderAddress, Order, OrderItem, Payment and Refund tables data removed successfully!"


if __name__ == "__main__":
    output = remove_data()
    print(output)
