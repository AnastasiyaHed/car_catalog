from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .models import CarPurchase
import asyncio
import telegram
from django.conf import settings

@receiver(post_save, sender=CarPurchase)
def send_telegram_notification(sender, instance, **kwargs):
    if kwargs.get('created', False):  # Отправляем уведомление только при создании объекта
        car_info = f"Car: {instance.car.year} {instance.car.make} {instance.car.model}\n"
        buyer_info = f"Buyer: {instance.buyer.username}\n"
        message = f"New car purchase:\n{car_info}{buyer_info}Ready for pickup within 3 days."

        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID

        try:
            bot = telegram.Bot(token=bot_token)
            bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            print(f"Telegram notification failed. Error: {e}")