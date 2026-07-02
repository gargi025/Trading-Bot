import pytest

from bot.models import OrderRequest
from bot.constants import Side, OrderType


def test_market_order_creation():
    order = OrderRequest(
        symbol="BTCUSDT",
        side=Side.BUY,
        order_type=OrderType.MARKET,
        quantity=0.01,
    )

    assert order.symbol == "BTCUSDT"
