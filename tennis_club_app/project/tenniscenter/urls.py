from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/selection/', views.selection, name='selection')
]