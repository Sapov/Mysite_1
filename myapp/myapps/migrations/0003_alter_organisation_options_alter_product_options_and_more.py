# Generated by Django 4.1.3 on 2022-11-01 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0002_organisation_delete_bd_ur_lico_alter_product_length_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'ordering': ['name_ul'], 'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'единица заказа'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapps.organisation', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='telegram',
            field=models.CharField(help_text='Указать @ник', max_length=20, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='whatsapp',
            field=models.CharField(help_text='Указать наличие', max_length=20, verbose_name='WhatsApp'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color_model',
            field=models.CharField(choices=[('RGB', 'rgb'), ('CMYK', 'cmyk'), ('GREY', 'Greyscale'), ('LAB', 'lab')], help_text='Для корректной печати модель должна быть CMYK', max_length=10, verbose_name='Цветовая модель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.FloatField(default=0, help_text='Указывается в см.', verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='product',
            name='resolution',
            field=models.IntegerField(default=0, help_text='для баннера 72 dpi, для Пленки 150 dpi', verbose_name='Разрешение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.FloatField(default=0, help_text='Указывается в см.', verbose_name='Ширина'),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dostavka', models.CharField(max_length=100, verbose_name='Способ доставки')),
                ('status', models.CharField(max_length=100, verbose_name='Статус заказа')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapps.organisation', verbose_name='Организация')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapps.product', verbose_name='ПРодукт')),
            ],
        ),
    ]