from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import ProjectViewSet

router=routers.DefaultRouter()

router.register(r'Project',ProjectViewSet)

urlpatterns = [
    path('',include(router.urls)),
]