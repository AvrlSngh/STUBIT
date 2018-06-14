from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Paper
from django.contrib.auth.decorators import login_required
from .filters import ListFilter


@login_required(login_url="/accounts/login/")
def papers_list(request):
    papers = Paper.objects.all().order_by('date')
    paper_filter = ListFilter(request.GET, queryset=papers)
    return render(request, 'papers/papers_list.html', {'papers': papers, 'filter': paper_filter})
