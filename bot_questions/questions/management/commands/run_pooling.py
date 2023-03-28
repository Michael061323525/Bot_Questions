from django.core.management.base import BaseCommand, CommandError
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from questions.handlers_bot.start import start
from django.conf import settings


class Command(BaseCommand):
    help = 'Запускает телеграм бота'

    def handle(self, *args, **options):
        app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", start))

        app.run_polling()
