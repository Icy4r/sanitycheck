from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.display_interactions),
    path('add/', views.input_interactions),
    path('hello/', views.say_hello)
]