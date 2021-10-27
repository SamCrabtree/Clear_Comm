
from django.urls import path
from . import views
from .views import LeadView, LeadDetails
urlpatterns = [
    path('', views.home, name="home" ),
    path('dash/', LeadView.as_view(), name="dash"),
    path('lead/<int:pk>', LeadDetails.as_view(), name="lead"),
  #  path('dash/', views.dash, name="dash" ),
    path('login/', views.loginPage, name ='login'),
    path('logoutuser/', views.logoutUser, name='logoutUser'),
    path('logout/', views.logoutSuccess, name='logout'),
]
