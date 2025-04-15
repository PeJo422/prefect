from prefect import flow
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from prefect.filesystems import GitHub

from daily_joke import upload_joke_to_db_flow

if __name__ == "__main__":
    Deployment.build_from_flow(
        flow=upload_joke_to_db_flow,
        name="daily-joke-deployment",
        work_pool_name="my-work-pool",
        schedule=CronSchedule(cron="0 * * * *", timezone="UTC"),  # Hourly
        path=".",
        storage=GitHub(
            repo="PeJo422/prefect",
            reference="main",  # or "master" if you're living in the 1900s
            access_token="{{ secrets.GITHUB_TOKEN }}"  # set this in your Prefect Cloud secrets
        ),
    ).apply()
