# 🌦️ sddd-template: Streamlit + DuckDB + dlt + dbt Template Project

A template to quickly set up a data pipeline and dashboard using:

- 🐍 [Streamlit](https://streamlit.io) — interactive dashboards
- 🦆 [DuckDB](https://duckdb.org) — embedded analytics database
- 🔄 [dlt](https://dlthub.com) — declarative ELT pipeline
- 🧙‍♂️ [dbt](https://www.getdbt.com) — SQL-based transformations (not yet implemented)

This template helps you go from **data ingestion** ➜ **transformation** ➜ **visualization** in no time.

<br/>

## 🧪 Example: OpenWeather API
**What you get:**
- Current weather in user-input city
- Historical weather data (to be extended)
- Clear table of metrics (e.g. temp, humidity, wind)

<br/>


## 📁 Project Structure

```bash
sddd-template/
├── data/                   # For .duckdb and other persistent data files
│   └── openweather.duckdb  # Your DuckDB database
│
├── dbt_project/            # For dbt (to be implemented)
│
├── dlt_pipeline/           # Contains source logic split into clean modules
│   ├── __init__.py
│   ├── db.py               # DuckDBConnection class
│   ├── fetch_current.py    # current_weather resource
│   ├── fetch_historical.py # historical_weather placeholder
│   ├── pipeline.py         # run_pipeline and openweather_source
│
├── docs/                   # Documentation
│   ├── documentation.md
│
├── streamlit_app/          # The Streamlit dashboard
│   ├── app.py              # Streamlit app file
│
├── .env                    # API key (not in Git - need to be created locally)
├── .gitignore
├── config.py               # Configuration file moved to the root
├── README.md               # Quick start
├── requirements.txt
├── run_test.py             # Test script
├── setup.sh

```

<br/>

## 📁 How to use this template
1. 🧱 Clone the template:
    ```
    git clone https://github.com/your-username/sddd-template
2. ⚙️ Install dependencies:

    Use ```venv```, ```pipenv```, ```conda``` or ```uv```. Example with ```uv```:
    ```
    uv venv
    .venv\scripts\activate
    uv pip install -r requirements.txt
3. 🔑 Configure API access:

    Create a ```.env``` file in the root folder:
    ```
    OPENWEATHER_API_KEY=your_api_key_here
4. 📊 Launch Streamlit Dashboard
    ```
    streamlit run streamlit_app/dashboard.py

(**dbt** to be implemented)
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
**Documentation coming soon!**
<!---
**To use with a new data source:**
1. Duplicate ```openweather_source.py``` and adapt to your source (e.g. ```reddit_source.py```).
2. Update ```dbt/models/staging/``` with new SQL models.
3. Update your Streamlit dashboard to show new visuals.
4. Update ```.env``` with new API keys or configs.
5. Rename the project files/folders if needed.
 -->

<br/>

## 🧠 Planned Extensions
- 🧠 Add a regression model (e.g. linear regression) to forecast weather
- 📅 Add scheduling with ```cron``` or ```Airflow``` (possibly)
- 🐳 Add Docker support for full deployable stack

<br/>

## 📝 Naming Conventions
- Pipelines in ```dlt_pipeline/pipeline.py``` should be named ```<source>_source.py```
- Models in ```dbt/models/staging/``` should be named ```stg_<source>.sql```
- Dashboard file should be in ```streamlit_app/``` and named ```dashboard.py```

<br/>

## 📚 Resources
- [OpenWeather API Docs](https://docs.openweather.co.uk/appid)
- [dlt Docs](https://dlthub.com/docs/intro)
- [DuckDB Docs](https://duckdb.org/docs/stable/)
- [dbt Docs](https://docs.getdbt.com/)
- [Streamlit Docs](https://docs.streamlit.io/)