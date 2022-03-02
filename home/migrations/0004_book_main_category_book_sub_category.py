# Generated by Django 4.0.2 on 2022-02-28 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_maincategory_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='main_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.maincategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.subcategory'),
        ),
    ]
