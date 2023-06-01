from app import create_app, make_celery

app = create_app()
celery = make_celery(app)

@celery.task(bind=True)
def long_running_task(self):
    # long running task here
    pass
