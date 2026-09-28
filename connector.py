import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        port = os.getenv("PORT"),
        user = os.getenv("DB_USER"),
        password = os.getenv("PASSWORD"),
        database = os.getenv("DATABASE"),
        use_pure = True
    )

connect = get_db_connection()

