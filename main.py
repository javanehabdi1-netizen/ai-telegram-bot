import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# تنظیمات لاگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"سلام {user_name} عزیز! 🌟\n\n"
        "به دستیار هوشمند هوش مصنوعی (Smart AI Assistant) خوش آمدید.\n"
        "من اینجا هستم تا به تمام سوالات شما پاسخ دهم و در تولید محتوا کمکتان کنم.\n\n"
        "کافیه پیام یا سوالت رو برام بفرستی!"
    )
    await update.message.reply_text(welcome_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    # پاسخ هوشمند اولیه (قابل اتصال به مدل‌های AI پیشرفته)
    response = f"🤖 پیام شما دریافت شد:\n\n«{user_text}»\n\nدر حال پردازش و پاسخگویی با هوش مصنوعی..."
    await update.message.reply_text(response)

if __name__ == '__main__':
    if not TOKEN:
        print("خطا: توکن تلگرام یافت نشد!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        print("ربات با موفقیت روشن شد...")
        app.run_polling()
