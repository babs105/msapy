from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_pic = models.ImageField(upload_to='profile/',null=True,blank=True,default="profile/Default.jpeg")

# User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])