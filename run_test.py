from dlt_pipeline.pipeline import run_pipeline

# Cities to test with
cities = ["Stockholm", "Berlin", "Tokyo"]

# Table you want to test
table_name = "current_weather"

# Run the pipeline
run_pipeline(cities, table_name)
