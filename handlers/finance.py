import logging

from telegram import Update
from telegram.ext import ContextTypes

from utils.finance import get_ticker_latest_price

logger = logging.getLogger(__name__)

TICKER_USD_IDR = "IDR=X"
TICKER_IHSG = "^JKSE"
TICKER_SPX = "^GSPC"

async def Harga_Dollar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    harga_dollar_IDR = get_ticker_latest_price(TICKER_USD_IDR)
    await update.message.reply_text(f"USD to IDR : Rp {harga_dollar_IDR:,.2f}")
    
async def Harga_IHSG(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    harga_IHSG = get_ticker_latest_price(TICKER_IHSG)
    await update.message.reply_text(f"Harga IHSG : Rp {harga_IHSG:,.2f}")
    
async def Harga_SPX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    harga_SPX_USD = get_ticker_latest_price(TICKER_IHSG)
    harga_dollar_IDR = get_ticker_latest_price(TICKER_USD_IDR)
    harga_SPX_IDR = harga_SPX_USD * harga_dollar_IDR
    await update.message.reply_text(f"S&P 500 USD : $ {harga_SPX_USD:,.2f}\n"
                                    f"S&P 500 IDR : Rp {harga_SPX_IDR:,.2f}\n")