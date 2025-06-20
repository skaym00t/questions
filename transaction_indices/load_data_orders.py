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

cursor.execute("SELECT id FROM customers")
customer_ids = [row[0] for row in cursor.fetchall()]

total_rows = 100_000
batch_size = 10_000

for i in tqdm(range(0, total_rows, batch_size)):
    batch = []
    for _ in range(batch_size):
        customer_id = random.choice(customer_ids)
        order_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        batch.append((customer_id, order_date))

    cursor.executemany(
        """
        INSERT INTO orders (customer_id, order_date)
        VALUES (%s, %s)
        """,
        batch
    )
    conn.commit()

cursor.close()
conn.close()
print("Заполнение таблицы orders завершено!")