from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import ProjectSerializer,Project_secondSerializer
from .models import Project,Project_second
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all().order_by('id')
    serializer_class=ProjectSerializer
    http_method_names = ['get']

class Project_secondViewSet(viewsets.ModelViewSet):
    queryset=Project_second.objects.all().order_by('id')
    serializer_class=Project_secondSerializer
    http_method_names = ['get']