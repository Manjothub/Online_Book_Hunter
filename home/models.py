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
        (2,'STUDENT'),
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
    
    def __str__(self):
        return self.category_name
    
class MainCategory(models.Model):
    main_category = models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



    
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
    category = models.ForeignKey(BookCategory,on_delete=models.CASCADE,null=True)
    main_category = models.ForeignKey(MainCategory,on_delete=models.CASCADE,null=True)
    book_status = models.BooleanField(default= True)
    book_description = models.CharField(max_length=250, null=True)
    book_image = models.ImageField(upload_to = 'uploads/book-cover-images/',null=True,default="static/images/default-img.png")
    book_volume = models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.book_name)
    
    

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_email_verfied = models.BooleanField(default = False)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    student_dob = models.DateField(auto_now_add=False)
    gender= models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="uploads/profile-pic/")

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.roll_no)+']'
    
@receiver(post_save, sender=Student)
def send_token(sender, instance, created, **kwargs):
        if created:
            token=uuid.uuid4()
            useremail = instance.user.email
            instance.email_token = token   
            student_verification_token(useremail,token)
                
                
        
        




def expiry():
    return datetime.today() + timedelta(days=14)   
class IssuedBook(models.Model):
    student_name= models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    book_name= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    

    
    
class RequestBook(models.Model):
    student_name= models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    book_name= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    request_status = models.IntegerField(null=True,default=0)
    button_value=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.student_name)