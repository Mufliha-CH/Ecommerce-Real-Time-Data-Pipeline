
from kafka import KafkaProducer
import json
import random
import time
import getpass
from datetime import datetime

HOST = "ecommerce-kafka-muflihamustafa-4648.a.aivencloud.com"
PORT = 15690

password = getpass.getpass("Enter Aiven Kafka password: ")

producer = KafkaProducer(
    bootstrap_servers=f"{HOST}:{PORT}",
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username="avnadmin",
    sasl_plain_password=password,
    ssl_cafile="ca.pem",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

products = {
    "Laptop": 45000,
    "Mobile": 20000,
    "Keyboard": 1200,
    "Mouse": 500,
    "Headphones": 2500
}

order_number = 1289

print("Continuous order generation started!")
print("Press Ctrl + C to stop.")

try:
    while True:
        product = random.choice(list(products.keys()))

        status = random.choices(
            ["PLACED", "SHIPPED", "DELIVERED", "CANCELLED"],
            weights=[30, 25, 40, 5]
        )[0]

        order = {
            "order_id": f"ORD{order_number:04d}",
            "customer_id": f"C{random.randint(101, 200)}",
            "product": product,
            "quantity": random.randint(1, 5),
            "unit_price": products[product],
            "order_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": status
        }

        producer.send("ecommerce_orders", value=order).get(timeout=15)

        print("New order sent:", order)

        order_number += 1
        time.sleep(5)

except KeyboardInterrupt:
    print("Order generation stopped.")

finally:
    producer.close()
