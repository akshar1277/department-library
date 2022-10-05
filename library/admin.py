from django.contrib import admin
from .models import Project,Project_second
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ProjectAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Batch','Project_id','Project_type','Project_name','Abstract','Project_area','Langauge','Company_name','Leader_enroll','Leader_name','Leader_email','Internal_guide']

class Project_secondAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Batch','Project_id','Project_type','Project_name','Abstract','Project_area','Langauge','Company_name','Leader_enroll','Leader_name','Leader_email','Internal_guide']


admin.site.register(Project,ProjectAdmin)
admin.site.register(Project_second,Project_secondAdmin)