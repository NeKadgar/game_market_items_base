from background.celery_app import app
from services.csmoney import DotaDataProcessor


@app.task(name="update_items_base", queue="items_base_queue")
def update_items_base(**kwargs):
    # test commit
    DotaDataProcessor.update(kwargs)
    return kwargs
