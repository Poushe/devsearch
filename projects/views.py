from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Project
from .form import ProjectForm, UserForm
from django.contrib.auth.decorators import login_required

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    page='simple projects'
    number=10
    projects=Project.objects.all()
    return render(request,'projects/projects.html',{'p':page, 'no':number, 'projects': projects})

def project(request, pk):
    projectObj=Project.objects.get(id=pk)
    tags=projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'projectObj': projectObj })
@login_required(login_url='login')
def project_form(request):
    if request.method=='POST':
        print(request.POST)
        Form=ProjectForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            return redirect('projects')
    pfrom=ProjectForm()
    context={'form':pfrom}
    return render(request, 'projects/project-form.html',context)

def user_form(request):
    if request.method=='POST':
        print(request.POST)
        Form=UserForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('projects')
    pfrom1=UserForm()
    context={'form':pfrom1}
    return render(request, 'projects/user-form.html',context)

@login_required(login_url='login')
def update_project(request,pk):
    project_data=Project.objects.get(id=pk)
    pfrom=ProjectForm(instance=project_data)
    if request.method=='POST':
        print(request.POST)
        Form=ProjectForm(request.POST, request.FILES, instance=project_data)
        if Form.is_valid():
            Form.save()
            return redirect('projects')
    context={'form':pfrom}
    return render(request, 'projects/project-form.html',context)

@login_required(login_url='login')
def delete_project(request,pk):
    project=Project.objects.get(id=pk)
    context={'object':project}
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_tem.html', context)

@login_required(login_url='login')
def projectlistedit(request):
    projectlist=Project.objects.all()
    context={'projectlist':projectlist}
    return render(request,'projects/projectlist.html',context)
