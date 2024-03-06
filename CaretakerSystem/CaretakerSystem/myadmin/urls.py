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
    path('staff-contact/', views.StaffContact),
    path('staff-nok/', views.NOK_staff),
    path('staff-qualification/', views.StaffQualification),
    path('staff-equipment/', views.StaffEquipment),
    path('staff-schedule/', views.StaffSchedule),
    
    # Schedule Section
    path('list-view/', views.ListView),
    
    
    # Deliver Section
    path('mobile-user-version/', views.MobileUserVersion),
    
    # Monitor Section
    path('check-in-out-data/', views.CheckInOutData),
    path('check-in-out-positions/', views.CheckInOutPositions),
    path('forms-tasks/', views.FormsTasks),
    path('medication-administration/', views.MedicationAdministration),
    path('planned-vs-actual/', views.PlannedVsActual),
    
    # Finance Section 
    path('funders/', views.Funders),
    path('archived-funders/', views.ArchivedFunders),
    path('add-funders/', views.AddFunders),
    path('add-account/', views.FunderAccount),
    path('add-invoice/', views.FunderInvoices),
    # path('add-notes/', views.FunderNotes),
    path('finance-invoices/', views.FinanceInvoices),
    path('finance-account/', views.FinanceAccount),
    path('payroll-comparison/', views.PayrollComparison),
    path('sage-invoice-extract/', views.SageInvoiceExtract),
    # Finance Setting Section
    path('special-days/', views.SpecialDays),
    path('travel-types/', views.TravelTypes),
    
    # settings Section
    path('app-setting/', views.AppSetting),
    path('app-setting-Landing-call/', views.AppSettingLandingcall),
    path('app-setting-sms-massaging/', views.AppSettingSMSMassaging),
    path('app-setting-integration/', views.AppSettingIntegration),
    path('job-role/', views.JobRole),
    path('update-job-role/', views.EditJobRole),
    path('master-medication/', views.MasterMedication),
    path('note-categories/', views.NoteCategories),
    path('master-regions/', views.MasterRegions),
    path('master-service-type/', views.MasterServiceTypes),
    path('master-training-skills-qualification/', views.MasterTraingSkillQuali),
    path('master-visit-type/', views.MasterVisitType),
    path('update_visit_type_rates/', views.SetAdminRates),
    
]
