from my_workflow import daily_jokes  # <- Import the flow directly

if __name__ == "__main__":
    daily_jokes.deploy(
        name="daily-joke-deployment",
        work_pool_name="my-work-pool",
        cron="0 * * * *",  # Run every day at midnight
    )