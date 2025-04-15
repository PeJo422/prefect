from prefect import flow

# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="https://github.com/PeJo422/prefect.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="daily_joke.py:upload_joke_to_db_flow", # Specific flow to run
    ).deploy(
        name="my-first-deployment",
        parameters={
            "github_repos": [
                "prefect/daily_joke"
            ]
        },
        work_pool_name="my-work-pool",
        cron="0 * * * *",  # Run every hour
    )