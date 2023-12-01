from django.urls import path
from . import views

# URLConfs
urlpatterns = [
    path('', views.run_homepage)
]