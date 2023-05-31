# Generated by Django 4.1.7 on 2023-05-31 14:37

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_uz', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('video', models.URLField()),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='LidersImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Repair', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='polls.liders')),
            ],
        ),
    ]