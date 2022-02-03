from celery import Celery
from kombu import Exchange, Queue
from main import create_app


def make_celery(flask_app):
    celery = Celery(
        flask_app.import_name,
        result_backend=flask_app.config.pop('CELERY_RESULT_BACKEND'),
        broker=flask_app.config.pop('CELERY_BROKER_URL'),
        include=['background.tasks'],
    )
    celery.conf.update(flask_app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = make_celery(create_app())


providers_exchange = Exchange("providers_exchange", type="direct")  # External connections queue

app.conf.task_queues = (
    Queue("items_base_queue", providers_exchange, routing_key="items_base_route"),  # noqa
)
