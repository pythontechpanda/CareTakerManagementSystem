from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
import os
class Assessor(models.Model):
    data = models.CharField(max_length=200, unique=True)
class Role(models.Model):
    assessor = models.ForeignKey(Assessor, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=200, unique=True)
class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    staff_id = models.IntegerField(unique=True, null=True)
    abbreviations = models.CharField(max_length=300, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=300, null=True)
    start_date = models.DateField(null=True)
class RegionsOption(models.Model):
    data = models.CharField(max_length=200, unique=True)
class ServiceType(models.Model):
    data = models.CharField(max_length=200, unique=True)
class QualificationType(models.Model):
    data = models.CharField(max_length=200, unique=True)
    cost = models.CharField(max_length=200, unique=True)
    reminder = models.CharField(max_length=200, unique=True)
class VisitType(models.Model):
    data = models.CharField(max_length=200, unique=True)
class Visit(models.Model):
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    visittype = models.ForeignKey(VisitType, on_delete=models.CASCADE)
    data = models.CharField(max_length=200, unique=True)
class SubRegionsOption(models.Model):
    regions = models.ForeignKey(RegionsOption, on_delete=models.CASCADE)
    data = models.CharField(max_length=200, unique=True)
class NoteCategorie(models.Model):
    visible_via_mobile = models.BooleanField()
    category_type = models.JSONField(default=list, null=True)
    data = models.CharField(max_length=200, unique=True)
class Medication(models.Model):
    data = models.CharField(max_length=200, unique=True)
    pdf_link = models.URLField(max_length=500, unique=True)
class PayrollGroup(models.Model):
    group = models.CharField(max_length=300)
class Country(models.Model):
    country = models.CharField(max_length=100)
class Language(models.Model):
    language = models.CharField(max_length=100)
class Employment(models.Model):
    detail_of = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_info", null=True)
    payroll_group = models.ForeignKey(PayrollGroup, on_delete=models.CASCADE, null=True)
    line_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manager", null=True)
    leave_allowance = models.IntegerField(null=True)
    marital_status = models.CharField(max_length=100, null=True)
    dependants = models.IntegerField(null=True)
    ni_number = models.CharField(max_length=100, null=True)
    target_hours = models.CharField(max_length=100, null=True)
    passport_no = models.CharField(max_length=100, null=True)
    visa_no = models.CharField(max_length=100, null=True)
    visa_expiry_date = models.DateField(null=True)
    driving_licence_no = models.CharField(max_length=100, null=True)
    mot_date = models.DateField(null=True)
    preferred_travel_type = models.CharField(max_length=100, null=True)
class Ethnicity(models.Model):
    ethnic = models.CharField(max_length=100)
class EqualityAndDiversity(models.Model):
    detail_of = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE, null=True)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    sexual_orientation = models.CharField(max_length=100, null=True)
    disability = models.TextField(null=True)
    first_language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    other_languages = models.CharField(max_length=150, null=True)
class Regions(models.Model):
    detail_of = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.JSONField(default=list, null=True)
class BankDetails(models.Model):
    detail_of = models.ForeignKey(User, on_delete=models.CASCADE)
    account_info = models.JSONField(default=list, null=True)
class ContactInformation(models.Model):
    detail_of = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=150, null=True)
    type_of =  models.CharField(max_length=12, null=True)
    mobile = models.CharField(max_length=12, null=True)
class AddressInformation(models.Model):
    detail_of = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=250, null=True)
    address_line2 = models.CharField(max_length=250, null=True)
    town_city = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=150, null=True)
    post_code = models.CharField(max_length=150, null=True)
def filepath_certificate(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('certificate/', filename)
class Qualification(models.Model):
    detail_of = models.ForeignKey(User, on_delete=models.CASCADE)
    add_skills = models.CharField(max_length=150, null=True)
    license_no = models.CharField(max_length=150, null=True)
    planned_date = models.DateField(null=True)
    acquired_date = models.DateField(null=True)
    expires_date = models.DateField(null=True)
    pais = models.CharField(max_length=150, null=True)
    uplod_certificate = models.FileField(upload_to=filepath_certificate, null=True)