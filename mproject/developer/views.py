from django.shortcuts import render

# Create your views here.

from developer.models import Developer
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import DeveloperForm, TaskForm
from django.urls import reverse
from .models import Task
from django.views.generic import DetailView, ListView


class IndexView(ListView):
    model = Developer
    template_name = "developer/index.html"
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = DeveloperForm
        return context


class DevDetailVue(DetailView):
    model = Developer
    template_name = 'developer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm
        return context


def create(request):
    form = DeveloperForm(request.POST)

    if form.is_valid():
        Developer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('developer:index'))


def delete(request, pk):
    developer = get_object_or_404(Developer, pk=pk)
    developer.delete()
    return HttpResponseRedirect(reverse('developer:index'))


def addTask(request, pk):
    developer = get_object_or_404(Developer, pk=pk)
    form = TaskForm(request.POST)

    if form.is_valid():
        developer.tasks.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            # assignee=form.cleaned_data['assignee']
        )
        print("sdr ok")
    else:
        print(f"sdr : {form.errors}")
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('developer:index'))
