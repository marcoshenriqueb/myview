from django.views.generic.base import TemplateView
from projects.models import Project

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(home=1).order_by('order')
        return context

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

class SingleProjectPageView(TemplateView):
    template_name = "single_project.html"
        