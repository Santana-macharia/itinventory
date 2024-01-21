from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# import datetime


class ITStaff(models.Model):
    staff_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # e_mail = models.EmailField(max_length=300)
    e_mail = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class MohiUser(models.Model):
    staff_id = models.CharField(max_length=50, unique=True)
    assignee_first_name = models.CharField(max_length=50)
    assignee_last_name = models.CharField(max_length=50)
    assignee_email_address = models.EmailField(max_length=300)
    
    def __str__(self):
        return self.assignee_email_address

class Centre(models.Model):
    centre_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    department_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Device(models.Model):
    device_name = models.CharField(max_length=100, unique=True)
    serial_number = models.CharField(max_length=100)
    system_model = models.CharField(max_length=100)
    # it_staff = models.ForeignKey(ITStaff, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(ITStaff, on_delete=models.CASCADE)
    assignee = models.ForeignKey(MohiUser, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
   
    CONDITION = (
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    )

    device_condition = models.CharField(max_length=100, choices=CONDITION)

    STATUS = (
        ('Issued', 'Issued'),
        ('Not Issued', 'Not Issued'),
        ('Returned', 'Returned'),
        
    )
    status = models.CharField(max_length=100, choices=STATUS)
    date = models.DateTimeField(default=timezone.now)
    # date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name
    
    
class PPM(models.Model):
    DEVICE = (
        ('PC', 'PC'),
        ('Monitor', 'Monitor'),
        ('Keyboard', 'Keyboard'),
        ('Printer', 'Printer'),
        ('UPS', 'UPS'),
    )
    device = models.CharField(max_length=100, choices= DEVICE)
    device_name = models.CharField(max_length=100, unique=True)
    serial_number = models.CharField(max_length=100)
    device_model = models.CharField(max_length=500)
    # it_staff = models.ForeignKey(ITStaff, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(ITStaff, on_delete=models.CASCADE)
    assignee = models.ForeignKey(MohiUser, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    ACTIVITIES = (
        ('Complete static dust extraction', 'Complete static dust extraction'),
        ('Internal Cleaning', 'Internal Cleaning'),
        ('Clean and inspect power supply', 'Clean and inspect power supply'),
        ('Cable ties and arrangement', 'Cable ties and arrangement'),
        ('Inspect for loose screws and corrosion', 'Inspect for loose screws and corrosion'),
        ('Detailed external cleaning', 'Detailed external cleaning'),
        ('System test and verification', 'System test and verification'),
        ('Check for software loaded in the PC', 'Check for software loaded in the PC'),
        ('Load the latest antivirus on the PC', 'Load the latest antivirus on the PC'),
        ('Clean and lubricate moving parts/gears', 'Clean and lubricate moving parts/gears'),
        ('Test printer, working properly', 'Test printer, working properly'),
        ('Returned', 'Returned'),
        
    )
    activities = models.CharField(max_length=500, choices=ACTIVITIES)
    issues = models.CharField(max_length=1000)
    recommendations = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    # date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name
    
    
   



