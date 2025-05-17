from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7915382996:AAEuSjAnSNZQ2sb4vgV1RGcthXH6fLo8XrM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📦 1688"], ["🛍 Taobao"], ["🎁 Pinduoduo"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Привет! Я помогу тебе зарегистрироваться на китайских площадках.\nВыбери нужную:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📦 1688":
        await update.message.reply_text("👉 Инструкция по регистрации на 1688: https://telegra.ph/Kak-zaregistrirovatsya-na-1688-04-01")
    elif text == "🛍 Taobao":
        await update.message.reply_text("👉 Инструкция по регистрации на Taobao: https://telegra.ph/Kak-zaregistrirovatsya-na-Taobao-04-01")
    elif text == "🎁 Pinduoduo":
        await update.message.reply_text("👉 Инструкция по регистрации на Pinduoduo: https://telegra.ph/Kak-zaregistrirovatsya-na-Pinduoduo-04-01")
    else:
        await update.message.reply_text("Пожалуйста, выбери площадку из меню ⬆️")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()
