
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('dash/', views.dash, name="dash" ),
    path('login/', views.loginPage, name ='login'),
    path('logoutuser/', views.logoutUser, name='logoutUser'),
    path('logout/', views.logoutSuccess, name='logout'),
]
