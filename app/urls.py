from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.home, name=""),
    path("what-we-do/", views.what_we_do_page, name="what-we-do")
]