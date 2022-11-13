from email.policy import default
from pickle import TRUE
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

# Create your models here.
PROJECT_TYPE=(
    ("UDP","UDP"),
    ("IDP","IDP"),
)

class Project(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    Batch=models.CharField(max_length=10,null=True)
    Project_id=models.CharField(max_length=15,null=True)
    Project_type=models.CharField(
        max_length=20,
        choices=PROJECT_TYPE,
        default="UDP",
        null=True
    )
    Project_name=models.CharField(max_length=100,null=True)
    Abstract=models.CharField(max_length=500,null=True)
    Project_area=models.CharField(max_length=200,null=True)
    Langauge=models.CharField(max_length=100,null=True)
    Company_name=models.CharField(max_length=100,null=True)
    Leader_enroll=models.IntegerField(null=True)
    Leader_name=models.CharField(max_length=50,null=True)
    Leader_email=models.EmailField(max_length = 254,null=True)
    Internal_guide=models.CharField(max_length=50,null=True)
    Poster_URL=models.URLField(max_length=200,null=True)
    Video_URL=models.URLField(max_length=200,null=True)
    Document_URL=models.URLField(max_length=200,null=True)

    def __str__(self):
        return self.Project_name

    class Meta:
        verbose_name = "Projects_2019-2020"
        verbose_name_plural = "Projects_2019-2020"

class Project_second(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    Batch=models.CharField(max_length=10,null=True)
    Project_id=models.CharField(max_length=15,null=True)
    Project_type=models.CharField(
        max_length=20,
        choices=PROJECT_TYPE,
        default="UDP",
        null=True
    )
    Project_name=models.CharField(max_length=100,null=True)
    Abstract=models.CharField(max_length=500,null=True)
    Project_area=models.CharField(max_length=200,null=True)
    Langauge=models.CharField(max_length=100,null=True)
    Company_name=models.CharField(max_length=100,null=True)
    Leader_enroll=models.IntegerField(null=True)
    Leader_name=models.CharField(max_length=50,null=True)
    Leader_email=models.EmailField(max_length = 254,null=True)
    Internal_guide=models.CharField(max_length=50,null=True)
    Poster_URL=models.URLField(max_length=200,null=True)
    Video_URL=models.URLField(max_length=200,null=True)
    Document_URL=models.URLField(max_length=200,null=True)
    
   

    def __str__(self):
        return self.Project_name

    class Meta:
        verbose_name = "Projects_2020-2021"
        verbose_name_plural = "Projects_2020-2021"


   

