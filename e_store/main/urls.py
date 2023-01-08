from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('login', views.login_page, name='login')
]