from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User

# Create your models here.
class time(models.Model):
    title = models.TextField(max_length=32)

    def __str__(self):
        return self.title


class task(models.Model):
    # title = models.TextField(max_length=250)
    desc = models.TextField(max_length=250)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    time_created = models.ForeignKey(time, on_delete = SET_NULL, null=True)
    def __str__(self):
       return self.title
    def __str__(self):
        return self.desc
    
    

