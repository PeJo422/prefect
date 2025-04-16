from prefect import flow
from prefect_github.repository import GitHubRepository

github_repository_block = GitHubRepository.load("git-pgdev")
# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="https://github.com/PeJo422/prefect.git"

print("🚀 Joke flow is starting...")

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="flows/daily_joke.py:upload_joke_to_db_flow", # Specific flow to run
    ).deploy(
        name="daily-joke-ingestion",
        description="A flow to fetch and store a daily programming joke.",
        work_pool_name="pdev-workpool",
        cron="0 * * * *",  # Run every hour
    )