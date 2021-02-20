from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path("structure/",views.structure,name="structure"),
    path("contact/",views.contact,name="contact"),
    path("Home/FIR/",views.FIR,name="FIR"),
    path("signup/",views.handleSignUp,name="handleSignUp"),
    path("signup/",views.handleSignUp, name='handleSignUp'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path("signuperror/",views.signuperror,name="error"),
    path("loginerror/",views.loginerror,name="loginerror"),
   
]