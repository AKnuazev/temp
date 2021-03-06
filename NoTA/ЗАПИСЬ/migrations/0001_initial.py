# Generated by Django 3.0.8 on 2020-07-15 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ОБЪЕКТ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('имя', models.CharField(max_length=150)),
                ('значение', models.CharField(max_length=50)),
                ('минимум', models.CharField(blank=True, max_length=50, null=True)),
                ('максимум', models.CharField(blank=True, max_length=50, null=True)),
                ('единицы_измерения', models.CharField(blank=True, max_length=50, null=True)),
                ('рисунок', models.ImageField(blank=True, null=True, upload_to='')),
                ('подпись', models.CharField(blank=True, max_length=150, null=True)),
                ('текст', models.TextField(blank=True, null=True)),
                ('примечание', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'объект',
                'verbose_name_plural': 'объекты',
            },
        ),
        migrations.CreateModel(
            name='ЗАПИСЬ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('тип', models.CharField(choices=[('Заголовки', (('РА', 'Раздел'), ('ПР', 'Подраздел'))), ('Текст', (('ТТ', 'Текст'), ('АБ', 'Абзац'), ('ПТ', 'Пункт'), ('ПП', 'Подпункт'))), ('Перечисления', (('ДЕ', 'Дефис'), ('БУ', 'Буква'), ('ЦИ', 'Цифра'))), ('Объекты', (('ТБ', 'Таблица'), ('РИ', 'Рисунок'), ('ЧЕ', 'Чертёж'), ('СХ', 'Схема')))], max_length=2)),
                ('содержательная_часть', models.CharField(max_length=10)),
                ('ВТЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ВТЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ВЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ВЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ЛВТ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ЛВТ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ЛВЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ЛВЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ЛНТ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ЛНТ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ЛНЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ЛНЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ЛТЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ЛТЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ЛЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ЛЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('НТЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_НТЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('НЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_НЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ПВТ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ПВТ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ПВЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ПВЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ПНТ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ПНТ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ПНЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ПНЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ПТЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ПТЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ПЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ПЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ТЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ТЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФВЛ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФВЛ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФВП', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФВП', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФВЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФВЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФЛЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФЛЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФНЛ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФНЛ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФНП', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФНП', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФНЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФНЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФПЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФПЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('ФЦ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='точка_ФЦ', to='ЗАПИСЬ.ОБЪЕКТ')),
                ('объект', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ЗАПИСЬ.ОБЪЕКТ')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
