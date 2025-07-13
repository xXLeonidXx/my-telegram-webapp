from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

WEB_APP_URL = 'https://68735c85022e411b5afb565a--dulcet-seahorse-35957b.netlify.app/'  # ссылка на твой миниапп

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "Запустить миниапп",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажми кнопку, чтобы открыть миниапп:", reply_markup=reply_markup)

if __name__ == '__main__':
    TOKEN = '8127229834:AAG3HNIUdUGIe-ZViB5rHkdhjs7437VLxbE'

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()
