from django.urls import path
from . import views as v
urlpatterns = [
    path("create-user",v.createUser),
]
