from distutils.command.upload import upload
from django.db import models


# Create your models here.
class Pricing(models.Model):
    price_name = models.CharField(max_length=100,null=True,blank=True)
    price_description = models.TextField(null=True,blank=True)
    
class Trainers(models.Model):
    traine_name = models.CharField(max_length=255)
    traine_spec = models.CharField(max_length=255)
    traine_image = models.ImageField(upload_to='trainers')
    
    
        
    
    
    
    
class Booking(models.Model):
    t_name = models.CharField(max_length=255)
    t_email = models.EmailField()
    t_height = models.IntegerField()
    t_weight = models.IntegerField()
    # trainer_name = models.ForeignKey(Trainers,on_delete=models.CASCADE)
    booked_on = models.DateField(auto_now=True)