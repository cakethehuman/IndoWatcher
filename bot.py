import os

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import yfinance as yf



load_dotenv()
TOKEN = os.getenv('TOKEN')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def Harga_Dollar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ticker = yf.Ticker("IDR=X")
    harga_dollar_idr = ticker.info.get('regularMarketPrice')
    await update.message.reply_text(f"USD to IDR : Rp {harga_dollar_idr:,.2f}")
    
async def Harga_IHSG(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ticker = yf.Ticker("^JKSE")
    harga_IHSG = ticker.info.get('regularMarketPrice')
    await update.message.reply_text(f"USD to IDR : Rp {harga_IHSG:,.2f}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("Harga_Dollar", Harga_Dollar))
app.add_handler(CommandHandler("Harga_IHSG", Harga_IHSG))
# app.add_handler(CommandHandler("Harga_IHSG_Dollar", Harga_Dollar))


app.run_polling()