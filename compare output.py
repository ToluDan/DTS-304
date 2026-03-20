from dotenv import load_dotenv
import os
import psycopg2
import time

# Load DB config
load_dotenv(r'C:\Users\USER\DTS304\DB_CONFIG.env')

DB_CONFIG = {
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# Connect to PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Fetch product IDs (unsorted for sequential search simulation)
cur.execute("SELECT product_id FROM purchases;")
rows = cur.fetchall()
product_ids = [row[0] for row in rows if row[0] is not None]

# Make a sorted copy for binary search
sorted_product_ids = sorted(product_ids)

# Ask user for product ID
target = int(input("Enter product ID to search: "))

# this is for Sequential Search
start_time = time.time()
seq_index = -1
for i, value in enumerate(product_ids):
    if value == target:
        seq_index = i
        break
seq_time = time.time() - start_time

if seq_index != -1:
    print(f"Sequential Search: Product ID {target} found at index {seq_index}")
else:
    print(f"Sequential Search: Product ID {target} not found")
print(f"Sequential Search Time: {seq_time:.6f} seconds")

# this is for Binary Search
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

start_time = time.time()
bin_index = binary_search(sorted_product_ids, target)
bin_time = time.time() - start_time

if bin_index != -1:
    print(f"Binary Search: Product ID {target} found at index {bin_index}")
else:
    print(f"Binary Search: Product ID {target} not found")
print(f"Binary Search Time: {bin_time:.6f} seconds")

# Close DB connection
cur.close()
conn.close()