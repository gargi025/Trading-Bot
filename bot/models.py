from typing import Optional

from pydantic import BaseModel, field_validator, model_validator

from bot.constants import OrderType, Side


class OrderRequest(BaseModel):
    symbol: str
    side: Side
    order_type: OrderType
    quantity: float
    price: Optional[float] = None
    stop_price: Optional[float] = None

    @field_validator("symbol")
    @classmethod
    def validate_symbol(cls, value: str):
        value = value.upper().strip()

        if len(value) < 6:
            raise ValueError("Invalid symbol")

        return value

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, value: float):
        if value <= 0:
            raise ValueError("Quantity must be greater than 0")
        return value

    @field_validator("price")
    @classmethod
    def validate_price(cls, value):
        if value is not None and value <= 0:
            raise ValueError("Price must be greater than 0")
        return value

    @field_validator("stop_price")
    @classmethod
    def validate_stop_price(cls, value):
        if value is not None and value <= 0:
            raise ValueError("Stop price must be greater than 0")
        return value

    @model_validator(mode="after")
    def validate_order(self):
        if self.order_type == OrderType.LIMIT and self.price is None:
            raise ValueError("LIMIT orders require a price.")

        if self.order_type == OrderType.STOP_LIMIT:
            if self.price is None:
                raise ValueError("STOP_LIMIT orders require a price.")

            if self.stop_price is None:
                raise ValueError("STOP_LIMIT orders require a stop price.")

        return self
