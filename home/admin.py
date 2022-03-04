from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



class UserModel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(CustomUser,UserModel)

admin.site.register(Book)

admin.site.register(BookLanguage)

@admin.register(BookCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']

admin.site.register(BookPrice)

admin.site.register(BookAuthor)


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','main_category','name']
    
    
admin.site.register(Student)

admin.site.register(IssuedBook)

@admin.register(RequestBook)
class RequestBookAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','book_name']