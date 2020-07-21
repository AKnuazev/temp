from django.db import models

# Create your models here.
class ОБЪЕКТ(models.Model):
    имя = models.CharField(max_length=150)
    значение = models.CharField(max_length=50)
    минимум = models.CharField(max_length=50, blank=True, null=True)
    максимум = models.CharField(max_length=50, blank=True, null=True)
    единицы_измерения = models.CharField(max_length=50, blank=True, null=True)
    рисунок = models.ImageField(blank=True, null=True)
    подпись = models.CharField(max_length=150, blank=True, null=True)
    текст = models.TextField(blank=True, null=True)
    примечание = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'объекты'

    def __str__(self):
        return 'ИМЯ: ' + self.имя + 'ЗНАЧЕНИЕ: ' + self.значение


class ЗАПИСЬ(models.Model):
    '''
    Описание аббревиатур класса:
        Рассматривается пространственная фигура в виде куба.
        Каждая плоскость куба (всего шесть плоскосей) именуются:
            Ф - фасад (передняя плоскость);
            Т - тыл (задняя плоскость относительно наблюдателя);
            Л - левая плоскость;
            П - правая плоскость;
            Н - нижняя плоскость;
            В - верхняя плоскость;
        Пересечения плоскостей формируют рёбра. Общее количество рёбер - 12
        Каждое ребро имеет три точки привязки - начало; центр; конец.
        Аббревиатуры точек привязок рёбер плоскостей куба формируются по принципу
        "от сложного к простому" - Плоскость -> Линия -> Точка:
            ФВЛ - точка, расположенная слева верхнего угла фасадной плоскости;
            ФВЦ - точка, расположенная в центре верхнего ребра фасадной плоскости;
            ФВП - точка, расположенная справа верхнего ребра фасадной плоскости;
            ФЛЦ - точка, расположенная в центре левого ребра фасадной плоскости;
            ФЦ - точка, расположенная в центре фасадной плоскости;
            ФПЦ - точка, расположенная в центре правого ребра фасадной плоскости;
            ФНЛ - точка, расположенная слева нижнего угла фасадной плоскости;
            ФНЦ - точка, расположенная в центре нижнего ребра фасадной плоскости;
            ФНП - точка, расположенная справа нижнего ребра фасадной плоскости;
            ПВЦ - точка, расположенная в центре ребра правой плоскости, расположенного сверху;
            ВЦ - точка, расположенная в центре верхней плоскости;
            ЛВЦ - точка в центре верхнего ребра левой плоскости;
            ПЦ - центральная точка правой плоскости;
            ЛЦ - центральная точка левой плоскости;
            ПНЦ - центральная точка нижнего ребра правой плоскости;
            НЦ - центральная точка нижней плоскости;
            ЛНЦ - центральная точка нижнего ребра левой плоскости;
            ПВТ - точка пересечения правой, верхней и тыльной плоскостей;
            ПТЦ - центральная точка ребра, сформированного пересечением правой и тыльной плоскостей;
            ПНТ - точка пересечения правой, нижней и тыльной плоскостей;
            ВТЦ - центральная точка ребра, сформированного верхней и тыльной плоскостями;
            ТЦ - центральная точка тыльной плоскости;
            НТЦ - центральная точка ребра, сформированного нижней и тыльной плоскостями;
            ЛВТ - точка пересечения левой, верхней и тыльной плоскостей;
            ЛТЦ - центральная точка ребра, сформированного левой и тыльной плоскостями;
            ЛНТ - точка пересечения левой, нижней и тыльной плоскостей;
        Общее количество точек привязки - 26
        Поскольку точки рёбер относительно плоскостей могут иметь два (для центра ребра)
        или три (для концевых точек ребра) названия, имеющие одну суть (технические синонимы),
        основополагающим по значимости считается ФАСАД. Т.е. для центральной точки ребра,
        сформированного плоскостями ФАСАД и ПРАВО название точки относительно фасада (ФПЦ)
        будет основным. Следом, равные по значимости ПРАВО (правая плоскость относительно
        наблюдателя, который смотрит прямо на фасад) и ЛЕВО. Следом ВЕРХ и НИЗ. Далее ТЫЛ.

    Для линейного взаимодействия между объектами используются:
        - ПЦ
        - ЛЦ
    Для плоского взаимодействия используются:
        - ПЦ
        - ПВЦ
        - ВЦ
        - ЛВЦ
        - ЛЦ
        - ЛНЦ
        - НЦ
        - ПНЦ
    Для пространственного взаимодействия используются комбинации всех 26 точек
    '''

    типы = (
        ('Заголовки', (
            ('РА', 'Раздел'),
            ('ПР', 'Подраздел'),
        )),
        ('Текст', (
            ('ТТ', 'Текст'),
            ('АБ', 'Абзац'),
            ('ПТ', 'Пункт'),
            ('ПП', 'Подпункт'),
        )),
        ('Перечисления', (
            ('ДЕ', 'Дефис'),
            ('БУ', 'Буква'),
            ('ЦИ', 'Цифра'),
        )),
        ('Объекты', (
            ('ТБ', 'Таблица'),
            ('РИ', 'Рисунок'),
            ('ЧЕ', 'Чертёж'),
            ('СХ', 'Схема'),
        )),
    )
    тип = models.CharField(max_length=2, choices=типы)
    # проект = models.ForeignKey(ПРОЕКТ, on_delete=models.CASCADE)
    # документ = models.ForeignKey(ДОКУМЕНТ, on_delete=models.CASCADE)
    содержательная_часть = models.CharField(max_length=10)

    ФВЛ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФВЛ', blank=True, null=True)
    ФВЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФВЦ', blank=True, null=True)
    ФВП = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФВП', blank=True, null=True)
    ФЛЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФЛЦ', blank=True, null=True)
    ФЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФЦ', blank=True, null=True)
    ФПЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФПЦ', blank=True, null=True)
    ФНЛ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФНЛ', blank=True, null=True)
    ФНЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФНЦ', blank=True, null=True)
    ФНП = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ФНП', blank=True, null=True)
    ПВЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ПВЦ', blank=True, null=True)
    ВЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ВЦ', blank=True, null=True)
    ЛВЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ЛВЦ', blank=True, null=True)
    ПЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ПЦ', blank=True, null=True)
    ЛЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ЛЦ', blank=True, null=True)
    ПНЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ПНЦ', blank=True, null=True)
    НЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_НЦ', blank=True, null=True)
    ЛНЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ЛНЦ', blank=True, null=True)
    ПВТ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ПВТ', blank=True, null=True)
    ПТЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ПТЦ', blank=True, null=True)
    ПНТ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ПНТ', blank=True, null=True)
    ВТЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ВТЦ', blank=True, null=True)
    ТЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ТЦ', blank=True, null=True)
    НТЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_НТЦ', blank=True, null=True)
    ЛВТ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ЛВТ', blank=True, null=True)
    ЛТЦ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ЛТЦ', blank=True, null=True)
    ЛНТ = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE, related_name='точка_ЛНТ', blank=True, null=True)
    объект = models.ForeignKey(ОБЪЕКТ, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def __str__(self):
        return self.тип + ' | '  # + self.проект + ' | ' + self.документ
