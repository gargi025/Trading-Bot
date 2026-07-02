from pydantic import BaseModel, field_validator
from typing import Optional

from bot.constants import Side, OrderType


class OrderRequest(BaseModel):
    symbol: str
    side: Side
    order_type: OrderType
    quantity: float
    price: Optional[float] = None
    stop_price: Optional[float] = None

    @field_validator("symbol")
    @classmethod
    def uppercase_symbol(cls, value):
        return value.upper()

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, value):
        if value <= 0:
            raise ValueError("Quantity must be positive")
        return value