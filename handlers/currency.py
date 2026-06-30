import logging

from telegram import Update
from telegram.ext import ContextTypes

from utils.finance import get_ticker_latest_price

logger = logging.getLogger(__name__)

TICKER_USD_IDR = "IDR=X"

async def Harga_Dollar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    harga_dollar_IDR = get_ticker_latest_price(TICKER_USD_IDR)
    await update.message.reply_text(f"USD to IDR : Rp {harga_dollar_IDR:,.2f}")