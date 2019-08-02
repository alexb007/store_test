from StoreTest.celery import app
from store.api_calls import create_order_call, delete_order_call


@app.task
def create_order(order):
    print('calling api')
    create_order_call(order)


@app.task
def delete_order(order_id):
    print('calling delete api')
    delete_order_call(order_id)
