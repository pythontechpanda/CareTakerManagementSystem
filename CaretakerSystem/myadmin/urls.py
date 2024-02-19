from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Dasboard),
    path('', views.LoginPage),
    path('logout/', views.logout_call),
    path('create-user/', views.UserCreatePage),
    path('edit-user/<int:id>/<int:empid>/<int:eadid>/<int:regid>/<int:bkid>/', views.UserInfo, name="staff_updt"),
    
]
