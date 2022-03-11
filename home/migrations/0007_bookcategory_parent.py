# Generated by Django 4.0.2 on 2022-03-10 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_customuser_user_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='home.bookcategory'),
        ),
    ]
