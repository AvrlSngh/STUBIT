from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.db import transaction
from .models import Student, User
from stubit1.choices import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(max_length=254, help_text='Required a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
                    'username',
                    'email',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = False
        user.save()
        student = Student.objects.create(user=user)
        student.first_name = self.cleaned_data['first_name']
        student.last_name = self.cleaned_data['last_name']
        return user
