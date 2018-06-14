from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = 'students'

urlpatterns = [
    url(r'^$', views.student_dashboard, name = "student_dashboard"),
    url(r'^(?P<slug>[\w-]+)/$', views.mynote_detail, name = "detail"),
    ]
