from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    video = models.URLField()

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    description = RichTextField()
    date = models.DateField()
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True)
    keyword = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'новости'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title


class Web(models.Model):
    logo = models.ImageField(upload_to='images/', blank=True)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'информация о сайте'
        verbose_name_plural = 'информация о сайте'


class Banner(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True)
    button = models.CharField(max_length=20)
    button_phone = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'баннер'
        verbose_name_plural = 'баннер'

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = RichTextField()

    def __str__(self):
        return self.question


class Partners(models.Model):
    logo = models.ImageField(upload_to='images/', blank=True)
    linkPartner = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'партнёры'
        verbose_name_plural = 'партнёры'

    def __str__(self):
        return self.linkPartner


class Request(models.Model):
    name = models.CharField(max_length=100)
    phon_number = models.CharField(max_length=20)
    message = models.TextField()
    organization = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'входящие письма'
        verbose_name_plural = 'входящие письма'

    def __str__(self):
        return self.name


class RequestCall(models.Model):
    name = models.CharField(max_length=100)
    phon_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'заказанные звонки'
        verbose_name_plural = 'заказанные звонки'

    def __str__(self):
        return self.name


class LidersCategories(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Категория рекламы'
        verbose_name_plural = 'Категория рекламы'

    def __str__(self):
        return self.name


class Liders(models.Model):
    category = models.ForeignKey(
        LidersCategories, on_delete=models.CASCADE, related_name='lider', blank=True, null=True)
    model = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    postavshik = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    description = RichTextField()
    instagram = models.URLField(max_length=500, blank=True, null=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/', blank=True)
    price = models.FloatField()
    pulbirligi = models.CharField(max_length=10)
    views = models.IntegerField(default=0)
    touch = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'рекламы'
        verbose_name_plural = 'рекламы'

    def __str__(self):
        return self.model


class LidersImage(models.Model):
    liders = models.ForeignKey(
        Liders, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class CategoryOborodvnya(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Категория Обородвинья'
        verbose_name_plural = 'Категория Обородвинья'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    category = models.ForeignKey(
        CategoryOborodvnya, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    model = models.CharField(max_length=500)
    views = models.IntegerField(default=0)
    touch = models.IntegerField(default=0)
    country = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = RichTextField()
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    price = models.FloatField()
    pulbirligi = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Обородвинья'
        verbose_name_plural = 'Обородвинья'

    def __str__(self):
        return self.model


class EquipmentImage(models.Model):
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='equipment_images',
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='images/', blank=True)


class CategoryReagents(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Категория Реагенты'
        verbose_name_plural = 'Категория Реагенты'

    def __str__(self):
        return self.name


class Reagents(models.Model):
    category = models.ForeignKey(
        CategoryReagents, on_delete=models.CASCADE, blank=True, null=True)
    model = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    releasedate = models.DateField()
    manufacturer = models.CharField(max_length=500)
    tests = models.IntegerField()
    supplier = models.CharField(max_length=100)
    price = models.FloatField()
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Реагенты'
        verbose_name_plural = 'Реагенты'

    def __str__(self):
        return self.title


class CategoryConsumables(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Категория Расходный материал'
        verbose_name_plural = 'Категория Расходный материал'

    def __str__(self):
        return self.name


class Consumables(models.Model):
    category = models.ForeignKey(
        CategoryConsumables, on_delete=models.CASCADE, blank=True, null=True)
    model = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    unit = models.IntegerField()
    manufacturer = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    price = models.FloatField()
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Расходный материал'
        verbose_name_plural = 'Расходный материал'

    def __str__(self):
        return self.title


class CategoryService(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Категория Сервис'
        verbose_name_plural = 'Категория Сервис'

    def __str__(self):
        return self.name


class Parts(models.Model):
    category = models.ForeignKey(
        CategoryService, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500)
    unit = models.IntegerField()
    manufacturer = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    price = models.FloatField()
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Запчасти'
        verbose_name_plural = 'Запчасти'

    def __str__(self):
        return self.title


class Repair(models.Model):
    category = models.ForeignKey(
        CategoryService, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=500)
    views = models.IntegerField(default=0)
    touch = models.IntegerField(default=0)
    organization = models.CharField(max_length=500)
    description = RichTextField()
    instagram = models.URLField(max_length=500, blank=True, null=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    price = models.FloatField()
    pulbirligi = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонт'

    def __str__(self):
        return self.title


class RepairImage(models.Model):
    Repair = models.ForeignKey(
        Repair, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
