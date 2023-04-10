import psycopg2

def remove_data_for_tables() -> str:
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="sdi_db",
        user="sdi_user",
        password="sdi_password",
        port="5432",
    )
    
    c = connection.cursor()

    # Reset sequence for id column in api_itemcategory table
    c.execute("DELETE FROM api_itemcategory")
    c.execute("ALTER SEQUENCE api_itemcategory_id_seq RESTART WITH 1")

    # Reset sequence for id column in api_item table
    c.execute("DELETE FROM api_item")
    c.execute("ALTER SEQUENCE api_item_id_seq RESTART WITH 1")

    # Save the changes to the database and close the connection
    connection.commit()
    connection.close()

    return ("ItemCategory and Item tables data removed successfully!")


remove_data_for_tables()
