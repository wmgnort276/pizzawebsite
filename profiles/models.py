from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm, fields
from datetime import date
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image =models.ImageField(default="default.jpg",upload_to="profile_pictures")
    name = models.CharField(max_length=100,default='')
    number_phone = models.CharField(max_length=10,blank=False)
    address = models.CharField(max_length=500, blank=False)
    pub_date = models.DateField('Birthday',default=date.today)
    def __str__(self) :
        return f'{self.user.username}\'s Profile...'
    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['image','name','number_phone','address','pub_date']
