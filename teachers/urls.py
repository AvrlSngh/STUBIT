from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = 'teachers'

urlpatterns = [
    url(r'^$', views.teacher_dashboard, name = "teacher_dashboard"),
    url(r'^upload_paper/$', views.upload_paper, name = "upload_paper"),
    url(r'^upload_notes/$', views.upload_notes, name = "upload_notes"),
    url(r'^upload_links/$', views.upload_links, name = "upload_links"),
    ]
