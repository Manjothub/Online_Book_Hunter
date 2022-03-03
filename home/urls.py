from django.urls import path
from home .views import *

urlpatterns = [
    path("",INDEX,name='index'),
    path('login',LOGINPAGE, name="loginpage"),
    path('doLogin/',DOLOGIN,name='doLogin'),
    path('doLogout',DOLOGOUT,name='doLogout'),
    path('contact',CONTACT,name='contactpage'),
    path("admin_dashboard",ADMIN_DASHBOARD,name="dashboardadmin"),
    
    #admin Urls
    path("add/book",ADDBOOK,name="addbook"),
    path("view/book",VIEWBOOKS,name="viewbook"),
    path("view/authors",VIEWAUTHORS,name="viewauthor"),
    path("add/categories",ADDCATEGORIES,name="addcategories"),
    path("view/categories",VIEWCATEGORIES,name="viewcategories"),
    path('edit/book/<int:id>',EDITBOOKS,name="editbook"),
    path('update/book/',UPDATEBOOKS,name="updatebook"),
    path('delete/book/<int:id>',DELETEBOOKS,name="deletebook"),
    path('issue/book',ISSUEBOOK,name="issuebook"),
    path("student/student_registration",STUDENTREGISTER, name="student_registration"),
        
    path('view/books/categorys/<int:items>/',BOOKVIEWCATEGORY,name = "viewbookscategory"),
    path('view/book_detail/<str:id>',BOOKDETAIL,name="bookdetials")
    
    ]
