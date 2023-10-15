from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime,timedelta
from . utils import student_verification_token
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

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
    
    def __str__(self):
        return self.author_name

class BookCategory(models.Model):
    category_name= models.CharField(max_length=100,null=True)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    
    def __str__(self):                           
        full_path = [self.category_name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.category_name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    

class BookLanguage(models.Model):
    language= models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.language
    
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
    category = models.ForeignKey(BookCategory, null=True, blank=True,on_delete=models.CASCADE)
    book_status = models.BooleanField(default= True)
    book_description = models.CharField(max_length=250, null=True)
    book_image = models.ImageField(upload_to = 'uploads/book-cover-images/',null=True,default="static/images/default-img.png")
    book_volume = models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.book_name)
    
    
    

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    customer_dob = models.DateField(auto_now_add=False)
    gender= models.CharField(max_length=10)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="uploads/profile-pic/")

    def __str__(self):
        return str(self.user) 
            
class RequestBook(models.Model):
    customer_name= models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    book_name= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    request_status = models.IntegerField(null=True,default=0)
    upto_date = models.DateField(auto_now_add=False,null=True)
    button_value=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.customer_name)
    

class IssuedBook(models.Model):
    customer_name= models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    book_name= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    issued_date = models.DateField(auto_now=True)
    date_return = models.DateField(auto_now_add=False,null=True)
    def __str__(self):
        return str(self.book_name) + str(self.customer_name)

class BookReview(models.Model):
    RATING_CHOICES = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )
    book_name= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    customer_name= models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    mesage = models.TextField(null=True)
    def __str__(self):
        return str(self.customer_name) + str(self.rating)
    

class BookComment(models.Model):
    bookname= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    customer_name= models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    cmnt_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(null=True)
    def __str__(self):
        return str(self.customer_name) + str(self.comment)