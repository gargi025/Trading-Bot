# Binance Futures Trading Bot

A Python CLI application for placing orders on the Binance USDT-M Futures Testnet.

## Features

- Market Orders
- Limit Orders
- Stop Orders (Bonus)
- BUY and SELL support
- Interactive CLI using Typer & Rich
- Input validation using Pydantic
- Structured logging
- Configurable environment variables
- Modular architecture

---

## Project Structure

```
Trading-Bot/
│
├── bot/
│   ├── client.py
│   ├── config.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── models.py
│   ├── orders.py
│
├── logs/
├── tests/
│
├── cli.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Installation

```bash
git clone <repository-url>

cd Trading-Bot

pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_SECRET
BINANCE_BASE_URL=https://testnet.binancefuture.com
```

---

## Run

```bash
python cli.py
```

---

## Example Flow

```
Enter Symbol
BTCUSDT

Side
BUY

Order Type
MARKET

Quantity
0.01
```

---

## Logging

Logs are stored in:

```
logs/trading.log
```

Every request and response is logged.

---

## Validation

The application validates:

- Symbol
- Quantity > 0
- Price required for Limit orders
- Stop Price required for Stop orders

---

## Assumptions

- Binance Futures Testnet credentials are required.
- The Binance endpoint is configurable through environment variables.
- The application uses direct REST API calls via `httpx`.

---

## Bonus Features

- Interactive CLI
- Stop Order support