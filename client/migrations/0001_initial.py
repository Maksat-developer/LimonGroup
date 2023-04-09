# Generated by Django 4.2 on 2023-04-09 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Каталог Категория:')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, verbose_name='Ссылка:')),
            ],
            options={
                'verbose_name': 'Категория Каталога',
                'verbose_name_plural': 'Категория Каталогов',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='Полное имя')),
                ('contacts', models.CharField(max_length=200, verbose_name='Контакты')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('is_new', models.BooleanField(default=True, verbose_name='Новый клиент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Запись создана')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articul', models.CharField(max_length=200, verbose_name='Артикуль:')),
                ('colors', models.CharField(max_length=100, verbose_name='Цвет:')),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=4, verbose_name='Размер:')),
                ('image', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Изображение:')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество:')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.catalogcategory', verbose_name='Категория:')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
            },
        ),
    ]
