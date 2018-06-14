from django.db import models
from accounts.models import User
from stubit1.choices import *

# Create your models here.
class Note(models.Model):
    # title of the paper uploaded
    title = models.CharField(max_length=500)

    # for which branch the paper is uploaded
    branch = models.CharField(max_length=5, choices=branch_choices, default='CSE')

    # for which semester paper is uploaded
    semester = models.IntegerField(choices=semester_choices, default=1)

    # sunject of the paper
    subject = models.CharField(max_length=250)

    # date of uploading
    date = models.DateTimeField(auto_now_add=True)

    # slug of the paper

    # in which year this paper has come
    year = models.IntegerField(choices=year_choices, default='')

    # in which time period this paper has come midsem or endsem
    time_period = models.CharField(max_length=6, choices=time_period_choices, default='midsem')

    # who uploaded the paper
    uploaded_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

    # add in file later
    file = models.FileField(null=True, blank=True, upload_to='files')

    def __str__(self):
        return self.title
