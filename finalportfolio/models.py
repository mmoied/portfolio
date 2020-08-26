import datetime
from time import timezone

from django.db import models

class Projects(models.Model):
	start = models.DateField('start date')
	end = models.DateField('end date')
	name = models.CharField(max_length=200)
	skills = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	ongoing = models.BooleanField(default=True)
	image = models.ImageField(upload_to="static/finalportfolio/images",default="image.jpeg")
