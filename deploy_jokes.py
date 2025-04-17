from prefect import flow
from prefect_github.repository import GitHubRepository

github_repository_block = GitHubRepository.load("git-pgdev")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/PeJo422/prefect.git",
        entrypoint="flows/daily_joke.py:upload_joke_to_db_flow"
    ).deploy(
        name="daily-joke-ingestion",
        description="A flow to fetch and store a daily programming joke.",
        work_pool_name="pdev-workpool",  # managed
        cron="0 * * * *"
    )
