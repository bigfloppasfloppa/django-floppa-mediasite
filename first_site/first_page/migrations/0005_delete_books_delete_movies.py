# Generated by Django 4.0.6 on 2022-07-19 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_page', '0004_movies'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
