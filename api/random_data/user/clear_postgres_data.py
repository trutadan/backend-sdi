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
            # Reset sequence for id column in api_useraddress table
            database_cursor.execute("DELETE FROM api_useraddress")
            database_cursor.execute("ALTER SEQUENCE api_useraddress_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_userprofile table
            database_cursor.execute("DELETE FROM api_userprofile")
            database_cursor.execute("ALTER SEQUENCE api_userprofile_id_seq RESTART WITH 1")

            # Reset sequence for id column in api_user table
            database_cursor.execute("DELETE FROM api_user")
            database_cursor.execute("ALTER SEQUENCE api_user_id_seq RESTART WITH 1")

        database_connection.commit()

    return "UserAddress, UserProfile and User tables data removed successfully!"


if __name__ == "__main__":
    output = remove_data()
    print(output)
