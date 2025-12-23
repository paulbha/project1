import os
import sys
from dotenv import load_dotenv
import psycopg2
import pandas as pd

from src.project1.exception import CustomException
from src.project1.logger import logging

# Load environment variables from .env
load_dotenv()

# Fetching variables with unique names to avoid Windows System conflicts
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
db = os.getenv("DB_NAME")

# Robust port handling
try:
    port_str = os.getenv("DB_PORT", "5432").strip().rstrip(",")
    port = int(port_str)
except (ValueError, AttributeError):
    logging.warning("Invalid port in .env. Using default port 5432.")
    port = 5432

def read_students_performance_from_sql():
    logging.info("Reading PostgreSQL database started")
    try:
        # Establish connection using the validated variables
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user=user,
            password=password
        )

        logging.info(f"Connection established successfully as user: {user}")

        # Read data
        query = "SELECT * FROM students_performance"
        df = pd.read_sql_query(query, conn)
        
        conn.close()
        logging.info("Data read successfully from students table")
        return df

    except Exception as ex:
        logging.error("Error while reading PostgreSQL data")
        # Providing more context in the exception
        raise CustomException(ex, sys)