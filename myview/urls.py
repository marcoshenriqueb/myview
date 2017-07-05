"""myview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from home.views import HomePageView, ProjectsPageView, SingleProjectPageView, ServicesPageView, CoursesPageView, LeadView, ContactView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^lead/$', LeadView.as_view(), name='lead'),
    url(r'^projetos/$', ProjectsPageView.as_view(), name='projects'),
    url(r'^projetos/(?P<id>[0-9]+)/$', SingleProjectPageView.as_view(), name='project'),
    url(r'^solucoes/$', ServicesPageView.as_view(), name='services'),
    url(r'^cursos/$', CoursesPageView.as_view(), name='courses'),
    url(r'^contato/$', ContactView.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)