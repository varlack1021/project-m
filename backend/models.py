from django.db import models
from django.conf import settings
#We use the makemigrate command to update and or create our database
#Migrate keeps track of any changes and then applies those changes
# Create your models here.
class Video(models.Model):
	video_link = models.CharField(max_length=200)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)