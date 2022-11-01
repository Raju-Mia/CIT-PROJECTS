
from django.urls import path

from .import views

# this is rerect urls. 
urlpatterns = [
    path('index/', views.index, name="index"),
    path('all-student/', views.all_student, name="all_student"),
    path ('create-student/', views.create_student, name='create_student'),

    
]