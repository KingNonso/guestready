from django.urls import include, path
from django.views.generic import TemplateView

from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.index, name='index'),

]
