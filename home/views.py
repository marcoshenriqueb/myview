from django.views.generic.base import TemplateView
from projects.models import Project, ProjectCategory
from contents.models import Content

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(home=1)
        content = {}
        for c in Content.objects.filter(page__name='Home'):
            content[c.key.lower().replace(" ", "_")] = c.text
        context['content'] = content
        return context

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectsPageView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = ProjectCategory.objects.filter(projects__isnull=False)
        return context

class SingleProjectPageView(TemplateView):
    template_name = "single_project.html"
        
    def get_context_data(self, **kwargs):
        context = super(SingleProjectPageView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=kwargs['id'])
        return context

class ServicesPageView(TemplateView):
    template_name = "services.html"