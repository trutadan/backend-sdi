import csv
import sqlite3


def export_orders_from_sqlite_to_csv(filename):
    # Connect to the database
    database_connection = sqlite3.connect('db.sqlite3')

    # Create a cursor
    cursor = database_connection.cursor()

    # Fetch the relevant order data
    cursor.execute("""
        SELECT
            oa.city AS shipping_address_city,
            oa.state AS shipping_address_state,
            julianday(o.received_date) - julianday(o.order_placed_date) AS shipping_duration
        FROM
            api_order o
        INNER JOIN
            api_orderaddress oa ON o.shipping_address = oa.id
        WHERE
            o.received = 1
    """)
    orders = cursor.fetchall()

    # Export the orders to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['shipping_address_city', 'shipping_address_state', 'shipping_duration'])
        writer.writerows(orders)

    print(f'Successfully exported {len(orders)} orders to CSV file')

    # Close the database connection
    database_connection.close()
