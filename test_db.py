import pandas as pd
from sqlalchemy import create_engine

# أكواد الألوان
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# الاتصال بقاعدة البيانات
engine = create_engine("sqlite:///olist_db.sqlite")

# 1. استعلام لاختبار حساب حالة التأخير (is_late)
query_orders = """
SELECT 
    order_id,
    order_status,
    order_delivered_customer_date,
    order_estimated_delivery_date,
    CASE 
        WHEN JULIANDAY(order_delivered_customer_date) > JULIANDAY(order_estimated_delivery_date) THEN 1
        ELSE 0
    END AS is_late
FROM orders
WHERE order_status = 'delivered'
LIMIT 5;
"""

print(f"{CYAN}--- Testing is_late calculation ---{RESET}")
df_orders = pd.read_sql(query_orders, engine)
print(f"{GREEN}{df_orders}{RESET}\n")

# 2. استعلام يربط جدولين مع بعض (JOIN)
query_join = """
SELECT 
    o.order_id,
    c.customer_city,
    c.customer_state,
    o.order_status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
LIMIT 5;
"""

print(f"{CYAN}--- Testing JOIN between Orders and Customers ---{RESET}")
df_join = pd.read_sql(query_join, engine)
print(f"{YELLOW}{df_join}{RESET}")