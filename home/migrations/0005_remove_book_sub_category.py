# Generated by Django 4.0.2 on 2022-02-28 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_book_main_category_book_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='sub_category',
        ),
    ]