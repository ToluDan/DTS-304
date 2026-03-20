import psycopg2
import os, time
from dotenv import load_dotenv

load_dotenv(r'C:\Users\USER\DTS304\DB_CONFIG.env')

#Load config from my  .env file
DB_CONFIG = {
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# Connecting to PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Fetching product IDs and sort them
cur.execute("SELECT product_id FROM purchases ORDER BY product_id;")
rows = cur.fetchall()
product_ids = [row[0] for row in rows if row[0] is not None]

# print("Product IDs:", product_ids)

# Binary search function
def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#  getting user input for product ID
target = int(input("Enter product ID to search: "))

# Run binary search
index = binary_search(product_ids, target)
if index != -1:
    print(f" Product ID {target} found at index {index}")
else:
    print(f" Product ID {target} not found")

# Close DB connection
cur.close()
conn.close()