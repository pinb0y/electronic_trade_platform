# Generated by Django 5.1.5 on 2025-01-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_trade', '0003_alter_product_supplier_alter_supplier_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Укажите сумму долга с копейками', max_digits=12, verbose_name='Сумма долга с копейками'),
        ),
    ]
