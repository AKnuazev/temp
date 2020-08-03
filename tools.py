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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    # can get this info by navigator.userAgent in chrome developer console

    return requests.get(url, headers=headers)  # make an HTTP request


def обработка_таблицы_УБИ(got_request):
    workbook = xlrd.open_workbook(file_contents=got_request.content)
    worksheet = workbook.sheet_by_index(0)

    таблица_УБИ = []
    for индекс_строки in range(2, worksheet.nrows):
        строка = worksheet.row_values(индекс_строки)
        таблица_УБИ.append(
            Угроза(идентификатор=int(строка[0]),
                   наименование=строка[1],
                   описание=строка[2],
                   источник=строка[3],
                   цель=строка[4],
                   последствия=[строка[5], строка[6], строка[7]]))

    return таблица_УБИ


class Угроза:
    def __init__(self, идентификатор, наименование, описание, источник, цель, последствия):
        self.идентификатор = идентификатор
        self.наименование = наименование
        self.описание = описание
        self.источник = источник
        self.цель = цель
        self.последствия = последствия

    def __str__(self):
        return str(self.наименование)


class Изделие:
    def __init__(self, наименование):
        self.наименование = наименование
        self.угрозы = []

    def __str__(self):
        output = self.наименование

        for угроза in self.угрозы:
            output += '\n' + "  - " + str(угроза)

        return output

    def проверить_наличие_в_списке(self, список, угроза):
        for изделие in список:
            if изделие.наименование == self.наименование:
                изделие.угрозы.append(угроза)
                return True
        return False


def фильтрация_по_изделиям(таблица_УБИ):
    список_изделий = []

    for угроза in таблица_УБИ:
        изделие = Изделие(наименование=угроза.цель)
        проверка = изделие.проверить_наличие_в_списке(список_изделий, угроза)
        if not проверка:
            изделие.угрозы.append(угроза)
            список_изделий.append(изделие)
        del изделие
    return список_изделий

def получить_таблицу_изделий():
    return фильтрация_по_изделиям(обработка_таблицы_УБИ(получение_таблицы_УБИ()))
