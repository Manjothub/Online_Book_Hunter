from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *


def INDEX(request):
    books = Book.objects.all()
    context ={
        'books':books
    }
    return render(request,'user/index.html',context)

@login_required(login_url = 'login')
def ADMIN_DASHBOARD(request):
    user = CustomUser.objects.get(id=request.user.id)
    context ={
        'user':user
    }
    return render(request,'admin/admin_dashboard.html',context)

def LOGINPAGE(request):
    return render(request,'common/login.html')

def DOLOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username=username, password=passw)
        if user is not None:
            login(request,user)
            user_type=user.user_type
            if user_type == '1':
                return redirect('dashboardadmin')
            elif user_type =='2':
                return redirect('dashboardstudent')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('loginpage')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('loginpage')
        
       
def DOLOGOUT(request):
    logout(request)
    return redirect('loginpage')


def CONTACT(request):
    return render(request,'user/contact.html')


@login_required(login_url = 'login')
#Admin Functions Starts Here
def ADDBOOK (request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_isbn = request.POST.get('book_isbn')
        publish_date = request.POST.get('publish_date')
        author_name = request.POST.get('author_name')
        book_category = request.POST.get('category')
        book_main_category = request.POST.get('main_category')
        book_sub_category = request.POST.get('sub_category')
        book_language = request.POST.get('language')
        reading_age = request.POST.get('reading_age')
        book_weight = request.POST.get('weight')
        book_image = request.FILES['cover_image']
        book_dimensions = request.POST.get('dimensions')
        book_volume = request.POST.get('volume')
        book_origin = request.POST.get('origin')
        book_desc = request.POST.get('description')
        book_price = request.POST.get('price')
        checkbox = request.POST.get('check') == 'on'
        author = BookAuthor(
            author_name = author_name
        )
        author.save()
        
        categorys = BookCategory.objects.get(id =book_category)
        
        maincategory = MainCategory(
            main_category = categorys,
            name = book_main_category
        )
        maincategory.save()
        
        
        price = BookPrice(
            price = book_price
        )
        price.save()
       
        language = BookLanguage(
            language = book_language
        )
    
        language.save()
        
        book = Book(
            book_name = book_name,
            book_isbn = book_isbn,
            publisher = author,
            text = language,
            publication_date = publish_date,
            book_reading_age = reading_age,
            book_weight = book_weight,
            book_dimensions = book_dimensions,
            book_origin = book_origin,
            category = categorys,
            main_category = maincategory,
            book_status = checkbox,
            book_description = book_desc,
            book_image = book_image,
            book_volume = book_volume,
            bookprice = price,
        )
        
        book.save()
        if book is not None:
            messages.success(request,'Book Added')
            return redirect('viewbook')
        else:
            messages.error(request,'Something went wrong')
            return redirect('addbook')
    categories = BookCategory.objects.all()
    context ={
        'categories':categories
    }
    return render(request,'admin/add_book.html',context)

@login_required(login_url = 'login')
def VIEWBOOKS(request):
    books = Book.objects.all()
    context ={
        'books':books
    }
    return render(request,'admin/view_books.html',context)

@login_required(login_url = 'login')
def VIEWAUTHORS(request):
    books = Book.objects.all()
    context ={
        'books':books
    }
    return render(request,'admin/authors_list.html',context)

@login_required(login_url = 'login')
def ADDCATEGORIES(request):
    if request.method == 'POST':
        name = request.POST.get('categoryname')
        category = BookCategory(
            category_name = name
        )
        if category is not None:
            category.save()
            messages.success(request,'Category Added')
        else:
            messages.error(request,'Fields needs to be checked')
    return render(request,'admin/add_categories.html')

@login_required(login_url = 'login')
def VIEWCATEGORIES(request):
    books = Book.objects.all()
    context ={
        'books':books
    }
    return render(request,'admin/view_categories.html',context)

@login_required(login_url = 'login')
def EDITBOOKS(request,id):
    books = Book.objects.filter(id=id)
    context ={
        'books':books
    }
    return render(request,'admin/edit_book.html',context)

@login_required(login_url = 'login')
def UPDATEBOOKS(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        isbn = request.POST.get('book_isbn')
        publish_date = request.POST.get('publication_date')
        author_name = request.POST.get('book_publisher')
        category = request.POST.get('book_category')
        language = request.POST.get('book_language')
        reading_age = request.POST.get('book_reading_age')
        weight = request.POST.get('book_weight')
        dimensions = request.POST.get('book_dimensions')
        volume = request.POST.get('book_volume')
        image = request.FILES['book_image']
        origin = request.POST.get('book_origin')
        price = request.POST.get('book_price')
        desc = request.POST.get('book_description')
        available = request.POST.get('book_status') =='on' 
        authors = BookAuthor(
            author_name = author_name
        )
        authors.save()
        category = BookCategory(
            category_name = category
        )
        category.save()
        
        bookprice = BookPrice(
            price = price
        )
        bookprice.save()
        
        booklanguage = BookLanguage(
            language = language
        )
        
        booklanguage.save()
        
        books = Book(
            book_name = book_name,
            book_isbn = isbn,
            publisher = authors,
            text = booklanguage,
            publication_date = publish_date,
            book_reading_age = reading_age,
            book_weight = weight,
            book_dimensions = dimensions,
            book_origin = origin,
            category = category,
            book_status = available,
            book_description = desc,
            book_image = image,
            book_volume = volume,
            bookprice = bookprice,
        )
        books.save()
        if books is not None:
            messages.success(request,'Data Updated')
            return redirect('viewbook')
        else:
            messages.error(request, 'something went wrong')
            return redirect('editbook')
    return render(request,'admin/edit_book.html')

@login_required(login_url = 'login')
def DELETEBOOKS(request,id):
    books= Book.objects.get(id=id)
    books.delete()
    return redirect('viewbook')



@login_required(login_url = 'login')
def ISSUEBOOK(request):
    books = Book.objects.all()
    students = Student.objects.all()
    context ={
        'books':books,
        'students':students
    }
    if request.method == 'POST':
        book_name=request.POST.get('book_name')
        author_name=request.POST.get('author')
        student_id= request.POST.get('student_id')
        isbn_number = request.POST.get('isbn')
        book_volume = request.POST.get('volume')
        book_category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        books = Book.objects.get(id=book_name)
        student = Student.objects.get(id=student_id)
        issuebook = IssuedBook(
            student_name =student,
            book_name =books,
            isbn = isbn_number,
            Volume = book_volume,
            author_name = author_name,
            category = book_category,
            sub_category = sub_category,
        )
        if issuebook is not None:
            issuebook.save()
            # print(issuebook)
            messages.success(request,'Book Issued Sucessfully')
            return redirect('issuedbooks')
        else:
            messages.error(request,'Book Issued Failed')
            return redirect('dashboardadmin')   
    return render(request,'admin/issue_book.html',context)







def BOOKVIEWCATEGORY(request,items):
    if items == 0:
        categories = BookCategory.objects.all()
        books = Book.objects.all()
        context ={
            'categories' : categories,
            'books':books
            }

        return render(request,'user/category.html',context)
        
    books = Book.objects.filter(category=items)
    categories = BookCategory.objects.all()
    context ={
            'categories' : categories,
            'books':books
            }
    return render(request,'user/category.html',context)



def BOOKDETAIL(request,id):
    product = Book.objects.filter(id=id)
    context ={
        'product':product
    }
    return render(request,'user/product_detail.html',context)



def STUDENTREGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        branch = request.POST.get('branch')
        date_birth=request.POST.get('dob_student')
        gender=request.POST.get('gender')
        roll_no = request.POST.get('roll_no')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            passnotmatch = True
            return render(request, "user/student_registration.html", {'passnotmatch':passnotmatch})

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already Taken')
            return redirect('student_registration')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,username + 'Already Taken')
            return redirect('student_registration')
        else:
            user= CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=image,
                user_type=2
            )    
            user.set_password(password)
            user.save()
        student = Student.objects.create(user=user, phone=phone, branch=branch,student_dob=date_birth,gender=gender,roll_no=roll_no, image=image)
        if student is not None:
            student.save()
            messages.success(request,'Account Created Successfully')
            return redirect('loginpage')
        else:
            messages.error(request,'Some error occured')
            return redirect('student_registration')
    return render(request, "user/student_registration.html")

@login_required(login_url = 'login')
def STUDENT_DASHBOARD(request):
    user = CustomUser.objects.get(id=request.user.id)
    books = Book.objects.all().count()
    context ={
        "user":user,
        'books':books
    }
    return render(request,'user/home.html',context)


@login_required(login_url = 'login')
def STUDENTISSUEDBOOKS(request):
    return render(request,'user/issued_book.html')


@login_required(login_url = 'login')
def VIEWISSUEDBOOK(request):
    issuedBooks = IssuedBook.objects.all()
    print(issuedBooks)
    context ={
        'issuedBooks':issuedBooks
    }
    return render(request,'admin/issued_books.html',context)

def STUDENTISSUEDBOOKS(request):
    user = request.user
    student = Student.objects.filter(user=user)
    issuedBooks = IssuedBook.objects.filter(student_name=student[0])
    issuedBooksdata = IssuedBook.objects.filter(student_name=student[0]).count()
    context={
        'issuebooks':issuedBooks,
        'issuedata' :issuedBooksdata
    }
    return render(request,'user/issued_book.html',context)