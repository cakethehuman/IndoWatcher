import logging
import yfinance as yf

logger = logging.getLogger(__name__)

def get_ticker_latest_price(name : str) -> float | None:
    try:
        ticker = yf.Ticker(name)
        price = ticker.info.get('regularMarketPrice')
        return price
    except Exception as e:
        logger.error(f"Failed to get {name} price because {e}")
        return;