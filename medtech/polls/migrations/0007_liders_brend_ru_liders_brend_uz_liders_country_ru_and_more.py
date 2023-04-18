# Generated by Django 4.1.7 on 2023-04-18 06:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_banner_button_ru_banner_button_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='liders',
            name='brend_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='brend_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='country_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='country_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='model_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='model_uz',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='postavshik_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='postavshik_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='pulbirligi_ru',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='liders',
            name='pulbirligi_uz',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='liderscategories',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='liderscategories',
            name='name_uz',
            field=models.CharField(max_length=500, null=True),
        ),
    ]