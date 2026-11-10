# AI-Powered Market Analysis & Strategy Builder

A local market-analysis API that calculates common technical indicators from supplied OHLCV candles and performs a transparent keyword sentiment baseline over supplied headlines. It does not place trades, fetch private broker data or provide investment advice.

## Run
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
POST /analyze with a `candles` array containing `close` values and optional headlines. No broker credentials or paid APIs are required.
