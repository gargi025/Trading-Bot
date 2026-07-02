from bot.models import OrderRequest
from bot.orders import OrderService
from bot.constants import Side, OrderType

order = OrderRequest(
    symbol="BTCUSDT",
    side=Side.BUY,
    order_type=OrderType.MARKET,
    quantity=0.001,
)

service = OrderService()

print(service.place_order(order))
