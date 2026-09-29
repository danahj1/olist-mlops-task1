# Olist E-Commerce Data Pipeline & Storage (MLOps - Task 1)

## 📌 Project Overview
Automated data ingestion pipeline from raw Olist e-commerce CSV datasets into a local SQLite relational database (`olist_db.sqlite`), verifying system integrity, SQL joins, and target variable calculation (`is_late`).

## 🛠️ Tech Stack
* Python 3.x
* SQLite & SQLAlchemy
* pandas & glob

## 🚀 Execution
1. Run ingestion: `python ingest.py`
2. Run tests: `python test_db.py`