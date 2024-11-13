import pandas as pd
import os
import sqlite3

def csv_to_sql(csv_file, db_name, table_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Ensure the database file has the correct extension
    if not db_name.endswith('.db'):
        db_name += '.db'

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)

    # Write the DataFrame to a SQL table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

    # Verify the database file is created and not empty
    if os.path.exists(db_name) and os.path.getsize(db_name) > 0:
        print(f"Database '{db_name}' created successfully.")
    else:
        print(f"Failed to create database '{db_name}'.")

# # Example usage
# csv_file = 'data.csv'  # Replace with your CSV file path
# db_name = 'database.db'  # Replace with your desired database name
# table_name = 'data_table'  # Replace with your desired table name

# csv_to_sql(csv_file, db_name, table_name)

# import pandas as pd
# import mysql.connector
# from mysql.connector import errorcode

# def csv_to_mysql(csv_file, db_name, table_name, user, password, host='localhost'):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(csv_file)

#     # Connect to MySQL server
#     try:
#         conn = mysql.connector.connect(
#             user=user,
#             password=password,
#             host=host
#         )
#         cursor = conn.cursor()

#         # Create database if it doesn't exist
#         try:
#             cursor.execute(f"CREATE DATABASE {db_name}")
#             print(f"Database '{db_name}' created successfully.")
#         except mysql.connector.Error as err:
#             if err.errno == errorcode.ER_DB_CREATE_EXISTS:
#                 print(f"Database '{db_name}' already exists.")
#             else:
#                 print(err.msg)

#         # Connect to the newly created database
#         conn.database = db_name

#         # Create table if it doesn't exist
#         columns = ", ".join([f"{col} TEXT" for col in df.columns])
#         create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
#         cursor.execute(create_table_query)

#         # Insert data into the table
#         for i, row in df.iterrows():
#             insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(row))})"
#             cursor.execute(insert_query, tuple(row))

#         # Commit the transaction
#         conn.commit()
#         print(f"Data inserted into table '{table_name}' successfully.")

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")

#     finally:
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()

# # Example usage
# csv_file = 'data.csv'  # Replace with your CSV file path
# db_name = 'my_database'  # Replace with your desired database name
# table_name = 'data_table'  # Replace with your desired table name
# user = 'your_username'  # Replace with your MySQL username
# password = 'your_password'  # Replace with your MySQL password

# csv_to_mysql(csv_file, db_name, table_name, user, password)
