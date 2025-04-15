from prefect import flow, task
from prefect.blocks.system import Secret
from sqlalchemy import create_engine
import pandas as pd

@task
def get_connection_string():
    # Load your password from the Prefect block
    password = Secret.load("az-pgdev-password").get()

    # Build the connection string
    user = "pejo"
    host = "pgsql-pdev.postgres.database.azure.com"
    port = 5432
    db = "postgres"

    conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    return conn_str

@task
def create_dummy_data():
    # Just some spicy nonsense
    df = pd.DataFrame({
        "id": range(1, 6),
        "name": ["Goblin", "Wizard", "Barista", "Overthinker", "Crybaby"],
        "mood": ["Chaotic", "Sleepy", "Burnt out", "Anxious", "Hopeful-ish"],
        "energy_level": [5, 3, 2, 1, 4]
    })
    return df

@task
def write_to_postgres(conn_str, df):
    # Create the SQLAlchemy engine
    engine = create_engine(conn_str)

    # Push the data to Postgres
    df.to_sql("dummy_table", engine, if_exists="replace", index=False)
    print("✅ Dummy data successfully uploaded to 'dummy_table'.")

@flow
def upload_dummy_data_flow():
    conn_str = get_connection_string()
    df = create_dummy_data()
    write_to_postgres(conn_str, df)

if __name__ == "__main__":
    upload_dummy_data_flow()
