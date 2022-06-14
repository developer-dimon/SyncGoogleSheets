from datetime import datetime

import httplib2
import requests
from django.conf import settings
from django.db import transaction
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from rest_framework.exceptions import ValidationError

from synchronization.models import Order


def get_service_sacc():
    creds = ServiceAccountCredentials.from_json_keyfile_name(settings.GOOGLE_CREDENTIALS_FILE, settings.SCOPES) \
        .authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds)


def get_orders() -> list[list]:
    try:
        sheet = get_service_sacc().spreadsheets()
        return sheet.values().get(
            spreadsheetId=settings.SAMPLE_SPREADSHEET_ID,
            range=settings.SAMPLE_RANGE_NAME
        ).execute().get('values', [])
    except Exception as exc:
        ValidationError(f'Сервис Google недоступен: {exc}')


def get_dollar_rate():
    try:
        return float(requests.get(settings.API_CB).json()['Valute']['USD']['Value'])
    except Exception as exc:
        ValidationError(f'Сервис ЦБ не доступен: {exc}')


def create_list_orders() -> list[Order]:
    dollar_rate = get_dollar_rate()
    new_orders = []
    for _id, order_number, price_dollars, delivery_date in get_orders()[1:]:
        new_orders.append(
            Order(
                order_number=int(order_number),
                price_dollars=float(price_dollars),
                price_rubles=float(price_dollars) * dollar_rate,
                delivery_date=datetime.strptime(delivery_date, '%d.%m.%Y')
            )
        )
    return new_orders


def update_orders_db():
    try:
        with transaction.atomic():
            Order.objects.all().delete()
            Order.objects.bulk_create(create_list_orders())
    except Exception as exc:
        ValidationError(f'Не удалось обновить данные {exc}')
