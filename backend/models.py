from django.db import models

#We use the makemigrate command to update and or create our database
#Migrate keeps track of any changes and then applies those changes
# Create your models here.
class Video(models.Model):
	video_link = models.CharField(max_length=200)