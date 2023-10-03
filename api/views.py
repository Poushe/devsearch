
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from projects.models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getAllproject(request):
    projects=Project.objects.all()
    serializer=ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleproject(request,pk):
    singleprojects=Project.objects.get(id=pk)
    serializer=ProjectSerializer(singleprojects, many=False)
    return Response(serializer.data)