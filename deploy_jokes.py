from prefect import flow

if __name__ == "__main__":
    flow.daily_joke.deploy(
        name="daily-joke-deployment",
        work_pool_name="my-work-pool",
        cron="0 * * * *",  # Run every day at midnight
    )