# 📖 Documentation: sddd-template

Welcome to the documentation for `sddd-template` — a lightweight data engineering + dashboard project using:

- 🐍 Streamlit
- 🦆 DuckDB
- 🔄 dlt
- 🧙‍♂️ dbt (coming soon)

---

## 🔑 How to Get an OpenWeather API Key

To use the weather pipeline, you’ll need a free API key from [OpenWeather](https://openweathermap.org/api):

1. Go to https://home.openweathermap.org/users/sign_up and create an account.
2. Verify your email and log in.
3. Visit the **API Keys** section and copy your default key.
4. Create a `.env` file in your root folder with:
    ```bash
    OPENWEATHER_API_KEY=your_key_here

---

## 🔧 What Are These Tools?

### Streamlit
A Python framework to create dashboards and web apps using only Python scripts — perfect for data apps.

🔗 https://streamlit.io

---

### DuckDB
An embedded SQL OLAP database that runs in-process (like SQLite but for analytics). You don’t need a server — just a file!

🔗 https://duckdb.org

---

### dlt (Data Load Tool)
A Python-first ETL tool that simplifies ingesting data from APIs and loading into destinations like DuckDB or BigQuery. Handles schema inference and pipelines declaratively.

🔗 https://dlthub.com

---

### dbt (Data Build Tool)
Used for managing SQL transformations and data modeling. Not yet active in this project but will help structure queries and analytics later.

🔗 https://www.getdbt.com

---

## 📥 How It Works (Simple Flow)

```text
+--------------+      +-------------+      +-------------+      +--------------+
|  Streamlit   | <--> |   DuckDB    | <--> |    dlt      | -->  |  OpenWeather |
| Dashboard UI |      | Local DB    |      | ELT pipeline|      |     API      |
+--------------+      +-------------+      +-------------+      +--------------+
```
1. You enter cities in the dashboard
2. dlt fetches data from OpenWeather
3. Data is stored in DuckDB
4. Streamlit queries the DuckDB database and shows:
    - Current weather table
    - Line chart of temperature trends

---

## 🧪 Testing
A small test is available:
```bash
python run_test.py
```

This ensures that the pipeline fetches valid data from the API and loads it correctly.

---

## 📍 To Be Added Soon
- dbt models and transformations
- Historical weather fetch
- Scheduled pipelines
- More visualization options