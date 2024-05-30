import psycopg2
import xlrd

# Define the database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'Dhanvantri',
    'user': 'postgres',
    'password': '8008'
}

# Define the path to your Excel file
excel_file_path = 'D://Projctzz//Dhanvantri//drug data//master_drug_data_v2.1.xlsx'

# Establish a connection to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    print("Connected to the database")
except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to the database: {error}")

# Create a cursor object
cursor = conn.cursor()

# Check if the 'drugs' table already exists and create it if not
try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS drugs (
        Drug_Name varchar(1000),
        Usage varchar(1000),
        Dosage varchar(1000),
        Warning varchar(1000)
    )
    """)
    conn.commit()
except (Exception, psycopg2.Error) as error:
    print(f"Error creating table: {error}")
    conn.rollback()

# Open the Excel file and read the data
try:
    workbook = xlrd.open_workbook(excel_file_path)
    sheet = workbook.sheet_by_index(0)  # Assuming data is on the first sheet

    # Assuming the first row in the Excel file contains column headers
    headers = sheet.row_values(0)

    # Loop through the rows in the Excel file (starting from the second row)
    for row_index in range(1, sheet.nrows):
        row_data = sheet.row_values(row_index)

        # Assuming the order of data in Excel matches the table's column order
        insert_query = "INSERT INTO drugs ({}) VALUES ({})"
        placeholders = ", ".join(["%s" for _ in headers])
        insert_query = insert_query.format(", ".join(headers), placeholders)

        cursor.execute(insert_query, row_data)

    conn.commit()
    print("Data imported into the 'drugs' table")
except Exception as e:
    print(f"Error reading or inserting data from Excel: {e}")

# Close the cursor and the connection
cursor.close()

if conn:
    conn.close()
    print("Database connection closed")
