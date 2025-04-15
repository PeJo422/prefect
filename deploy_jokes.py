from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

SOURCE_REPO = "https://github.com/PeJo422/prefect.git"

if __name__ == "__main__":
    Deployment.build_from_source(
        name="daily-joke-deployment",
        work_pool_name="my-work-pool",
        schedule=CronSchedule(cron="0 0 * * *", timezone="UTC"),
        source=SOURCE_REPO,
        entrypoint="my_workflow.py:daily_jokes",  # your flow function
    ).apply()
