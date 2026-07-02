# Binance Futures Trading Bot

A Python CLI application for placing orders on the Binance USDT-M Futures Testnet.

## Features

- Place **Market Orders**
- Place **Limit Orders**
- Place **Stop Orders** *(Bonus)*
- BUY and SELL support
- Interactive CLI built with **Typer** and **Rich**
- Input validation using **Pydantic**
- Structured logging
- Environment-based configuration
- Modular architecture with separate client and service layers

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

## Architecture

```text
                CLI (Typer + Rich)
                       │
                       ▼
                Order Service
                       │
                       ▼
               Binance Client
                       │
                       ▼
           Binance REST API (HTTPX)
                       │
                       ▼
        Binance USDT-M Futures Testnet
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet API credentials

---

## Installation

```bash
git clone https://github.com/gargi025/Trading-Bot.git

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

## Example

```text
$ python cli.py

Enter Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.01

📋 Order Request Summary

Submit this order? y
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

- The application targets the Binance USDT-M Futures Testnet.
- The Binance endpoint is configurable using the `BINANCE_BASE_URL` environment variable.
- Valid Binance Testnet API credentials are required to successfully place orders.
- The application communicates directly with Binance using HTTPX and signed REST API requests.

## Note

The application is implemented against the Binance Futures Testnet endpoint specified in the assignment. Since the endpoint and Testnet credential availability may vary over time, the base URL is configurable through environment variables without requiring code changes.

---

## Bonus Features

- Interactive CLI
- Stop Order support