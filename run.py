from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from excel_parser import SNILS_ERROR_TEXT, get_message
from snils_chek import snils_chek
from dotenv import load_dotenv
import os


TOKEN = ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
            text=fr"Hi {user.mention_html()}!",
            # reply_markup=ForceReply(selective=True),
            )

async def send_data_from_snils(update: Update, context: ContextTypes.DEFAULT_TYPE):
    snils = snils_chek(update.message.text)
    if snils and len(snils) == 14:
        message = get_message(snils)
    else:
        message = SNILS_ERROR_TEXT    

    await update.message.reply_html(text=message)


def main() -> None:
    load_dotenv()
    TOKEN = str(os.getenv("BOT_TOKEN"))

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, callback=send_data_from_snils))

    app.run_polling()


if __name__ == "__main__":
    main()
