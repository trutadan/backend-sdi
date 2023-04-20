import sqlite3


def remove_data() -> str:
    with sqlite3.connect('db.sqlite3') as database_connection:
        database_cursor = database_connection.cursor()

        # Reset sequence for id column in api_itemcategory table
        database_cursor.execute("DELETE FROM api_itemcategory")
        database_cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'api_itemcategory'")

        # Reset sequence for id column in api_item table
        database_cursor.execute("DELETE FROM api_item")
        database_cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'api_item'")

    return "ItemCategory and Item tables data removed successfully!"


if __name__ == '__main__':
    output = remove_data()
    print(output)
