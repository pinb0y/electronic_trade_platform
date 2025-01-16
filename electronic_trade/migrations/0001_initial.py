# Generated by Django 5.1.5 on 2025-01-15 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название поставщика', max_length=250, verbose_name='Название')),
                ('supplier_type', models.PositiveSmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0, help_text='Укажите тип поставщика', verbose_name='Тип поставщика')),
                ('debt', models.DecimalField(decimal_places=2, help_text='Укажите сумму долга с копейками', max_digits=12, verbose_name='Сумма долга с копейками')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('supplier', models.ForeignKey(help_text='Укажите связанного поставщика предыдущего по иерархии', on_delete=django.db.models.deletion.DO_NOTHING, related_name='suppliers', to='electronic_trade.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название продукта', max_length=200, verbose_name='Название')),
                ('model', models.CharField(help_text='Укажите модель', max_length=100, verbose_name='Модель')),
                ('release_date', models.DateField(help_text='Укажите дату выхода продукта на рынок', verbose_name='Дата выхода продукта на рынок')),
                ('supplier', models.ManyToManyField(help_text='Укажите поставщика', related_name='products', to='electronic_trade.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Укажите электронную почту', max_length=250, verbose_name='Электронная почта')),
                ('country', models.CharField(help_text='Укажите страну', max_length=150, verbose_name='Страна')),
                ('city', models.CharField(help_text='Укажите город', max_length=150, verbose_name='Город')),
                ('street', models.CharField(help_text='Укажите улицу', max_length=250, verbose_name='улица')),
                ('street_number', models.CharField(help_text='Укажите номер дома', max_length=30, verbose_name='Номер дома')),
                ('supplier', models.OneToOneField(help_text='Укажите поставщика', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='electronic_trade.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
