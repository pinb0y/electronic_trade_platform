# Generated by Django 5.1.5 on 2025-01-15 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_trade', '0002_alter_product_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(help_text='Укажите поставщика', related_name='products', to='electronic_trade.supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier',
            field=models.ForeignKey(blank=True, help_text='Укажите связанного поставщика предыдущего по иерархии', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='suppliers', to='electronic_trade.supplier', verbose_name='Поставщик'),
        ),
    ]
