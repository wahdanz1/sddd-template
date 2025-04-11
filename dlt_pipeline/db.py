import duckdb as ddb
import pandas as pd

# --- Database connection class ---
class DuckDBConnection:
    """Context manager for DuckDB connection."""

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = ddb.connect(str(self.db_path))
        return self
    
    def query(self, query):
        """Execute a query and return the result."""
        try:
            return self.conn.execute(query).df()
        except Exception as e:
            print(f"Error executing query: {e}")
            return pd.DataFrame()  # Return an empty DataFrame if there's an error

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()