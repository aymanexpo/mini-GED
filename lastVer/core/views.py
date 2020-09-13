from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from .forms import DocsForm
from .models import Docs
import json


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def singup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/singup.html', {
        'form': form
    })


@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['Document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


class upload2(LoginRequiredMixin, TemplateView):
    template_name = 'upload.html'


def Docs_list(request):
    docs = Docs.objects.all()
    return render(request, 'Docs_list.html', {
        'docs': docs
    })


def upload_Docs(request):
    if request.method == 'POST':
        form = DocsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Docs_list')
    else:
        form = DocsForm()
    return render(request, 'upload_Docs.html', {
        'form': form
    })


def delete_Docs(request, pk):
    if request.method == 'POST':
        docs = Docs.objects.get(pk=pk)
        docs.delete()
    return redirect('Docs_list')


def showfile(request):
    if request.method == 'POST':
        fileid=request.POST.get('file_id')
        file = Docs.objects.get(id=fileid)
        print(file.pdf)
        data = '[{"url":"'+str(file.pdf)+'"}]'
        print(data)

        dumpurl = json.loads(data)
        return HttpResponse(json.dumps(dumpurl), content_type='application/json')

def todo(request):
    count = User.objects.count()
    return render(request, 'todo.html', {
        'count': count
    })