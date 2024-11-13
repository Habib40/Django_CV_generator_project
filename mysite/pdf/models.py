from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    summery = models.TextField(max_length=1000,null=False)
    degree = models.CharField(max_length=1000)
    school = models.CharField(max_length=1000)
    university = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    previouse_work = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.name
