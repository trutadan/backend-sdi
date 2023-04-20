import sqlite3


def remove_data() -> str:
    with sqlite3.connect('db.sqlite3') as database_connection:
        database_cursor = database_connection.cursor()

        # Reset sequence for id column in api_useraddress table
        database_cursor.execute("DELETE FROM api_useraddress")
        database_cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'api_useraddress'")

        # Reset sequence for id column in api_userprofile table
        database_cursor.execute("DELETE FROM api_userprofile")
        database_cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'api_userprofile'")

        # Reset sequence for id column in api_user table
        database_cursor.execute("DELETE FROM api_user")
        database_cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'api_user'")

    return "UserAddress, UserProfile and User tables data removed successfully!"


if __name__ == '__main__':
    output = remove_data()
    print(output)
