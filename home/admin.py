from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



class UserModel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(CustomUser,UserModel)

admin.site.register(Book)
admin.site.register(BookLanguage)
admin.site.register(BookCategory)
admin.site.register(BookPrice)
admin.site.register(BookAuthor)