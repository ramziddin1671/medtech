# Generated by Django 4.1.7 on 2023-05-10 17:37

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_uz', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('button', models.CharField(max_length=20)),
                ('button_uz', models.CharField(max_length=20, null=True)),
                ('button_ru', models.CharField(max_length=20, null=True)),
                ('button_phone', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'баннер',
                'verbose_name_plural': 'баннер',
            },
        ),
        migrations.CreateModel(
            name='CategoryConsumables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('name_uz', models.CharField(max_length=500, null=True)),
                ('name_ru', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Категория Расходный материал',
                'verbose_name_plural': 'Категория Расходный материал',
            },
        ),
        migrations.CreateModel(
            name='CategoryOborodvnya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('name_uz', models.CharField(max_length=500, null=True)),
                ('name_ru', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Категория Обородвинья',
                'verbose_name_plural': 'Категория Обородвинья',
            },
        ),
        migrations.CreateModel(
            name='CategoryReagents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('name_uz', models.CharField(max_length=500, null=True)),
                ('name_ru', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Категория Реагенты',
                'verbose_name_plural': 'Категория Реагенты',
            },
        ),
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('name_uz', models.CharField(max_length=500, null=True)),
                ('name_ru', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Категория Сервис',
                'verbose_name_plural': 'Категория Сервис',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('model', models.CharField(max_length=500)),
                ('model_uz', models.CharField(max_length=500, null=True)),
                ('model_ru', models.CharField(max_length=500, null=True)),
                ('views', models.IntegerField(default=0)),
                ('touch', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=100)),
                ('country_uz', models.CharField(max_length=100, null=True)),
                ('country_ru', models.CharField(max_length=100, null=True)),
                ('supplier', models.CharField(max_length=100)),
                ('supplier_uz', models.CharField(max_length=100, null=True)),
                ('supplier_ru', models.CharField(max_length=100, null=True)),
                ('brand', models.CharField(max_length=100)),
                ('brand_uz', models.CharField(max_length=100, null=True)),
                ('brand_ru', models.CharField(max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_uz', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('telegram', models.URLField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('price', models.FloatField()),
                ('pulbirligi', models.CharField(max_length=10)),
                ('pulbirligi_uz', models.CharField(max_length=10, null=True)),
                ('pulbirligi_ru', models.CharField(max_length=10, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.categoryoborodvnya')),
            ],
            options={
                'verbose_name': 'Обородвинья',
                'verbose_name_plural': 'Обородвинья',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('question_uz', models.CharField(max_length=500, null=True)),
                ('question_ru', models.CharField(max_length=500, null=True)),
                ('answer', ckeditor.fields.RichTextField()),
                ('answer_uz', ckeditor.fields.RichTextField(null=True)),
                ('answer_ru', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LidersCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('name_uz', models.CharField(max_length=500, null=True)),
                ('name_ru', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Категория рекламы',
                'verbose_name_plural': 'Категория рекламы',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('subtitle', models.CharField(max_length=500)),
                ('subtitle_uz', models.CharField(max_length=500, null=True)),
                ('subtitle_ru', models.CharField(max_length=500, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_uz', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('date', models.DateField()),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('keyword', models.CharField(max_length=500)),
                ('keyword_uz', models.CharField(max_length=500, null=True)),
                ('keyword_ru', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'новости',
                'verbose_name_plural': 'новости',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='images/')),
                ('linkPartner', models.URLField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'партнёры',
                'verbose_name_plural': 'партнёры',
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('views', models.IntegerField(default=0)),
                ('touch', models.IntegerField(default=0)),
                ('organization', models.CharField(max_length=500)),
                ('organization_uz', models.CharField(max_length=500, null=True)),
                ('organization_ru', models.CharField(max_length=500, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_uz', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('telegram', models.URLField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.categoryservice')),
            ],
            options={
                'verbose_name': 'Ремонт',
                'verbose_name_plural': 'Ремонт',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phon_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('organization', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'входящие письма',
                'verbose_name_plural': 'входящие письма',
            },
        ),
        migrations.CreateModel(
            name='RequestCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phon_number', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'заказанные звонки',
                'verbose_name_plural': 'заказанные звонки',
            },
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='images/')),
                ('address', models.CharField(max_length=500)),
                ('address_uz', models.CharField(max_length=500, null=True)),
                ('address_ru', models.CharField(max_length=500, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, max_length=500, null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('youtube', models.URLField(blank=True, max_length=500, null=True)),
                ('telegram', models.URLField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'информация о сайте',
                'verbose_name_plural': 'информация о сайте',
            },
        ),
        migrations.CreateModel(
            name='RepairImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Repair', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='polls.repair')),
            ],
        ),
        migrations.CreateModel(
            name='Reagents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=500)),
                ('model_uz', models.CharField(max_length=500, null=True)),
                ('model_ru', models.CharField(max_length=500, null=True)),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('releasedate', models.DateField()),
                ('manufacturer', models.CharField(max_length=500)),
                ('manufacturer_uz', models.CharField(max_length=500, null=True)),
                ('manufacturer_ru', models.CharField(max_length=500, null=True)),
                ('tests', models.IntegerField()),
                ('supplier', models.CharField(max_length=100)),
                ('supplier_uz', models.CharField(max_length=100, null=True)),
                ('supplier_ru', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('phone', models.CharField(max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.categoryreagents')),
            ],
            options={
                'verbose_name': 'Реагенты',
                'verbose_name_plural': 'Реагенты',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('unit', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=500)),
                ('manufacturer_uz', models.CharField(max_length=500, null=True)),
                ('manufacturer_ru', models.CharField(max_length=500, null=True)),
                ('organization', models.CharField(max_length=500)),
                ('organization_uz', models.CharField(max_length=500, null=True)),
                ('organization_ru', models.CharField(max_length=500, null=True)),
                ('price', models.FloatField()),
                ('phone', models.CharField(max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.categoryservice')),
            ],
            options={
                'verbose_name': 'Запчасти',
                'verbose_name_plural': 'Запчасти',
            },
        ),
        migrations.CreateModel(
            name='Liders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=500)),
                ('model_uz', models.CharField(max_length=500, null=True)),
                ('model_ru', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(max_length=100)),
                ('country_uz', models.CharField(max_length=100, null=True)),
                ('country_ru', models.CharField(max_length=100, null=True)),
                ('postavshik', models.CharField(max_length=100)),
                ('postavshik_uz', models.CharField(max_length=100, null=True)),
                ('postavshik_ru', models.CharField(max_length=100, null=True)),
                ('brend', models.CharField(max_length=100)),
                ('brend_uz', models.CharField(max_length=100, null=True)),
                ('brend_ru', models.CharField(max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_uz', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('telegram', models.URLField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.FloatField()),
                ('pulbirligi', models.CharField(max_length=10)),
                ('pulbirligi_uz', models.CharField(max_length=10, null=True)),
                ('pulbirligi_ru', models.CharField(max_length=10, null=True)),
                ('views', models.IntegerField(default=0)),
                ('touch', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lider', to='polls.liderscategories')),
            ],
            options={
                'verbose_name': 'рекламы',
                'verbose_name_plural': 'рекламы',
            },
        ),
        migrations.CreateModel(
            name='EquipmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_images', to='polls.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=500)),
                ('model_uz', models.CharField(max_length=500, null=True)),
                ('model_ru', models.CharField(max_length=500, null=True)),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('unit', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=500)),
                ('manufacturer_uz', models.CharField(max_length=500, null=True)),
                ('manufacturer_ru', models.CharField(max_length=500, null=True)),
                ('organization', models.CharField(max_length=500)),
                ('organization_uz', models.CharField(max_length=500, null=True)),
                ('organization_ru', models.CharField(max_length=500, null=True)),
                ('price', models.FloatField()),
                ('phone', models.CharField(max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.categoryconsumables')),
            ],
            options={
                'verbose_name': 'Расходный материал',
                'verbose_name_plural': 'Расходный материал',
            },
        ),
    ]
