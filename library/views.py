from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import ProjectSerializer
from .models import Project
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all().order_by('id')
    serializer_class=ProjectSerializer