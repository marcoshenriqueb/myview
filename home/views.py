from django.views.generic.base import TemplateView
from projects.models import Project, ProjectCategory
from contents.models import Content
from clients.models import Client
from courses.models import Course
from services.models import Service, Solution

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

class ContactPageView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        content = {}
        for c in Content.objects.all():
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context
