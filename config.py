from dotenv import load_dotenv
import os

load_dotenv('.env')
DB_SCHEMA = os.getenv('Schema')
DB_USERNAME = os.getenv('Username')
DB_PASSWORD = os.getenv('Password')
DB_PORT = os.getenv('PortNumber')
DB_HOST = os.getenv('Server')
