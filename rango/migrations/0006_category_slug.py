# Generated by Django 2.2.17 on 2021-02-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
