import logging
from telegram import Update
from telegram.ext import ContextTypes
 
logger = logging.getLogger(__name__)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logging.info(f"/hello command was used by : {user.id}")
    await update.message.reply_text(
        f"👋 Halo user {user.first_name}\n"
        "User /help to view the commands : \n"
    )
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logging.info(f"/help command was used by : {user.id}")
    await update.message.reply_text(
        "Commands : \n"
        "/Harga_USD — Harga USD to IDR\n"
        "/harga_IHSG — Harga IHSG\n"
        "/Harga_SPX - Harga S&p 500\n"
        "/Harga_BBCA - Harga saham BBCA\n"
        "/Harga_BBRI - Harga saham BBRI\n"
        "/Harga_BREN - Harga saham BREN\n"
    )