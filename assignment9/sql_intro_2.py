# Task 5: Read Data into a DataFrame
import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
    SELECT line_items.line_item_id, line_items.quantity, line_items.product_id,
           products.product_name, products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    """
    df = pd.read_sql_query(sql_statement, conn)

print(df.head())

df['total'] = df['quantity'] * df['price']
print(df.head())

summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})
print(summary.head())

summary = summary.sort_values('product_name')
print(summary.head())

summary.to_csv('order_summary.csv')
print("Saved to order_summary.csv")