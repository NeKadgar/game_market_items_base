from kombu import Exchange, Queue
from background import make_celery
from main import create_app


app = make_celery(create_app())


providers_exchange = Exchange("providers_exchange", type="direct")  # External connections queue

app.conf.task_queues = (
    Queue("items_base_queue", providers_exchange, routing_key="items_base_route"),  # noqa
)
