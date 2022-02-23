from decimal import Decimal
from background.celery_app import app as celery_app
from services.csmoney import DotaDataProcessor
from services.dota import DotaService


@celery_app.task(name="update_items_base", queue="items_base_queue")
def update_items_base(**kwargs):
    DotaDataProcessor.update(kwargs)
    celery_app.send_task(name="update_steam_items", queue="base_steam_queue",
                         kwargs={"item_hash_name": kwargs.get("steamName")})
    return kwargs


@celery_app.task(name="update_service_price", queue="items_base_queue")
def update_service_price(game_id: int, item_hash_name: str, price: Decimal, service: str):
    if game_id == 570:
        DotaService.update_service_price(item_hash_name=item_hash_name, price=price, service=service)
    elif game_id == 730:
        pass
    else:
        raise Exception("No such a game")
