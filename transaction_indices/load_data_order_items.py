import psycopg2
import random
from tqdm import tqdm

conn_params = {
    "dbname": "test_koltsov_db",
    "user": "postgres",
    "password": "4freund_",
    "host": "localhost",
    "port": "5432"
}

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

cursor.execute("SELECT id FROM orders")
order_ids = [row[0] for row in cursor.fetchall()]

products = [f"Продукт {i}" for i in range(1, 501)]

total_rows = 1_000_000
batch_size = 10_000

for i in tqdm(range(0, total_rows, batch_size)):
    batch = []
    for _ in range(batch_size):
        order_id = random.choice(order_ids)
        product_name = random.choice(products)
        quantity = random.randint(1, 10)
        price = round(random.uniform(100, 100000), 2)
        batch.append((order_id, product_name, quantity, price))

    cursor.executemany(
        """
        INSERT INTO order_items (order_id, product_name, quantity, price)
        VALUES (%s, %s, %s, %s)
        """,
        batch
    )
    conn.commit()

cursor.close()
conn.close()
print("Заполнение таблицы order_items завершено!")