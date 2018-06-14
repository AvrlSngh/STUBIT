from django.db import models
from accounts.models import User
from stubit1.choices import *

# Create your models here.
# Have to create a unique model for links due to their functionality
class Link(models.Model):
    # title of the paper uploaded
    topic_of_link = models.CharField(max_length=500)

    # for which branch the paper is uploaded
    branch = models.CharField(max_length=5, choices=branch_choices, default='CSE')

    # for which semester paper is uploaded
    semester = models.IntegerField(choices=semester_choices, default=1)

    # sunject related to the link
    subject = models.CharField(max_length=250)

    # date of uploading
    date = models.DateTimeField(auto_now_add=True)

    # in which time period this paper has come midsem or endsem
    time_period = models.CharField(max_length=6, choices=time_period_choices, default='midsem')

    # who uploaded the paper
    uploaded_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

    # adress of the link
    link_address = models.CharField(max_length=1050)

    def __str__(self):
        return self.topic_of_link
