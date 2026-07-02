import hashlib
import hmac
import time
from typing import Any

import httpx
from urllib.parse import urlencode

from bot.config import Config
from bot.logging_config import logger


class BinanceClient:
    def __init__(self) -> None:
        if not Config.API_KEY or not Config.API_SECRET:
            raise ValueError(
                "Binance API credentials are missing. "
                "Please configure BINANCE_API_KEY and BINANCE_API_SECRET in your .env file."
            )

        self.base_url = Config.BASE_URL
        self.api_key = Config.API_KEY
        self.secret = Config.API_SECRET.encode()

        self.client = httpx.Client(
            timeout=Config.TIMEOUT,
            headers={
                "X-MBX-APIKEY": self.api_key
            },
        )

        logger.info(f"Using Binance endpoint: {self.base_url}")

    def _sign(self, params: dict[str, Any]) -> dict[str, Any]:
        query = urlencode(params)

        signature = hmac.new(
            self.secret,
            query.encode(),
            hashlib.sha256,
        ).hexdigest()

        params["signature"] = signature
        return params

    def _handle_response(self, response: httpx.Response) -> dict:
        try:
            data = response.json()
        except Exception:
            logger.error(f"Invalid response from Binance:\n{response.text}")
            raise

        if response.is_success:
            logger.success("Request completed successfully.")
        else:
            logger.error(
                f"Binance Error [{response.status_code}]: {data}"
            )

        return data

    def get_server_time(self) -> dict:
        url = f"{self.base_url}/fapi/v1/time"

        response = self.client.get(url)

        response.raise_for_status()

        return self._handle_response(response)

    def get_account(self) -> dict:
        params = {
            "timestamp": int(time.time() * 1000),
        }

        params = self._sign(params)

        response = self.client.get(
            f"{self.base_url}/fapi/v2/account",
            params=params,
        )

        return self._handle_response(response)

    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
    ) -> dict:

        logger.info(
            f"Placing MARKET order | Symbol={symbol} | Side={side} | Qty={quantity}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "timestamp": int(time.time() * 1000),
        }

        params = self._sign(params)

        response = self.client.post(
            f"{self.base_url}/fapi/v1/order",
            data=params,
        )

        return self._handle_response(response)

    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
    ) -> dict:

        logger.info(
            f"Placing LIMIT order | Symbol={symbol} | Side={side} | Qty={quantity} | Price={price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "quantity": quantity,
            "price": price,
            "timeInForce": "GTC",
            "timestamp": int(time.time() * 1000),
        }

        params = self._sign(params)

        response = self.client.post(
            f"{self.base_url}/fapi/v1/order",
            data=params,
        )

        return self._handle_response(response)

    def place_stop_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
        stop_price: float,
    ) -> dict:

        logger.info(
            f"Placing STOP order | Symbol={symbol} | Side={side} | Qty={quantity} | Stop={stop_price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": "STOP",
            "quantity": quantity,
            "price": price,
            "stopPrice": stop_price,
            "timeInForce": "GTC",
            "timestamp": int(time.time() * 1000),
        }

        params = self._sign(params)

        response = self.client.post(
            f"{self.base_url}/fapi/v1/order",
            data=params,
        )

        return self._handle_response(response)

    def close(self) -> None:
        self.client.close()