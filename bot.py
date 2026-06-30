import os
import logging

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

import yfinance as yf

from config.settings import settings

from handlers.general import hello,help
from handlers.finance import Harga_Dollar, Harga_IHSG, Harga_SPX, Harga_BBCA, Harga_BBRI, Harga_BREN

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Bot...")


    app = ApplicationBuilder().token(settings.TOKEN).build()

    app.add_handler(CommandHandler("Hello", hello))
    app.add_handler(CommandHandler("Help", help))
    app.add_handler(CommandHandler("Harga_USD", Harga_Dollar))
    app.add_handler(CommandHandler("Harga_IHSG", Harga_IHSG))
    app.add_handler(CommandHandler("Harga_SPX", Harga_SPX))
    app.add_handler(CommandHandler("Harga_BBCA", Harga_BBCA))
    app.add_handler(CommandHandler("Harga_BBRI", Harga_BBRI))
    app.add_handler(CommandHandler("Harga_BREN", Harga_BREN))

    app.run_polling()

if __name__ == "__main__":
    main()
