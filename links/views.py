from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Link
from django.contrib.auth.decorators import login_required
from .filters import ListFilter

@login_required(login_url="/accounts/login/")
def links_list(request):
    links = Link.objects.all().order_by('date')
    links_filter = ListFilter(request.GET, queryset=links)
    return render(request, 'links/links_list.html', {'links': links, 'filter': links_filter})
