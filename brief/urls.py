from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers
app_name = 'brief'

router = routers.DefaultRouter()
router.register(r'api-brief', BriefViewSet)
urlpatterns = [
    path('brief',views.briefs, name = 'brief'),
    path('test',views.test, name = 'test'),
    path('', include(router.urls))
    
]
