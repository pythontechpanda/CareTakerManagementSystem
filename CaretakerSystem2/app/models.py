from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

class Role(models.Model):
    rol = models.CharField(max_length=200, unique=True)

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    staff_id = models.IntegerField(unique=True, null=True)
    abbreviations = models.CharField(max_length=300, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=300, null=True)
    start_date = models.DateField(null=True)
    
    
    
    
class RegionsOption(models.Model):
    data = models.CharField(max_length=200, unique=True)
    
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
    

