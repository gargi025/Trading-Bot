from bot.client import BinanceClient
from bot.constants import OrderType
from bot.logging_config import logger
from bot.models import OrderRequest


class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def place_order(self, order: OrderRequest) -> dict:
        logger.info(f"Processing {order.order_type.value} order for {order.symbol}")

        if order.order_type == OrderType.MARKET:
            return self.client.place_market_order(
                symbol=order.symbol,
                side=order.side.value,
                quantity=order.quantity,
            )

        elif order.order_type == OrderType.LIMIT:
            return self.client.place_limit_order(
                symbol=order.symbol,
                side=order.side.value,
                quantity=order.quantity,
                price=order.price,
            )

        elif order.order_type == OrderType.STOP:
            return self.client.place_stop_order(
                symbol=order.symbol,
                side=order.side.value,
                quantity=order.quantity,
                price=order.price,
                stop_price=order.stop_price,
            )

        raise ValueError(f"Unsupported order type: {order.order_type}")
