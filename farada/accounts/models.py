from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    SERVICES =(
        ('gp','General Podiatry '),
        ('spba','Sports Podiatry and Biomechanical Assessments'),
        ('foi','Foot Orthoses and Innersoles '),
        ('cf','Children’s Feet (Paediatrics)'),)
    is_provider = models.BooleanField(default=False)
    is_participant = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255,blank=True, null=True)
    dob = models.DateField(blank=True,null=True)
    ndis_number = models.CharField(max_length=255,blank=True, null=True)
    address = models.TextField()
    services =  MultiSelectField(choices=SERVICES,default='None')
    city = models.CharField(max_length=255,blank=True, null=True)
   
    def  __str__(self): 
        return self.username
