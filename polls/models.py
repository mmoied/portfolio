import datetime
from time import timezone

from django.db import models
from enum import Enum

class work(models.Model):
    start = models.DateField('start date')
    end = models.DateField('end date')
    place = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    def __str__(self):
        return self.position + " " +self.place




class project(models.Model):
    start = models.DateField('start date')
    end = models.DateField('end date')
    name = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    photo = models.CharField(max_length= 2000)

    def __str__(self):
        return self.skills + " " + self.name
class Level(models.TextChoices):   # A subclass of Enum
    l1 = "level 1"
    l2 = 'level 2'
    l3 = 'level 3'
    l4 = 'level 4'
    l5 = 'level 5'
    l6 = 'intermediate'

class Type(models.TextChoices):   # A subclass of Enum
    lang='Language'
    web='Web/ Framework / App'
    har='Hard Skills'


class skills(models.Model):
    # types = ('learning','basic','intermediate','advanced','expert')
    level = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)
    type = models.CharField(
        max_length=40,
        choices=Type.choices , # Cho# ices is a list of Tuple
        default=Type.lang
    )
    def __str__(self):
        return  self.description + self.type


