from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №.{order_id}'
    message = f'Добрый день {order.first_name}, спасибо вам за заказ №{order_id}'
    mail_sent = send_mail(subject, message, 'admin@flowwow_sucks.com', [order.email])
    return mail_sent
