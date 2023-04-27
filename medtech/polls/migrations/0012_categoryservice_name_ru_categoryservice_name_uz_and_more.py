# Generated by Django 4.1.7 on 2023-04-19 07:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_categoryconsumables_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryservice',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='categoryservice',
            name='name_uz',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='manufacturer_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='manufacturer_uz',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='organization_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='organization_uz',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='title_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='title_uz',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='organization_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='organization_uz',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='title_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='title_uz',
            field=models.CharField(max_length=500, null=True),
        ),
    ]