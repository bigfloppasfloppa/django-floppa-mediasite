# Generated by Django 4.0.6 on 2022-07-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page', '0002_alter_books_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
