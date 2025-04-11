# 🌦️ sddd-template: Streamlit + DuckDB + dlt + dbt Template Project

A template to quickly set up a data pipeline and dashboard using:

- 🐍 [Streamlit](https://streamlit.io) — interactive dashboards
- 🦆 [DuckDB](https://duckdb.org) — embedded analytics database
- 🔄 [dlt](https://dlthub.com) — declarative ELT pipeline
- 🧙‍♂️ [dbt](https://www.getdbt.com) — SQL-based transformations (not yet implemented)

This template helps you go from **data ingestion** ➜ **transformation** ➜ **visualization** in no time.

> ⚠️ I am using this project as a *learn-by-doing* side project while attending a programming course. Therefore, some parts may vary in quality as I learn and experiment!

<br/>

## 🧪 Example: OpenWeather API
**What you get:**
- Fetch current weather in multiple cities
- Store results in DuckDB locally
- Visualize weather metrics:
  - Metric table with temperature, humidity, wind
  - 📈 Line chart showing temperature trends per city

<br/>


## 📁 Project Structure

```bash
sddd-template/
├── data/                       # For .duckdb and other persistent data files
│   └── openweather.duckdb      # Your DuckDB database
│
├── dbt_project/                # For dbt (to be implemented)
│
├── dlt_pipeline/               # Contains source logic split into clean modules
│   ├── __init__.py
│   ├── db.py                   # DuckDBConnection class
│   ├── fetch_current.py        # current_weather resource
│   ├── fetch_historical.py     # historical_weather placeholder
│   ├── pipeline.py             # run_pipeline and openweather_source
│
├── docs/                       # Documentation
│   ├── documentation.md
│
├── streamlit_app/              # The Streamlit dashboard
│   ├── utils/                  # Streamlit utility folder
│       ├── constants.py
│       ├── data_fetching.py
│       ├── plotting.py
│   ├── app.py                  # Streamlit app file
│
├── .env                        # API key (not in Git - need to be created locally)
├── .gitignore
├── config.py                   # Configuration file moved to the root
├── README.md                   # Quick start
├── requirements.txt
├── run_test.py                 # Test script
├── setup.sh

```

<br/>

## 📁 How to use this template
1. 🧱 Clone the template:
    ```bash
    git clone https://github.com/your-username/sddd-template
    cd sddd-template
2. ⚙️ Install dependencies:

    Use ```venv```, ```pipenv```, ```conda``` or ```uv```. Example with ```uv```:
    ```bash
    uv venv
    .venv\scripts\activate     # Windows
    source .venv/bin/activate  # Mac/Linux
    uv pip install -r requirements.txt
3. 🔑 Configure API access:

    Create a ```.env``` file in the root folder:
    ```bash
    OPENWEATHER_API_KEY=your_api_key_here
4. 📊 Launch Streamlit Dashboard
    ```bash
    streamlit run streamlit_app/dashboard.py
(**dbt** integration coming soon)
<!---
4. 🧪 Run the dlt Pipeline:
    ```
    python dlt_pipeline/openweather_source.py
5. 📦 Run dbt Transformations
    ```
    cd dbt_project
    dbt run
    -->
---
<br/>


## 🧰 Customizing the Template
**Documentation and guide for adding new APIs or sources is in progress. You'll be able to:**
- Add new dlt pipelines
- Extend the dbt SQL models
- Visualize different data types in Streamlit
- Plug in ML or scheduling

<br/>

## 🧠 Planned Extensions
- 🔮 Add a regression model to forecast temperature trends
- 🕰️ Add scheduling (cron or Airflow)
- 🐳 Dockerize the full stack

<br/>

## 📝 Naming Conventions
- Pipelines: ```dlt_pipeline/<source>_source.py```
- dbt models: ```dbt_project/models/staging/stg_<source>.sql```
- Dashboard: ```streamlit_app/app.py```

<br/>

## 📚 Resources
- [OpenWeather API Docs](https://docs.openweather.co.uk/appid)
- [dlt Docs](https://dlthub.com/docs/intro)
- [DuckDB Docs](https://duckdb.org/docs/stable/)
- [dbt Docs](https://docs.getdbt.com/)
- [Streamlit Docs](https://docs.streamlit.io/)