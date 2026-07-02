from bot.constants import OrderType
from bot.exceptions import ValidationException


def validate_order(order):
    if order.order_type == OrderType.LIMIT:
        if order.price is None:
            raise ValidationException("LIMIT order requires price.")

    if order.order_type == OrderType.STOP_LIMIT:
        if order.price is None:
            raise ValidationException("STOP_LIMIT requires price.")

        if order.stop_price is None:
            raise ValidationException("STOP_LIMIT requires stop price.")
