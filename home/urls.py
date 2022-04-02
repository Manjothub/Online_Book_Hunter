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
    path("edit/categories/<int:id>",EDITCATEGORIES,name="editcategories"),
    path("update/categories",UPDATECATEGORIES,name="updatecategories"),
    path("delete/categories/<int:id>",DELETECATEGORIES,name="deletecategories"),
    path('edit/book/<int:id>',EDITBOOKS,name="editbook"),
    path('update/book/',UPDATEBOOKS,name="updatebook"),
    path('delete/book/<int:id>',DELETEBOOKS,name="deletebook"),
    path('issue/book',ISSUEBOOK,name="issuebook"),
    path('issued/view/book',VIEWISSUEDBOOK,name="issuedbooks"),
    path('issued/delete/book<int:id>',DELETEISSUEDBOOK,name="deleteissuedbook"),
    path('view/request/books',VIEWREQUESTEDBOOKS,name="requestedbooks"),
    path('student/book/approve/<str:id>',STUDENTAPPROVEBOOK,name="bookapprove"),
    path('student/book/disapprove/<str:id>',STUDENTDISAPPROVEBOOK,name="bookdisapprove"),
    path('userlist' ,USERLIST,name="userlist"),
    path('userlist/delete/<int:id>',DELETESTUDENT,name="deletestudent"),
    
    
    
    path("student/student_registration",STUDENTREGISTER, name="student_registration"),
    path("student/dashboard",STUDENT_DASHBOARD, name="dashboardstudent"),   
    path('view/books/categorys/<int:items>/',BOOKVIEWCATEGORY,name = "viewbookscategory"),
    path('view/book_detail/<str:id>',BOOKDETAIL,name="bookdetials"),
    path('view/issued-books/',STUDENTISSUEDBOOKS,name="studentbookissued"),
    path('request/book/<int:id>',BOOKREQUEST,name="saverequest"),
    path('student/book_request_history/',BOOKREQUESTHISTORY,name ="bookrequesthistory"),
    path('student/profile/',STUDENTPROFILE,name ="studentprofile"),
    path('student/profile/update',STUDENTPROFILEUPDATE,name ="studentprofileupdate"),
    path('verify-email/<token>',VERIFYSTUDENT,name ="verifystudent"),
    path('addcomments/<int:id>',ADDCOMMENT,name ="addcomment"),
    path('addreview/<int:id>',ADDREVIEW,name ="addreview"),
    path('design',DESIGN,name="design")
    ]
