from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ValidationError
from audiovisual.models import Client, Service, Equipament
from enterprise.models import Industry, IndustryService, Benefit
from solutions.models import Project
from academy.models import Course
from contents.models import Content
from .forms import ContactForm
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

class AudiovisualView(View):

    def get(self, request):
        context = {}
        context['clients'] = Client.objects.all()
        context['services'] = Service.objects.all()
        context['equipaments'] = Equipament.objects.all()
        context['form'] = ContactForm()
        context['formurl'] = 'audiovisual'
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'audiovisual.html', context)

    def post(self, request):
        context = {}
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Obrigado pelo contato!')
                send_mail(
                    'Contato Site MyView',
                    'Nome: %s, Email: %s, Telefone: %s, Mensagem: %s' % (
                        form.cleaned_data['name'],
                        form.cleaned_data['email'],
                        form.cleaned_data['phone'],
                        form.cleaned_data['message'],
                    ),
                    'myviewsolutions123@gmail.com',
                    ['joaovbalmeida@gmail.com', 'joaov_almeida@hotmail.com']
                )
                return HttpResponseRedirect(reverse('audiovisual'))
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
        context['form'] = form
        return TemplateResponse(request, 'audiovisual.html', context)

class EnterpriseView(View):
    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        context['industrys'] = Industry.objects.all()
        context['industryservices'] = IndustryService.objects.all()
        context['benefits'] = Benefit.objects.all()
        context['formurl'] = 'enterprise'
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'enterprise.html', context)

    def post(self, request):
        context = {}
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Obrigado pelo contato!')
                send_mail(
                    'Contato Site MyView',
                    'Nome: %s, Email: %s, Telefone: %s, Mensagem: %s' % (
                        form.cleaned_data['name'],
                        form.cleaned_data['email'],
                        form.cleaned_data['phone'],
                        form.cleaned_data['message'],
                    ),
                    'myviewsolutions123@gmail.com',
                    ['joaovbalmeida@gmail.com', 'joaov_almeida@hotmail.com']
                )
                return HttpResponseRedirect(reverse('enterprise'))
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
        context['form'] = form
        return TemplateResponse(request, 'enterprise.html', context)

class SolutionsView(TemplateView):
    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        context['projects'] = Project.objects.all()
        context['formurl'] = 'enterprise'
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'solutions.html', context)

    def post(self, request):
        context = {}
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Obrigado pelo contato!')
                send_mail(
                    'Contato Site MyView',
                    'Nome: %s, Email: %s, Telefone: %s, Mensagem: %s' % (
                        form.cleaned_data['name'],
                        form.cleaned_data['email'],
                        form.cleaned_data['phone'],
                        form.cleaned_data['message'],
                    ),
                    'myviewsolutions123@gmail.com',
                    ['joaovbalmeida@gmail.com', 'joaov_almeida@hotmail.com']
                )
                return HttpResponseRedirect(reverse('solutions'))
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
        context['form'] = form
        return TemplateResponse(request, 'solutions.html', context)

class AcademyView(View):

    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        context['courses'] = Course.objects.all()
        context['formurl'] = 'academy'
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'academy.html', context)

    def post(self, request):
        context = {}
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Obrigado pelo contato!')
                send_mail(
                    'Contato Site MyView',
                    'Nome: %s, Email: %s, Telefone: %s, Mensagem: %s' % (
                        form.cleaned_data['name'],
                        form.cleaned_data['email'],
                        form.cleaned_data['phone'],
                        form.cleaned_data['message'],
                    ),
                    'myviewsolutions123@gmail.com',
                    ['joaovbalmeida@gmail.com', 'joaov_almeida@hotmail.com']
                )
                return HttpResponseRedirect(reverse('academy'))
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
        context['form'] = form
        return TemplateResponse(request, 'academy.html', context)