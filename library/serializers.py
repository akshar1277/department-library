from rest_framework import serializers

from .models import Project,Project_second

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','Batch','Project_id','Project_type','Project_name','Abstract','Project_area','Langauge','Company_name','Leader_enroll','Leader_name','Leader_email','Internal_guide','Poster_URL','Video_URL','Document_URL')

class Project_secondSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project_second
        fields=('id','Batch','Project_id','Project_type','Project_name','Abstract','Project_area','Langauge','Company_name','Leader_enroll','Leader_name','Leader_email','Internal_guide','Poster_URL','Video_URL','Document_URL')