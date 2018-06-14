from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required
from . import forms
from .models import MyNote

@login_required(login_url="/accounts/login/")
def student_dashboard(request):
    if request.method == 'POST':
        form = forms.CreateMyNotes(request.POST)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('students:student_dashboard')
    else:
        form = forms.CreateMyNotes()
    mynotes = MyNote.objects.all().order_by('date')
    return render(request, 'students/student_dashboard.html', {'form':form, 'mynotes':mynotes})

def mynote_detail(request, slug):
    mynote = MyNote.objects.get(slug=slug)
    return render(request, 'students/mynote_detail.html', {'mynote':mynote})
