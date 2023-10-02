from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
import json
from django.db.models import Q
from .forms import *
from django.db.models import Avg


def INDEX(request):
    books = Book.objects.all()
    context ={
        'books':books,

    }
    return render(request,'user/index.html',context)

@login_required(login_url = 'login')
def ADMIN_DASHBOARD(request):
    user = CustomUser.objects.get(id=request.user.id)
    students = Student.objects.all().count()
    booksdata = Book.objects.all().count()
    requestbook = RequestBook.objects.all().count()
    issuedbookdata = IssuedBook.objects.all().count()
    student_male = Student.objects.filter(gender = 'Male').count()
    student_female = Student.objects.filter(gender = 'Female').count()
    categorieslabels = BookCategory.objects.all().count()
    context ={
        'user':user,
        'students':students,
        'booksdata':booksdata,
        'requestbook':requestbook,
        'issuedbookdata':issuedbookdata,
        'student_male':student_male,
        'student_female':student_female,
        'categorieslabels':categorieslabels
    }
    return render(request,'admin/homepage.html',context)

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
                    cuser=CustomUser.objects.get(username=username)
                    stu=Student.objects.get(user=cuser)
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
        book_language = request.POST.get('language')
        reading_age = request.POST.get('reading_age')
        book_weight = request.POST.get('weight')
        book_image = request.FILES['cover_image']
        book_dimensions = request.POST.get('dimensions')
        book_volume = request.POST.get('volume')
        book_origin = request.POST.get('origin')
        book_desc = request.POST.get('description')
        checkbox = request.POST.get('check') == 'on'
        author = BookAuthor(
            author_name = author_name
        )
        author.save()
        
        categorys = BookCategory.objects.get(id =book_category)
        
       
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
            book_status = checkbox,
            book_description = book_desc,
            book_image = book_image,
            book_volume = book_volume,
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
        id = request.POST.get('category')
        try:
            sub_category = BookCategory.objects.get(id=id)
            category = BookCategory(
                category_name = name,
                parent=sub_category
            )
            if category is not None:
                if BookCategory.objects.filter(category_name=category).exists():
                    messages.warning(request,'Category is already Taken')
                    return redirect('addcategories')
                else:
                    category.save()
                    messages.success(request,'Category Added')
            else:
                messages.error(request,'Fields needs to be checked')
        except:
                category = BookCategory(
                category_name = name,   
            )
                category.save()
                messages.success(request,'Category Added')
    categories = BookCategory.objects.all()
    context ={
        'categories':categories
    }
    return render(request,'admin/add_categories.html',context)

@login_required(login_url = 'login')
def VIEWCATEGORIES(request):
    categories = BookCategory.objects.all()
    context ={
        'categories':categories
    }
    return render(request,'admin/view_categories.html',context)

def EDITCATEGORIES(request,id):
    categories = BookCategory.objects.get(id=id)
    context ={
        'categories':categories
    }
    return render(request,'admin/edit_categories.html',context)

def UPDATECATEGORIES(request):
    if request.method == 'POST':
        category = request.POST.get('category_name')
        categorytable = BookCategory(category_name =category)
        if categorytable is not None:
            categorytable.save()
            messages.success(request,'Category Updated Sucessfully')
            return redirect('viewcategories')
        else:
            messages.error(request,'Something went wrong')
    return render(request,'admin/edit_categories.html')

def DELETECATEGORIES(request,id):
    categories = BookCategory.objects.get(id=id)
    categories.delete()
    return redirect('viewcategories')


def USERLIST(request):
    students = Student.objects.all()
    context ={
        'students':students
    }
    return render(request,'admin/users_list.html',context)

def DELETESTUDENT(request,id):
    stud = Student.objects.get(id=id)
    stud.delete()
    return redirect('userlist')

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
        id= request.POST.get('book_id')
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
        
        
        booklanguage = BookLanguage(
            language = language
        )
        
        booklanguage.save()
        
        books = Book(
            id = id,
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
        )
        if books:
            messages.success(request,'Data Updated')
            books.save()
            return redirect('viewbook')
        else:
            messages.error(request,'Something went wrong')
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
            messages.success(request,'Book Issued Sucessfully')
            return redirect('issuedbooks')
        else:
            messages.error(request,'Book Issued Failed')
            return redirect('dashboardadmin')   
    return render(request,'admin/issue_book.html',context)


def BOOKVIEWCATEGORY(request,items):
    if items == 0:
        categories = BookCategory.objects.select_related().all()
        books = Book.objects.all()
        context ={
            'categories' : categories,
            'books':books,
            }
        for c in categories:
            print (c.parent)
        return render(request,'user/category.html',context)
    else:
        categories = BookCategory.objects.select_related().all()
    
        books = Book.objects.filter(category=items)
        context ={
            'books':books,
            'categories' : categories,
            }
        for c in categories:
            if c.parent is None:
                print ('no')
            else:
                print(c.parent)
    return render(request,'user/category.html',context)



def BOOKDETAIL(request,id):
    product = Book.objects.filter(id=id)
    products = Book.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        stu=Student.objects.get(user=user)
        show=RequestBook.objects.filter(Q(book_name=products) & Q(student_name=stu))
        cmnt = BookComment.objects.filter(bookname=products)
        form = UserReviewForm()
        userreview = BookReview.objects.filter(book_name=products)
        
    else:
         return render(request,'common/login.html')
    context ={
        'product':product,
        'show':show,
        'comments':cmnt,
        'form':form,
        'userreview':userreview

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
    students = Student.objects.get(user=user)
    issuedbooks = IssuedBook.objects.filter(student_name =students).count()
    requestedbook = RequestBook.objects.filter(student_name =students).count()
    context ={
        "user":user,
        'books':books,
        "requestedbook":requestedbook,
        "issuedbooks":issuedbooks
    }
    return render(request,'user/home.html',context)


@login_required(login_url = 'login')
def STUDENTISSUEDBOOKS(request):
    return render(request,'user/issued_book.html')


@login_required(login_url = 'login')
def VIEWISSUEDBOOK(request):
    issuedBooks = IssuedBook.objects.all()
    context ={
        'issuedBooks':issuedBooks,
    }
    return render(request,'admin/issued_books.html',context)

def DELETEISSUEDBOOK(request,id):
    bookissued = IssuedBook.objects.get(id=id)
    bookissued.delete()
    return redirect('issuedbooks')

@login_required(login_url = 'login')
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

def BOOKREQUEST(request,id):
    if request.method == 'POST':
            if request.user.is_authenticated:
                user = request.user
                student = Student.objects.get(user=user)
                book = Book.objects.get(id=id)
                date = request.POST.get('uptodate')
                bookrequest = RequestBook(
                    student_name = student,
                    book_name = book,
                    upto_date =date,
                    button_value=True
                )
                bookrequest.save()
                messages.success(request,'Book Requested')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return render(request,'common/login.html')
    return redirect('bookdetials')

def VIEWREQUESTEDBOOKS(request):
    requested_books = RequestBook.objects.all()
    context ={
        'requested_books':requested_books
    }
    return render(request,'admin/requested_books.html',context)


@login_required(login_url = 'login')
def STUDENTAPPROVEBOOK(request,id):
    bookrequests = RequestBook.objects.get(id=id)
    print(bookrequests)
    bookrequests.request_status = 1
    bookrequests.save()
    if bookrequests.request_status == 1:
        name = bookrequests.student_name
        book = bookrequests.book_name
        date = bookrequests.upto_date
        issue = IssuedBook(student_name =name,book_name=book,date_return=date)
        issue.save()
        messages.success(request,'Book Issued ')
    return redirect('requestedbooks')

@login_required(login_url = 'login')
def STUDENTDISAPPROVEBOOK(request,id):
    bookrequests = RequestBook.objects.get(id=id)
    bookrequests.request_status = 2
    bookrequests.save()
    messages.success(request,'Request Cancelled')
    return redirect('requestedbooks')

@login_required(login_url = 'login')
def BOOKREQUESTHISTORY(request):
    student = Student.objects.filter(user=request.user.id)
    for i in student:
        student_id = i.id
        student_book_request_history = RequestBook.objects.filter(student_name = student_id)
        context={
            'student_book_request_history':student_book_request_history
        }
    return render(request,'user/request_books_history.html',context)

def STUDENTPROFILE(request):
    return render(request,'user/user_profile.html')

def STUDENTPROFILEUPDATE(request):
    if request.method == 'POST':
        profilepic = request.FILES.get('profilepic')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        password = request.POST.get('password')
        studentdob = request.POST.get('dateofbirth')
        branch = request.POST.get('branch')
        roll_no = request.POST.get('rollnum')
        phone_no = request.POST.get('phonenum')
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name = firstname
            customuser.last_name = lastname
            customuser.profile_pic = profilepic
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            student = Student.objects.get(user = customuser)
            student.user = customuser
            student.student_dob = studentdob
            student.branch = branch
            student.roll_no = roll_no
            student.phone = phone_no
            student.save()
            messages.success(request,"Your Profile Updated Successfully")
            return redirect("studentprofile")
        except:
            messages.error(request,"Fail to update your Profile")
    return render(request,'user/edit_user_profile.html')

def VERIFYSTUDENT(request,token):
    try:
        students = Student.objects.get(email_token=token)
        students.is_email_verfied = True
        students.save()
        messages.success(request,'User Verfied')
        return redirect('loginpage')
    except Exception as e:
        return render(request,'common/errorpage404.html')

def ADDCOMMENT(request,id):
    if request.method =='POST':
        user = request.user
        student = Student.objects.get(user=user)
        book = Book.objects.get(id=id)
        msg = request.POST.get('message')
        cmnt = BookComment(
            bookname = book,
            studentname = student,
            comment = msg
        )
        cmnt.save()
        messages.success(request,'Comment Posted Sucessfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('bookdetails')
    
def ADDREVIEW(request,id):
    if request.method =='POST':
        user = request.user
        student = Student.objects.get(user=user)
        book = Book.objects.get(id=id)
        reviewmsg= request.POST.get('reviewmsg')
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.book_name =book
            review.student_name = student
            review.mesage = reviewmsg
            review.save()
            messages.success(request,'Review Added Sucessfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('bookdetails')
    
def DESIGN(request):
    return render(request,'common/design.html')