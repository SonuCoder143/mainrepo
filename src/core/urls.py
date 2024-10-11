
from django.contrib import admin
from django.urls import path,include
from user  import views as s



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include("user.urls")),
    path("",s.index)
]
