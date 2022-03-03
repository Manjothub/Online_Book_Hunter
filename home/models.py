from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

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


class BookPrice(models.Model):
    price= models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return str(self.price)

    
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
    bookprice = models.ForeignKey(BookPrice,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.book_name)
    
    

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_dob = models.DateField(auto_now_add=False)
    gender= models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="uploads/profile-pic/")

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.roll_no)+']'

   
class IssuedBook(models.Model):
    student_name= models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    book_name= models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    author_name = models.CharField(max_length=200,null=True)
    isbn = models.CharField(max_length=13)
    Volume = models.CharField(max_length=50,null=True)
    category = models.CharField(max_length=100,null=True)
    sub_category = models.CharField(max_length=100,null=True)
    issued_date = models.DateField(auto_now=True)