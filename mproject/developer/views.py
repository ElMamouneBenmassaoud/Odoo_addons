from django.shortcuts import render

# Create your views here.

from developer.models import Developer
from django.shortcuts import render, get_object_or_404


def index(request):
    context = {
        'developers': Developer.objects.all()
    }
    return render(request, 'developer/index.html', context)


def detail(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer/detail.html', {'developer': developer})