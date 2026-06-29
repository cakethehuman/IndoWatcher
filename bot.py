import os
import logging

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

import yfinance as yf

from config.settings import settings

from handlers.general import hello
from handlers.finance import Harga_Dollar, Harga_IHSG, Harga_SPX

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Bot...")


    app = ApplicationBuilder().token(settings.TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("Harga_USD", Harga_Dollar))
    app.add_handler(CommandHandler("Harga_IHSG", Harga_IHSG))
    app.add_handler(CommandHandler("Harga_SPX", Harga_SPX))

    app.run_polling()

if __name__ == "__main__":
    main()
