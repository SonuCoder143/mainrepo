
from django.contrib import admin
from django.urls import path
from myauth import views as authi

urlpatterns = [
    path('',authi.register,name="register"),
    path('login',authi.login,name="login"),
    path('admin/', admin.site.urls),
]
