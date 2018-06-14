from django.conf.urls import url
from . import views

app_name = 'papers'

urlpatterns = [
    url(r'^$', views.papers_list, name = "papers_list"),
    ]
