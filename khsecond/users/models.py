from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    CHOICES = [
    ('Одежда', (
        (1, 'Блузы и рубашки'),
        (2, 'Боди'),
        (3, 'Брюки'),
        (4, 'Верхняя одежда'),
        (5, 'Свитеры, кардиганы'),
        (6, 'Джинсы'),
        (7, 'Нижнее бельё'),
        (8, 'Пиджаки, костюмы'),
        (9, 'Платья'),
        (10, 'Топы'),
        (11, 'Футболки'),
        (12, 'Худи и толстовки'),
        (13, 'Шорты, велосипедки'),
        (14, 'Юбки'),
        )
    ),
    ('Обувь', (
        (1, 'Балетки'),
        (2, 'Босоножки'),
        (3, 'Ботильоны'),
        (4, 'Ботинки'),
        (5, 'Вечерняя обувь'),
        (6, 'Казаки'),
        (7, 'Кроссовки, кеды'),
        (8, 'Сабо, мюли'),
        (9, 'Сандалии'),
        (10, 'Сапоги'),
        (11, 'Туфли'),
        )
    ),
    ('Аксессуары', (
        (1, 'Аксессуары для волос'),
        (2, 'Головные уборы'),
        (3, 'Очки'),
        (4, 'Перчатки и варежки'),
        (5, 'Украшения'),
        (6, 'Чехлы для телефонов'),
        (7, 'Шарфы'),
        )
    ),
    ('Сумки', (
        (1, 'Клатчи'),
        (2, 'Поясные сумки'),
        (3, 'Сумки с ручками'),
        (4, 'Сумки через плечо'),
        (5, 'Шопперы'),
        )
    ),
    ]
    type = models.CharField(max_length=255, choices=CHOICES, verbose_name="Type")
    photo = models.ImageField(upload_to="images/", verbose_name="Image")
    size = models.CharField(max_length=255, verbose_name="Size")
    color = models.CharField(max_length=255, verbose_name="Color")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    material = models.CharField(max_length=255, verbose_name="Material")
    brand = models.CharField(max_length=255, null=True, verbose_name="Brand")


class CustomUser(AbstractUser):
    pass
