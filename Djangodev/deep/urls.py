from django.urls import path
from . import views
urlpatterns = [
   #localhost:8000/deep
   #localhost:8000/deep/order
    path('', views.all_deep , name='all_deep'),
   
    path('services/', views.services, name='services' ),
   
]