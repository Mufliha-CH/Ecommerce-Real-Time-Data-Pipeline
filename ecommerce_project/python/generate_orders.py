import pandas as pd
import random
from datetime import datetime, timedelta

# Sample customers and products
customers = [f"C{i:03d}" for i in range(101, 201)]

products = {
    "Laptop": 45000,
    "Mobile": 20000,
    "Keyboard": 1200,
    "Mouse": 500,
    "Headphones": 2500
}

orders = []

# Generate 1000 orders
for i in range(1, 1001):

    product = random.choice(list(products.keys()))

    order = {
        "order_id": f"ORD{i:04d}",
        "customer_id": random.choice(customers),
        "product": product,
        "quantity": random.randint(1, 5),
        "unit_price": products[product],
        "order_timestamp": datetime.now() - timedelta(
            minutes=random.randint(0, 10000)
        ),
        "status": "PLACED"
    }

    orders.append(order)

# Convert to DataFrame
df = pd.DataFrame(orders)

# Save as CSV
df.to_csv("ecommerce_orders.csv", index=False)

print("Orders generated successfully!")
print("Total orders:", len(df))
print(df.head())

print("\nTotal Customers:", df["customer_id"].nunique())

print("Total Products:", df["product"].nunique())

print("\nProduct Distribution:")
print(df["product"].value_counts())

print("\nDataset Shape:", df.shape)

# Create a copy of the original dataset
test_df = df.copy()

# 1. Add duplicate orders
duplicates = test_df.sample(10, random_state=42)
test_df = pd.concat([test_df, duplicates], ignore_index=True)

# 2. Introduce invalid quantities
test_df.loc[1000:1004, "quantity"] = [-2, 0, -5, 0, -1]

# 3. Introduce invalid prices
test_df.loc[1005:1009, "unit_price"] = [-500, 0, -100, 0, -250]

# Save the test dataset
test_df.to_csv("ecommerce_orders_test.csv", index=False)

print("\nTest dataset created!")
print("Original records:", len(df))
print("Test records:", len(test_df))

# Load the test dataset
test_df = pd.read_csv("ecommerce_orders_test.csv")

# Check duplicate orders
duplicates = test_df[test_df.duplicated(subset=["order_id"])]

# Check invalid quantities
invalid_quantity = test_df[test_df["quantity"] <= 0]

# Check invalid prices
invalid_price = test_df[test_df["unit_price"] <= 0]

print("\n--- DATA QUALITY REPORT ---")

print("Total Records:", len(test_df))
print("Duplicate Orders:", len(duplicates))
print("Invalid Quantities:", len(invalid_quantity))
print("Invalid Prices:", len(invalid_price))

