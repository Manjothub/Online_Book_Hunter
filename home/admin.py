from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(CustomUser,UserModel)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name']



admin.site.register(BookLanguage)

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']


admin.site.register(BookAuthor)


admin.site.register(Student)

admin.site.register(IssuedBook)

@admin.register(RequestBook)
class RequestBookAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','book_name']
    
admin.site.register(BookReview)
admin.site.register(BookComment)