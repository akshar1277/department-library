from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import ProjectViewSet,Project_secondViewSet

router=routers.DefaultRouter()

router.register(r'Project_2019-20',ProjectViewSet)
router.register(r'Project_2020-21',Project_secondViewSet)

urlpatterns = [
    path('',include(router.urls)),
]