import sqlite3


def remove_data() -> str:
    with sqlite3.connect('db.sqlite3') as database_connection:
        database_cursor = database_connection.cursor()
        
        # Reset sequence for id column in api_coupon table
        database_cursor.execute("DELETE FROM api_coupon")
        database_cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='api_coupon'")

        # Reset sequence for id column in api_orderaddress table
        database_cursor.execute("DELETE FROM api_orderaddress")
        database_cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='api_orderaddress'")

        # Reset sequence for id column in api_order table
        database_cursor.execute("DELETE FROM api_order")
        database_cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='api_order'")

        # Reset sequence for id column in api_orderitem table
        database_cursor.execute("DELETE FROM api_orderitem")
        database_cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='api_orderitem'")

        # Reset sequence for id column in api_payment table
        database_cursor.execute("DELETE FROM api_payment")
        database_cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='api_payment'")

        # Reset sequence for id column in api_refund table
        database_cursor.execute("DELETE FROM api_refund")
        database_cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='api_refund'")

    return "Coupon, OrderAddress, Order, OrderItem, Payment and Refund tables data removed successfully!"


if __name__ == "__main__":
    output = remove_data()
    print(output)