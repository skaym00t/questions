import psycopg2
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

data = [(f"Клиент {i}", f'client_{i}@example.com') for i in range(1, 10001)]

total_rows = 10_000
batch_size = 1000

for i in tqdm(range(0, total_rows, batch_size)):
    batch = data[i:i + batch_size]

    cursor.executemany(
        """
        INSERT INTO customers (name, email)
        VALUES (%s, %s)
        """,
        batch
    )
    conn.commit()

cursor.close()
conn.close()
print("Заполнение таблицы customers завершено!")