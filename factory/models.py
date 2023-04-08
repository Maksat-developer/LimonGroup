from django.db import models


class RawStuff(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Наименование')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт из склада'
        verbose_name_plural = 'Продукт из склада'


class Storage(models.Model):

    code = models.CharField(max_length=50, blank=True, null=True, verbose_name='Код')
    product = models.ForeignKey(RawStuff, on_delete=models.SET_NULL)
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Цвет')
    quantity = models.IntegerField(default=0, null=True, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, verbose_name='Сумма')
    data_purchase = models.DateField(verbose_name='Дата закупки')
    is_ready = models.BooleanField(default=True, verbose_name='')
    remainder = models.CharField(max_length=10, blank=True, null=True, verbose_name='Остаток')
    defect = models.IntegerField(default=0, blank=True, null=True, verbose_name='Брак')
    created_at = models.DateTimeField(verbose_name='')
    where_was_purchase = models.TextField(max_length=100, blank=True, null=True, verbose_name='Поставщик')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Склад-Сырье'
        verbose_name_plural = 'Склад-Сырье'


class SewingModel(models.Model):
    client = models.CharField(max_length=50, verbose_name='Клиент')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    material = models.CharField(max_length=50, verbose_name='Материал', blank=True, null=True)
    type = models.CharField(max_length=50, verbose_name='Тип модели')
    price_for_one = models.DecimalField(max_length=10, verbose_name='Цена за штуку')

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель'


class FabricCutting (models.Model):
    material = models.ForeignKey(Storage, on_delete=models.SET_NULL)
    model_id = models.ForeignKey(SewingModel, on_delete=models.SET_NULL)
    quantity_model_total = models.IntegerField(default=0, null=True)
    data_start_day = models.DateField(verbose_name='Дата начала')
    data_start_end = models.DateField(verbose_name='Дата окончания')

    def __str__(self):
        return self.material

    class Meta:
        verbose_name = 'Раскрой ткани'
        verbose_name_plural = 'Раскрой ткани'
