from django.db import models

NULLABLE = {"blank": True, "null": True}


# Создание класса Категория
class Category(models.Model):
    objects = None
    name = models.CharField(
        max_length=255,
        verbose_name="Название категории",
    )
    description = models.TextField(verbose_name="Описание категории", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


# Создание класса продукт
class Product(models.Model):
    objects = None

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    image = models.ImageField(
        upload_to="products/", verbose_name="Фото продукта", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="products",
        null=True,
        blank=True
    )
    price = models.IntegerField(verbose_name="Цена продукта", **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", **NULLABLE)
    updated_at = models.DateField(verbose_name="Дата изменения", **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = "Продукт"  # Настройка для наименования одного объекта
        verbose_name_plural = "Продукты"  # Настройка для наименования набора объектов
        ordering = ["name", "category"]
