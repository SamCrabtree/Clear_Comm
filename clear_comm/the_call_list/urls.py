
from django.urls import path
from . import views
from .views import LeadView, LeadDetails, AddLeadView, DeleteLeadView
urlpatterns = [
    path('', views.home, name="home" ),
    path('dash/', LeadView.as_view(), name="dash"),
    path('lead/<int:pk>', LeadDetails.as_view(), name="lead"),
    path('add_lead/', AddLeadView.as_view(), name="add_lead" ),
    path('lead/delete_lead/<int:pk>', DeleteLeadView.as_view(), name="delete_lead" ),
    path('login/', views.loginPage, name ='login'),
    path('logoutuser/', views.logoutUser, name='logoutUser'),
    path('logout/', views.logoutSuccess, name='logout'),
]
