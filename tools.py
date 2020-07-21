'''
Данный файл содержит ряд полезных инструментов, не относящихся напрямую к логике некоторых модулей,
но необходимых для решения некоторых задач в них. Для того, чтобы не загромождать код модулей,
данные инструменты вынесены в этот отдельный файл.


СПИСОК ИНСТРУМЕНТОВ:
-----------------------------------------------------------------------------
> полное_имя_типа
    Получает:       список типов и код имеющегося элемента
    Возвращает:     полное наименование типа, соответствующего данному коду
    Использован в:  ЗАПИСЬ.models,
-----------------------------------------------------------------------------
> склонение_слова
    Получает:       слово и падеж, в который его нужно склонить
    Возвращает:     слово в заданном падеже
    Использован в:  -
-----------------------------------------------------------------------------

'''

from pymorphy2 import MorphAnalyzer
import requests
from urllib.request import urlretrieve
import xlrd

def полное_имя_типа(список_типов, код_типа):
    for группа in список_типов:
        for пара_код_имя in группа[1]:
            if пара_код_имя[0] == код_типа:
                return пара_код_имя[1]
    return None


def склонение_слова(слово, падеж):
    падежи = ("именительный",
              "родительный",
              "дательный",
              "винительный",
              "творительный",
              "предложный",
              "звательный",)

    кодировки_падежей = ("nomn", "gent", "datv", "accs", "ablt", "loct", "voct")

    анализатор = MorphAnalyzer()

    индекс_падежа = падежи.index(падеж)
    код_падежа = кодировки_падежей[индекс_падежа]
    return анализатор.parse(str(слово))[0].inflect({код_падежа}).word


def получение_таблицы_УБИ():
    url = 'https://bdu.fstec.ru/files/documents/thrlist.xlsx'
    r = requests.get(url)  # make an HTTP request

    workbook = xlrd.open_workbook(file_contents=r.content)  # open workbook
    worksheet = workbook.sheet_by_index(0)  # get first sheet
    first_row = worksheet.row(0)  # you can iterate over rows of a worksheet as well

    print(first_row)  # list of cells

получение_таблицы_УБИ()