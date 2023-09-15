from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contact_viewset', Contact_usViewSet)
router.register(r'notifications_viewsets', NotificationsViewSet)
app_name = 'main'
urlpatterns = [
    # path('',views.main_page, name='main_page'),
    path('forms', views.Forms, name = 'forms'),
    path('', include(router.urls))
]
