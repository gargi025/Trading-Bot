class ValidationException(Exception):
    """Raised when user input is invalid."""
    pass


class BinanceClientException(Exception):
    """Raised when Binance API returns an error."""
    pass