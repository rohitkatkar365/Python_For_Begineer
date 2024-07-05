import sys

import pymysql
from pymysql import Error

# Connect to MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',       # Replace with your MySQL username
    password='',       # Replace with your MySQL password
    database='world',  # Replace with your database name
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Ensure state table exists
        create_state_table = '''
            CREATE TABLE IF NOT EXISTS state (
                s_id INT PRIMARY KEY,
                s_name VARCHAR(100),
                c_id INT,
                CONSTRAINT fk_state_country FOREIGN KEY (c_id) REFERENCES country(c_id)
            )
        '''
        # cursor.execute(create_state_table)

        # Ensure country table exists
        create_country_table = '''
            CREATE TABLE IF NOT EXISTS country (
                c_id INT PRIMARY KEY,
                c_name VARCHAR(100)
            )
        '''
        # cursor.execute(create_country_table)

        # Insert data into country table
        query1 = "INSERT INTO country (c_id, c_name) VALUES (%s, %s)"
        data_countries = [(1, 'India'), (2, 'Sri Lanka'), (3, 'Australia')]
        # cursor.executemany(query1, data_countries)

        # Insert data into state table
        query2 = "INSERT INTO state (s_id, s_name, c_id) VALUES (%s, %s, %s)"
        data_states = [
            (1, 'Rajasthan', 1),
            (2, 'Delhi', 1),
            (3, 'Victoria', 3),
            (4, 'Western Australia', 3),
            (5, 'Colombo', 2),
            (6, 'Kandy', 2)
        ]
        # cursor.executemany(query2, data_states)

        # Print data from state table
        # print("{:<15} {:<20} {:<20}".format("State Id", "State Name", "Country Id"))
        # query = "SELECT * FROM state inner join country on state.c_id = country.c_id"
        # cursor.execute(query)
        # sdata = cursor.fetchall()
        # for s in sdata:
        #     print("{:<15} {:<20} {:<20}".format(s['s_id'], s['s_name'], s['c_id']))
        # print("{:<15} {:<20}".format("Country Id", "Country Name"))
        # query = "SELECT * FROM country left join state on state.c_id = country.c_id"
        # cursor.execute(query)
        # sdata = cursor.fetchall()
        # for s in sdata:
        #     print("{:<15} {:<20}".format(s['c_id'], s['c_name']))

        print("{:<15} {:<20} {:<20}".format("State Id", "State Name", "Country Id"))
        query = "SELECT * FROM state right join country on state.c_id = country.c_id where state.c_id between 2 and 3"
        cursor.execute(query)
        sdata = cursor.fetchall()
        for s in sdata:
            print("{:<15} {:<20} {:<20}".format(s['s_id'], s['s_name'], s['c_id']))
    # Commit the transaction
    connection.commit()
    print("Data inserted successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    connection.close()
    print("MySQL connection is closed")
