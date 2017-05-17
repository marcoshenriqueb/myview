from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

class SingleProjectPageView(TemplateView):
    template_name = "single_project.html"
        