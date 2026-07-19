from django.http import HttpResponse, HttpResponseNotFound

import calendar

"""
Вьюха get_month_title_view возвращает название месяца по его номеру. 
Вся логика работы должна происходить в функции get_month_title_by_number.

Задания:
    1. Напишите логику получения названия месяца по его номеру в функции get_month_title_by_number
    2. Если месяца по номеру нет, то должен возвращаться ответ типа HttpResponseNotFound c любым сообщением об ошибке
    3. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/month-title/45 тут номер месяца/ 
       вызывалась вьюха get_month_title_view. Например http://127.0.0.1:8000/month-title/3 
"""


def get_month_title_by_number(month_number: int):
    try:

        return calendar.month_name[month_number]
    except:
        return False

def get_month_title_view(request, month_number: int):
    # код писать тут
    name_month = get_month_title_by_number(month_number)
    if name_month:
        return HttpResponse(name_month)
    return HttpResponseNotFound('Месяца с таким номером не существует')
