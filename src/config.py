import os
from dotenv import load_dotenv

load_dotenv()

class Development():
    MYSQL_DATABASE_HOST="localhost"
    MYSQL_DATABASE_PORT=3306
    MYSQL_DATABASE_USER="root"
    MYSQL_DATABASE_PASSWORD="root"
    MYSQL_DATABASE_DB="flask_todo_DAW"

class Build():
    MYSQL_DATABASE_HOST=os.getenv("MYSQL_DATABASE_HOST")
    MYSQL_DATABASE_PORT=int(os.getenv("MYSQL_DATABASE_PORT"))
    MYSQL_DATABASE_USER=os.getenv("MYSQL_DATABASE_USER")
    MYSQL_DATABASE_PASSWORD=os.getenv("MYSQL_DATABASE_PASSWORD")
    MYSQL_DATABASE_DB=os.getenv("MYSQL_DATABASE_DB")
