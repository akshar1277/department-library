from rest_framework import serializers

from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','Batch','Project_id','Project_type','Project_name','Abstract','Project_area','Langauge','Company_name','Leader_enroll','Leader_name','Leader_email','Internal_guide')