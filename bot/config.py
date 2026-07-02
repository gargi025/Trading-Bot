from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")

    BASE_URL = os.getenv("BINANCE_BASE_URL", "https://testnet.binancefuture.com")

    RECV_WINDOW = 5000
    TIMEOUT = 15
