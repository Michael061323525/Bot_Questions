from django.core.management.base import BaseCommand, CommandError
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from questions.handlers_bot.start import start

class Command(BaseCommand):
    help = 'Запускает телеграм бота'

    def handle(self, *args, **options):
        app = ApplicationBuilder().token("6271624941:AAGU0M2U4dKEyv2IztLJaODwJJ7XGc1bZGc").build()

        app.add_handler(CommandHandler("start", start))

        app.run_polling()
