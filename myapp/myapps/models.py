from django.db import models

'''поля юля таблицы из бд
ORDERS - 
каждый примланный файл на печать будет иметь свой ордер.
order_id не пишeм'''



# база юридических лиц
#
class Organisation(models.Model):
    name_ul = models.CharField(max_length=70, verbose_name="Имя юр. лица")
    adress_ur = models.TextField(null=True, blank=True, verbose_name='Юр. Адрес')
    adress_post = models.TextField(null=True, blank=True, verbose_name='Почтовый Адрес')
    telefon = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    e_mail = models.EmailField(max_length=20, blank=True, verbose_name='Электронная почта')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    kpp = models.CharField(max_length=9, verbose_name='КПП')
    okpo = models.CharField(max_length=12, blank=True, verbose_name='ОКПО')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Организации'
        verbose_name = 'Организация'
        ordering = ['name_ul']

    def __str__(self):
        return self.name_ul


# база clients
class Clients(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    suname = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(max_length=20, verbose_name='Электронная почта')
    phone = models.CharField(max_length=17, verbose_name='Телефон')
    whatsapp = models.CharField(max_length=20, verbose_name='WhatsApp', help_text="Указать наличие")
    telegram = models.CharField(max_length=20, verbose_name='Telegram', help_text="Указать @ник")
    country = models.CharField(max_length=12, verbose_name='Страна')
    region = models.CharField(max_length=20, verbose_name='Регион')
    city = models.CharField(max_length=12, verbose_name='Город')
    category = models.CharField(max_length=12, verbose_name='Категория')
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT, verbose_name='Организация')

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиенты'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    COLOR_MODE = (
        ('RGB', 'rgb'),
        ('CMYK', 'cmyk'),
        ('GREY', 'Greyscale'),
        ('LAB', 'lab')
    )
    MATERIAL_TYPE = (
        ('banner_440', 'Баннер 440 гр.'),
        ('film', 'Пленка'),
        ('banner_510', 'Баннер 510 гр.'),
        ('setka', 'Сетка'),
        ('perfo', 'Перфопленка')
    )
    file_name = models.CharField(max_length=60, verbose_name='Имя файла')
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, verbose_name='order')
    material = models.CharField(max_length=20, choices=MATERIAL_TYPE, verbose_name='Материал',
                                help_text="Выбирите материал для печати")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    width = models.FloatField(default=0, verbose_name="Ширина", help_text="Указывается в см.")
    length = models.FloatField(default=0, verbose_name="Длина", help_text="Указывается в см.")
    resolution = models.IntegerField(default=0, verbose_name="Разрешение",
                                     help_text="для баннера 72 dpi, для Пленки 150 dpi")
    color_model = models.CharField(max_length=10, choices=COLOR_MODE, verbose_name="Цветовая модель",
                                   help_text="Для корректной печати модель должна быть CMYK")
    size = models.FloatField(default=0, verbose_name="Размер в Мб")
    price = models.FloatField(default=0, verbose_name="Стоимость")
    path_file = models.ImageField(upload_to='image/%y%m%d')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name_plural = 'единица заказа'
        verbose_name = 'Товар'
        # ordering = ['file_name']

class Orders(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT, verbose_name='Организация')
    dostavka = models.CharField(max_length=100, verbose_name="Способ доставки")
    status = models.CharField(max_length=100, verbose_name="Статус заказа")
    tovar = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='ПРодукт')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'

        # ordering = ['name']

    # def __str__(self):
    #     return self.name


