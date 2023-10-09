from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from developer.forms import DeveloperForm


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['app'] = "home"
        return context

class RegisterView(CreateView):
    template_name = 'registration/register.html'  # Créez ce template
    form_class = DeveloperForm
    success_url = reverse_lazy('login')