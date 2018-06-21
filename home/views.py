from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ValidationError
from audiovisual.models import Client, Service, Equipament
from contents.models import Content
from .forms import LeadForm, ContactForm
import json

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class AudiovisualView(TemplateView):
    template_name = "audiovisual.html"

    def get_context_data(self, **kwargs):
        context = super(AudiovisualView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['services'] = Service.objects.all()
        context['equipaments'] = Equipament.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class EnterpriseView(TemplateView):
    template_name = "enterprise.html"

    def get_context_data(self, **kwargs):
        context = super(EnterpriseView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['services'] = Service.objects.all()
        context['equipaments'] = Equipament.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class SolutionsView(TemplateView):
    template_name = "solutions.html"

    def get_context_data(self, **kwargs):
        context = super(SolutionsView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['services'] = Service.objects.all()
        context['equipaments'] = Equipament.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class AcademyView(TemplateView):
    template_name = "academy.html"

    def get_context_data(self, **kwargs):
        context = super(AcademyView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['services'] = Service.objects.all()
        context['equipaments'] = Equipament.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context