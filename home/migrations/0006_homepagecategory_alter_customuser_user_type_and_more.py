# Generated by Django 4.0.2 on 2022-03-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_book_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='static/images/default-img.png', null=True, upload_to='homepage/home-page-category-images/')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'CUSTOMER'), (1, 'ADMIN')], default=1, max_length=50),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]