# Binance Futures Trading Bot

## Features

- Market Orders
- Limit Orders
- Stop Orders (Bonus)
- Interactive CLI
- Pydantic Validation
- Rich Terminal UI
- Structured Logging
- Configurable Environment

## Setup

pip install -r requirements.txt

## Configure

Create a .env file

BINANCE_API_KEY=...
BINANCE_API_SECRET=...
BINANCE_BASE_URL=https://testnet.binancefuture.com

## Run

python cli.py

## Project Structure

(bot folder tree)

## Assumptions

- Uses Binance Futures Testnet endpoint.
- Endpoint is configurable.
- Requires valid Testnet credentials.

## Bonus

- Interactive Rich CLI
- Stop Order Support