from django.db import models


class Supplier(models.Model):
    class SupplierType(models.IntegerChoices):
        FACTORY = 0, 'Завод'
        RETAIL = 1, 'Розничная сеть'
        SOLE_TRADER = 2, 'Индивидуальный предприниматель'

    name = models.CharField(
        verbose_name='Название',
        max_length=250,
        help_text='Укажите название поставщика'
    )

    supplier = models.ForeignKey(
        verbose_name='Поставщик',
        to='self',
        on_delete=models.DO_NOTHING,
        related_name='suppliers',
        help_text='Укажите связанного поставщика предыдущего по иерархии',
        null=True,
        blank=True
    )

    supplier_type = models.PositiveSmallIntegerField(
        verbose_name='Тип поставщика',
        choices=SupplierType,
        default=SupplierType.FACTORY,
        help_text='Укажите тип поставщика'
    )
    debt = models.DecimalField(
        verbose_name='Сумма долга с копейками',
        decimal_places=2,
        max_digits=12,
        help_text='Укажите сумму долга с копейками'
    )

    created_at = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Дата и время изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.name} - {self.SupplierType}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    supplier = models.ManyToManyField(
        verbose_name='Поставщик',
        to='Supplier',
        related_name='products',
        help_text='Укажите поставщика',


    )

    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Укажите название продукта'
    )

    model = models.CharField(
        verbose_name='Модель',
        max_length=100,
        help_text='Укажите модель'
    )

    release_date = models.DateField(
        verbose_name='Дата выхода продукта на рынок',
        help_text='Укажите дату выхода продукта на рынок'
    )

    def __str__(self):
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contact(models.Model):
    supplier = models.OneToOneField(
        verbose_name='Поставщик',
        to='Supplier',
        on_delete=models.CASCADE,
        related_name='contacts',
        help_text='Укажите поставщика'
    )

    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=250,
        help_text='Укажите электронную почту'
    )

    country = models.CharField(
        verbose_name='Страна',
        max_length=150,
        help_text='Укажите страну'
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=150,
        help_text='Укажите город'
    )

    street = models.CharField(
        verbose_name='улица',
        max_length=250,
        help_text='Укажите улицу'
    )

    street_number = models.CharField(
        verbose_name='Номер дома',
        max_length=30,
        help_text='Укажите номер дома'
    )

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street} {self.street_number} ({self.email})'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
