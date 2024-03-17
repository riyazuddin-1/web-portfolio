from django.http import HttpResponse
from django.template import loader
from .models import ProjectDetails, ProjectLinks

def projects(request):
    template = loader.get_template('projects/index.html')
    context = {
        'myprojects' : ProjectDetails.objects.all().values()
    }
    return HttpResponse(template.render(context, request))

def projectInfo(request, id):
    template = loader.get_template('projects/details.html')
    context = {
        'myproject': ProjectDetails.objects.get(id = id),
        'links': ProjectLinks.objects.filter(project_id = int(id)).order_by('id')
    }
    return HttpResponse(template.render(context, request))