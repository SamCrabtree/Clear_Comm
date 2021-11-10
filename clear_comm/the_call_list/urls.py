
from django.urls import path
from . import views
from .views import LeadView, LeadDetails, AddLeadView, DeleteLeadView, UpdateLeadView, AddNoteView, LoopView, LoopDetailView, TentListView, AddLoopView, DeleteLoopView, UpdateTentView
urlpatterns = [
    #Homepage
    path('', views.home, name="home" ),

    #Dashboard
    path('dash/', TentListView.as_view(), name="dash"),
    path('dash/<int:pk>/update', UpdateTentView.as_view(), name="update_tent"),
    
    #Call List 
    path('call_list/', LeadView.as_view(), name='call_list'),

    #Leads
    path('add_lead/', AddLeadView.as_view(), name="add_lead" ),
    path('lead/<int:pk>', LeadDetails.as_view(), name="lead"),
    path('lead/<int:pk>/update', UpdateLeadView.as_view(), name="update_lead"),
    path('lead/<int:pk>/add_note/', AddNoteView.as_view(), name="add_note" ),
    path('lead/delete_lead/<int:pk>', DeleteLeadView.as_view(), name="delete_lead" ),
    
    #Loops
    path('loops/', LoopView.as_view(), name="loops"),
    path('add_loop/', AddLoopView.as_view(), name="add_loop" ),
    path('loop/<int:pk>', LoopDetailView.as_view(), name="loop"),
    path('lead/delete_loop/<int:pk>', DeleteLoopView.as_view(), name="delete_loop" ),

    #Login/Logouts
    path('login/', views.loginPage, name ='login'),
    path('logoutuser/', views.logoutUser, name='logoutUser'),
    path('logout/', views.logoutSuccess, name='logout'),
]
