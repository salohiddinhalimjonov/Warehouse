import psycopg2
import environ


env = environ.Env()
# reading .env file
environ.Env.read_env(".env")

try:
    connection = psycopg2.connect(
        dbname=env("DB_NAME"),
        user=env("DB_USER"),
        password=env("DB_PASSWORD"),
        host="127.0.0.1",
        port="5432"
    )

    cursor = connection.cursor()

except Exception as e:
    print(f"An error occurred: {e}")

cursor = connection.cursor()
