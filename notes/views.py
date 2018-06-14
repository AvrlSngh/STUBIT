from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Note
from django.contrib.auth.decorators import login_required
from .filters import ListFilter

@login_required(login_url="/accounts/login/")
def notes_list(request):
    notes = Note.objects.all().order_by('date')
    notes_filter = ListFilter(request.GET, queryset=notes)
    return render(request, 'notes/notes_list.html', {'notes': notes, 'filter':notes_filter})
