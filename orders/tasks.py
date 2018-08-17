# coding: utf-8
from celery import task
from django.core.mail import send_mail
from .models import Order
from myshop import settings


@task()
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    title = '订单信息. {}'.format(order.id)
    message = ('尊敬的{}先生,\n\n您已成功完成了订单. 您的订单号为{}.'.format(order.first_name, order.id)).decode('utf-8')
    mail_sent = send_mail(title, message, settings.EMAIL_FROM, [order.email])
    return mail_sent
