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
    path('customer/book/approve/<str:id>',CUSTOMERAPPROVEBOOK,name="bookapprove"),
    path('customer/book/disapprove/<str:id>',CUSTOMERDISAPPROVEBOOK,name="bookdisapprove"),
    path('userlist' ,USERLIST,name="userlist"),
    path('userlist/delete/<int:id>',DELETECUSTOMER,name="deletestudent"),
    
    
    
    path("customer/customer_registration",CUSTOMERREGISTER, name="student_registration"),
    path("customer/dashboard",CUSTOMER_DASHBOARD, name="dashboardstudent"),   
    path('view/books/categorys/<int:items>/',BOOKVIEWCATEGORY,name = "viewbookscategory"),
    path('view/book_detail/<str:id>',BOOKDETAIL,name="bookdetials"),
    path('view/issued-books/',CUSTOMERISSUEDBOOKS,name="studentbookissued"),
    path('request/book/<int:id>',BOOKREQUEST,name="saverequest"),
    path('customer/book_request_history/',BOOKREQUESTHISTORY,name ="bookrequesthistory"),
    path('customer/profile/',CUSTOMERPROFILE,name ="studentprofile"),
    path('customer/profile/update',CUSTOMERPROFILEUPDATE,name ="studentprofileupdate"),
    path('addcomments/<int:id>',ADDCOMMENT,name ="addcomment"),
    path('addreview/<int:id>',ADDREVIEW,name ="addreview"),
    path('design',DESIGN,name="design")
    ]
