from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Dasboard),
    path('', views.LoginPage),
    path('logout/', views.logout_call),
    path('create-staff/', views.UserCreatePage),
    path('edit-user/<int:id>/<int:empid>/<int:eadid>/<int:regid>/<int:bkid>/', views.UserInfo, name="staff_updt"),
    # path('delete-staff/<int:id>/<int:empid>/<int:eadid>/<int:regid>/<int:bkid>/', views.StaffDelete, name="staff_del"),
    path('staff-table/', views.StaffTable, name="all-staff"),
    
    # Plan Section
    path('capacity/', views.Capacity),
    path('regular-visits/', views.RegularVisits),
    path('plan-rounds/', views.Rounds),
    path('care-booster/', views.CAREbooster),
    path('planned-medication/', views.PlannedMedication),
    path('planned-monthly-hours-comparison/', views.PlannedMonthlyHoursComparison),
    path('regular-care-hours/', views.RegularCareHours),
    
    # Deliver Section
    path('mobile-user-version/', views.MobileUserVersion),
    
    # Monitor Section
    path('check-in-out-data/', views.CheckInOutData),
    path('check-in-out-positions/', views.CheckInOutPositions),
    path('forms-tasks/', views.FormsTasks),
    path('medication-administration/', views.MedicationAdministration),
    path('planned-vs-actual/', views.PlannedVsActual),
]
