from synchronization.celery import app
from synchronization.services import update_orders_db


@app.task
def periodic_update_orders():
    update_orders_db()
