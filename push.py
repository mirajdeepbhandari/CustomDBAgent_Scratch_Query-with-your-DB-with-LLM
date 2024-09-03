import pandas as pd
from sqlalchemy import create_engine

# Read data from CSV file
csv_file_path = 'cor_Nepa2pos.xlsx'  # Replace with your CSV file path
df = pd.read_excel(csv_file_path)

# Define MySQL connection details
username = 'root'  # Replace with your MySQL username
password = ''  # Replace with your MySQL password
host = 'localhost'          # Replace with your MySQL host (usually localhost)
port = '3306'               # Replace with your MySQL port (usually 3306)
database = 'nepa'  # Replace with your MySQL database name

# Create an engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Insert data into MySQL table
table_name = 'pos'  # Replace with your MySQL table name
df.to_sql(table_name, con=engine, if_exists='append', index=False)

print("Data has been inserted successfully.")
