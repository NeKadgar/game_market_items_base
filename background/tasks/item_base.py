from background.celery_app import app as celery_app
from services.csmoney import DotaDataProcessor


@celery_app.task(name="update_items_base", queue="items_base_queue")
def update_items_base(**kwargs):
    DotaDataProcessor.update(kwargs)
    celery_app.send_task(name="update_steam_items", queue="base_steam_queue",
                         kwargs={"item_hash_name": kwargs.get("steamName")})
    return kwargs
