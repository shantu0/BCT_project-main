# Generated by Django 5.0.8 on 2024-08-13 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Airecipe', '0002_recipe_delete_wishlistitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
