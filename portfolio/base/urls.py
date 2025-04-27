from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name='index'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
