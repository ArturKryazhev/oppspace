from django.urls import path
from . import views

app_name = 'brief'

urlpatterns = [
    path('',views.briefs, name = 'brief'),
]
