from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import datetime
from django.utils import timezone

# Create your models here.
# title - depends on user, could be what muscle group hit that day or the session count
# body - will contain exercises, sets, and reps (for now will be a single input)
    # could separate into a different model
# add pub_date for time sorting later on
class Entry(models.Model):
        # for user-specific access to posts
    # profile = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 100)
    routine = models.CharField(max_length = 750)
    date = models.DateField('Publish Date', default=datetime.date.today())
        # this threw an error, will look into

    def __str__(self):
        return self.title
                # could do f"{self.title}" for format string, right now is okay

# more developed idea could be a different model that corresponds to the day