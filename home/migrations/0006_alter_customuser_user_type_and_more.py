# Generated by Django 4.0.2 on 2022-03-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'ADMIN'), (2, 'STUDENT')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='date_return',
            field=models.DateField(null=True),
        ),
    ]