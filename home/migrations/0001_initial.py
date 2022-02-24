# Generated by Django 4.0.2 on 2022-02-24 08:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(2, 'AUTHOR'), (3, 'CUSTOMER'), (1, 'ADMIN')], default=1, max_length=50)),
                ('profile_pic', models.ImageField(upload_to='uploads/profile_pic/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_bio', models.CharField(max_length=250, null=True)),
                ('author_gender', models.CharField(max_length=10)),
                ('author_dob', models.DateField()),
                ('author_mobile_no', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, null=True)),
                ('book_isbn', models.PositiveIntegerField()),
                ('publication_date', models.DateField(null=True)),
                ('book_reading_age', models.CharField(max_length=100, null=True)),
                ('book_weight', models.CharField(max_length=100, null=True)),
                ('book_dimensions', models.CharField(max_length=100, null=True)),
                ('book_origin', models.CharField(max_length=50, null=True)),
                ('book_status', models.BooleanField(default=True)),
                ('book_description', models.CharField(max_length=250, null=True)),
                ('book_image', models.ImageField(default='static/images/default-img.png', null=True, upload_to='uploads/book-cover-images/')),
                ('book_volume', models.CharField(max_length=50, null=True)),
                ('book_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.bookcategory')),
                ('book_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.booklanguage')),
                ('book_publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.bookauthor')),
            ],
        ),
    ]
