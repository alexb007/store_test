import json

from store.serializers import OrderSerializer
from store.tasks import create_order, delete_order


def order_saved_handler(sender, instance, created, **kwargs):
    if created and sender:
        try:
            order = OrderSerializer(instance).data
            create_order.apply_async(args=(order,))
        except Exception as ex:
            print(ex)


def order_deleted_handler(sender, instance, **kwargs):
    delete_order.apply_async(args=(instance.id, ))

