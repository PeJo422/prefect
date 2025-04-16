import requests
import pandas as pd
from prefect import flow, task
from prefect.blocks.system import Secret
from sqlalchemy import create_engine
from datetime import datetime

from prefect import flow, task
from utils.postgres_db_connection import get_connection_string

@task
def connect_and_do_something():
    conn_str = get_connection_string()
    # Now use conn_str with SQLAlchemy or whatever


@task
def fetch_programming_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Programming')
    data = response.json()

    if data.get("error"):
        raise ValueError("Joke API returned an error.")

    # Flatten flags and add metadata
    joke_data = {
        "joke_id": data.get("id"),
        "category": data.get("category"),
        "joke": data.get("joke") if data.get("type") == "single" else f"{data.get('setup')} - {data.get('delivery')}",
        "nsfw": data["flags"].get("nsfw", False),
        "religious": data["flags"].get("religious", False),
        "political": data["flags"].get("political", False),
        "racist": data["flags"].get("racist", False),
        "sexist": data["flags"].get("sexist", False),
        "explicit": data["flags"].get("explicit", False),
        "date": datetime.now()
    }

    return joke_data

@task
def write_to_postgres(conn_str, joke_data):
    engine = create_engine(conn_str)
    df = pd.DataFrame([joke_data])
    df.to_sql("daily_jokes", engine, if_exists="append", index=False, schema="public")
    print(f"✅ Joke saved: {joke_data['joke']}")

@flow
def upload_joke_to_db_flow():
    conn_str = get_connection_string()
    joke_data = fetch_programming_joke()
    write_to_postgres(conn_str, joke_data)

if __name__ == "__main__":
    upload_joke_to_db_flow()