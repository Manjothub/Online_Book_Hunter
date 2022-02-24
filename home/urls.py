from django.urls import path
from home .views import *

urlpatterns = [
    path("",INDEX,name='index'),
    path('login',LOGINPAGE, name="loginpage"),
    path('doLogin/',DOLOGIN,name='doLogin'),
    path('doLogout',DOLOGOUT,name='doLogout'),
    path('contact',CONTACT,name='contactpage'),
    path("admin_dashboard",ADMIN_DASHBOARD,name="dashboardadmin"),
    path("add/book",ADDBOOK,name="addbook")
    ]
