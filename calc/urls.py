
from django.urls import path, include
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path('add/', add, name="add"),
    path("sub/", sub, name="sub"),
    path("mul/", mul, name="mul"),
    path("mystars/", userstars, name="mystars"),
    #path("mystars", MyStars.as_view(), name="mystars"),
]
