from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from .models import Book
import os

@shared_task
def send_email_task():
    print("TASK_INTERVAL:", os.getenv('TASK_INTERVAL'))
    interval_minutes = int(settings.TASK_INTERVAL)

    now = datetime.now()
    time_threshold = now - timedelta(minutes=interval_minutes)

    recent_books = Book.objects.filter(is_created__gte=time_threshold)

    if recent_books.exists():
        subject = f"Новые книги за последние {interval_minutes} минут"
        message = "Вот список книг, добавленных недавно:\n\n"

        for book in recent_books:
            message += f"- {book.title} (Автор: {book.author}, Страниц: {book.page_count}, Дата публикации: {book.publication_date})\n"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECIPIENT],
            fail_silently=False,
        )
    else:
        print("Новых книг за указанный интервал нет.")

@shared_task
def test_task():
    print("Celery работает!")
    return "Hello from Celery!"