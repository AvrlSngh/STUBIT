from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^teachers/', include('teachers.urls')),
    url(r'^papers/', include('papers.urls')),
    url(r'^notes/', include('notes.urls')),
    url(r'^links/', include('links.urls')),
    url(r'^about/$', views.about, name = "about"),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^contact/$', views.contact, name="contact"),
    ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
