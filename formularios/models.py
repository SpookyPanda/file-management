from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

def get_image_path(instance, filename):
	ext = filename.split('.')[-1]
	filename =  "%s.%s"%(instance.user_info.id,ext)
	return os.path.join('photos',str(instance.user_info.username),filename)

class userinfo(models.Model):
	user_info = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to=get_image_path,blank=True)

	def __str__(self):
		return self.user_info.username