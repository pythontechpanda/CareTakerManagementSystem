from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.


@login_required(login_url="/admin-panel/")
def Dasboard(request):    
    return render(request, "admin_temp/index.html")


def LoginPage(request):        
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(username=email, password=pwd)        

        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin-panel/index/')           
        else:
            messages.error(request, "Username or password incorrect")
            return redirect('/admin-panel/')   
    else:
        return render(request, "admin_temp/loginpage.html")
    

def logout_call(request):
    logout(request)
    return redirect('/admin-panel/')



@login_required(login_url="/admin-panel/")
def UserCreatePage(request):
    
    get_id = User.objects.all()
    total_ids = []
    
    for i in get_id:
        total_ids.append(i.id)
    get_lst_index = total_ids[-1]
    new_id =get_lst_index+1
    if request.method == "POST":
        abbrevi = request.POST['abbreviations']
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        stafid = request.POST["stafid"]
        role = request.POST["role"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        start_date = request.POST["start"]
        usrnm = fname+lname+str(stafid)
        usr = User(abbreviations=abbrevi,username=usrnm,first_name=fname, last_name=lname, staff_id=stafid, role_id=role,dob=dob, gender=gender, start_date=start_date, is_staff=True)
        usr.save()
        
        uplead1 = Employment(detail_of_id=usr.id)
        uplead1.save()
        
        uplead2= EqualityAndDiversity(detail_of_id=usr.id)
        uplead2.save()
        
        uplead3 = Regions(detail_of_id=usr.id) 
        uplead3.save()
        
        uplead4 = BankDetails(detail_of_id=usr.id)     
        uplead4.save()
        
        messages.error(request,"Your register successfully")
        return redirect(f'/admin-panel/edit-user/{ usr.id }')
    else:
        get_role = Role.objects.all()
        return render(request, "admin_temp/create-staff.html", {'new_id':new_id,'get_role':get_role})
    
@login_required(login_url="/admin-panel/")   
def UserInfo(request,id,empid,eadid,regid,bkid):
    get_usr = User.objects.get(id=id)
    get_emp = Employment.objects.get(id=empid)
    get_ead = EqualityAndDiversity.objects.get(id=eadid)
    get_reg = Regions.objects.get(id=regid)
    get_bk = BankDetails.objects.get(id=bkid)
    print(get_usr.staff_id)
    if request.method == "POST":
        payroll_group = request.POST['payroll']
        print(">>>>>>>",payroll_group)
        line_manager = request.POST["line_manager"]
        leave_allowance = request.POST["leave_allowance"]
        marital_status = request.POST["marital_status"]
        dependants = request.POST["dependants"]
        regions = request.POST.getlist('region')
        ni_number = request.POST["ni_number"]
        target_hours = request.POST["target_hours"]
        passport_no = request.POST["passport_no"]        
        visa_no = request.POST["visa_no"]
        visa_expiry_date = request.POST["visa_expiry_date"]
        driving_licence_no = request.POST["driving_licence_no"]
        mot_date = request.POST["mot_date"]
        preferred_travel_type = request.POST["preferred_travel_type"]        
        
        ethnicity = request.POST["ethnicity"]
        nationality = request.POST["nationality"]
        sexual_orientation = request.POST["sexual_orientation"]
        disability = request.POST["disability"]
        first_language = request.POST["first_language"]
        other_languages = request.POST["other_languages"]
        
        option = request.POST.getlist("option")
        
        account_info = request.POST["account_info"]
        
        
        uplead1 = Employment.objects.filter(id=empid, detail_of=get_usr)        
        print("find uplead1",uplead1)
        uplead1.update(payroll_group_id=payroll_group, line_manager_id=line_manager, leave_allowance=leave_allowance, marital_status=marital_status,dependants=dependants,ni_number=ni_number,target_hours=target_hours,passport_no=passport_no,visa_no=visa_no,visa_expiry_date=visa_expiry_date,driving_licence_no=driving_licence_no,mot_date=mot_date,preferred_travel_type=preferred_travel_type)
        
        print("Data Updated Successfully!!!!!!!!!!",uplead1)
        uplead2 = EqualityAndDiversity.objects.filter(id=eadid, detail_of=get_usr)        
        uplead2.update(ethnicity_id=ethnicity, nationality_id=nationality, sexual_orientation=sexual_orientation, disability=disability,first_language=first_language,other_languages=other_languages)
        
        uplead3 = Regions.objects.filter(id=regid, detail_of=get_usr)        
        uplead3.update(option=option)
        
        uplead4 = BankDetails.objects.filter(id=bkid, detail_of=get_usr)        
        uplead4.update(account_info=account_info)
        
        messages.error(request,"Your profile has been updated successfully")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        get_role = Role.objects.all()
        get_payroll = PayrollGroup.objects.all()
        usr = User.objects.filter(is_staff=True, is_superuser=False)
        ethic = Ethnicity.objects.all()
        country = Country.objects.all()
        lang = Language.objects.all()
        region = RegionsOption.objects.all()
        return render(request, "admin_temp/create-staff.html", {'get_role':get_role,'usr':usr,'get_usr':get_usr,'get_payroll':get_payroll,'ethic':ethic,'country':country,'lang':lang,'region':region})



def StaffTable(request):
    usr = User.objects.filter(is_staff=True, is_superuser=False)
    staff_data = []

    for user in usr:
        # Retrieve related data using foreign key relationships
        employment_id = Employment.objects.filter(detail_of=user).values_list('id', flat=True).first()
        equality_and_diversity_id = EqualityAndDiversity.objects.filter(detail_of=user).values_list('id', flat=True).first()
        regions_id = Regions.objects.filter(detail_of=user).values_list('id', flat=True).first()
        bank_details_id = BankDetails.objects.filter(detail_of=user).values_list('id', flat=True).first()

        staff_details = {
            'user_id': user.id,
            'employment_id': employment_id,
            'equality_and_diversity_id': equality_and_diversity_id,
            'regions_id': regions_id,
            'bank_details_id': bank_details_id,
        }

        staff_data.append(staff_details)
    print("staff_data: ",staff_data)
    
    mapped = zip(usr, staff_data)
    
    # for user, details in mapped:
    #     print(user.id, details['employment_id'], details['equality_and_diversity_id'], details['regions_id'], details['bank_details_id'])
    # emp = Employment.objects.all()
    # eqal = EqualityAndDiversity.objects.all()
    # reg = Regions.objects.all()
    # bank = BankDetails.objects.all()
    # print("emp : ", emp)
    return render(request, "admin_temp/staff-table.html", {"mapped":mapped})    #{"staff":usr,"staff_data":staff_data}




# Plan functionality
def Capacity(request):
    return render(request, "admin_temp/capacity.html")

def RegularVisits(request):
    return render(request, "admin_temp/regularvisits.html")

def Rounds(request):
    return render(request, "admin_temp/rounds.html")

def CAREbooster(request):
    current_day = datetime.today().strftime('%A') 
    print(current_day)
    return render(request, "admin_temp/CAREbooster.html", {'current_day':current_day})


def PlannedMedication(request):
    return render(request, "admin_temp/PlannedMedication.html")

def PlannedMonthlyHoursComparison(request):
    return render(request, "admin_temp/PlannedMonthlyHoursComparison.html")

def RegularCareHours(request):
    return render(request, "admin_temp/RegularCareHours.html")

def MobileUserVersion(request):
    return render(request, "admin_temp/MobileUserVersion.html")


def CheckInOutData(request):
    return render(request, "admin_temp/CheckInOutData.html")


def CheckInOutPositions(request):
    return render(request, "admin_temp/CheckInOutPositions.html")

def FormsTasks(request):
    return render(request, "admin_temp/FormsTasks.html")

def MedicationAdministration(request):
    return render(request, "admin_temp/MedicationAdministration.html")

def PlannedVsActual(request):
    return render(request, "admin_temp/PlannedVsActual.html")



