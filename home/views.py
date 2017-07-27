from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ValidationError
from projects.models import Project, ProjectCategory
from contents.models import Content
from clients.models import Client
from courses.models import Course
from services.models import Service, Solution
from .forms import LeadForm, ContactForm
import json

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['projects'] = Project.objects.filter(home=1)
        context['services'] = Service.objects.all()
        context['solutions'] = Solution.objects.filter(home=1)
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class LeadView(View):
    def post(self, request):
        try:
            form = LeadForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Seu email foi adicionado a nossa newsletter!')
                send_mail(
                    'ENTRADA DE LEAD PARA MAILLING',
                    form.cleaned_data['email'],
                    'myviewsolutions123@gmail.com',
                    ['contato@myviewsolutions.com', 'thiago@myviewsolutions.com']
                )
            else:
                messages.add_message(request, messages.INFO, 'Digite um email válido, por favor.')
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos adicionar o email na newsletter, por favor tente novamente.')
        return HttpResponseRedirect(reverse('home') + '#contact')
    

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectsPageView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = ProjectCategory.objects.filter(projects__isnull=False).distinct()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class SingleProjectPageView(TemplateView):
    template_name = "single_project.html"
        
    def get_context_data(self, **kwargs):
        context = super(SingleProjectPageView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=kwargs['id'])
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class ServicesPageView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super(ServicesPageView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['solutions'] = Solution.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context


class CoursesPageView(TemplateView):
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesPageView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context


class ContactView(View):
    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return TemplateResponse(request, 'contact.html', context)

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
                    ['contato@myviewsolutions.com', 'thiago@myviewsolutions.com']
                )
                return HttpResponseRedirect(reverse('contact'))
        except Exception as e:
            messages.add_message(request, messages.INFO, 'Não conseguimos enviar a mensagem, por favor tente novamente.')
        context['form'] = form
        return TemplateResponse(request, 'contact.html', context)
