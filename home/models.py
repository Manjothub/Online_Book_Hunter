from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    USER ={
        (1,'ADMIN'),
        (2,'CUSTOMER'),
    }
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='uploads/profile_pic/')


class BookAuthor(models.Model):
    author_name = models.CharField(max_length = 50,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class BookCategory(models.Model):
    category_name= models.CharField(max_length=100,null=True)
    
    
class BookPrice(models.Model):
    price= models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return str(self.price)

    

class BookLanguage(models.Model):
    language= models.CharField(max_length=100,null=True)
    
    
class Book(models.Model):
    book_name = models.CharField(max_length=100,null=True)
    book_isbn = models.PositiveIntegerField()
    publisher = models.ForeignKey(BookAuthor, on_delete=models.CASCADE,null=True)
    text = models.ForeignKey(BookLanguage, on_delete=models.CASCADE,null=True)
    publication_date = models.DateField(auto_now=False,null=True)
    book_reading_age = models.CharField(max_length=100,null=True)
    book_weight = models.CharField(max_length=100,null=True)
    book_dimensions = models.CharField(max_length=100,null=True)
    book_origin = models.CharField(max_length=50,null=True)
    category = models.ForeignKey(BookCategory,on_delete=models.CASCADE,null=True)
    book_status = models.BooleanField(default= True)
    book_description = models.CharField(max_length=250, null=True)
    book_image = models.ImageField(upload_to = 'uploads/book-cover-images/',null=True,default="static/images/default-img.png")
    book_volume = models.CharField(max_length=50,null=True)
    bookprice = models.ForeignKey(BookPrice,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.book_name)