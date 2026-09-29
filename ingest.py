import os
import glob
import pandas as pd
from sqlalchemy import create_engine

# إنشاء قاعدة بيانات SQLite محلياً
engine = create_engine("sqlite:///olist_db.sqlite")

print("Loading data into SQLite...\n")

# البحث عن جميع ملفات CSV في المجلد الرئيسي وفي المجلدات الفرعية
csv_files = glob.glob("**/*.csv", recursive=True)

for file_path in csv_files:
    # الحصول على اسم الملف فقط بدون المسار أو الامتداد لتسمية الجدول
    file_name = os.path.basename(file_path)
    
    # تجنب قراءة ملفات مؤقتة إذا وجدت
    if file_name.startswith("~"):
        continue

    # استخراج اسم الجدول من اسم الملف (إزالة .csv)
    table_name = file_name.replace(".csv", "").replace("_dataset", "").replace("olist_", "")

    try:
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Uploaded table '{table_name}' from {file_path} ({len(df)} rows)")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

print("\nData upload completed successfully!")