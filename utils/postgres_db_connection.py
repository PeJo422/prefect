from prefect.blocks.system import Secret

pgdev_host_details = {
    "user": "pejo",
    "host": "pgsql-pdev.postgres.database.azure.com",
    "port": 5432,
    "db": "postgres"
}

def pg_connection_string():
    password = Secret.load("az-pgdev-password").get()
    return f"postgresql+psycopg2://{pgdev_host_details['user']}:{password}@{pgdev_host_details['host']}:{pgdev_host_details['port']}/{pgdev_host_details['db']}"
