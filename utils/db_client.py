import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.config_reader import ConfigReader


load_dotenv()  # loads .env file locally


class DBClient:

    def __init__(self):

        db_password = os.getenv("DB_PASSWORD")

        if not db_password:
            raise ValueError("DB_PASSWORD not found")

        self.connection = psycopg2.connect(
            host=ConfigReader.get("database", "host"),
            database=ConfigReader.get("database", "database"),
            user=ConfigReader.get("database", "user"),
            password=db_password,
            port=ConfigReader.get("database", "port")
        )

    def execute_query(self, query, params=None):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.fetchall()

    def close(self):
        self.connection.close()