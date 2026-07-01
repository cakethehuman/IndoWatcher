import logging
import yfinance as yf
from curl_cffi import requests
logger = logging.getLogger(__name__)
session = requests.Session(impersonate="chrome")
def get_ticker_latest_price(name : str) -> float | None:
    try:
        ticker = yf.Ticker(name, session=session)
        price = ticker.info.get('regularMarketPrice')
        return price
    except Exception as e:
        logger.error(f"Failed to get {name} price because {e}")
        return None