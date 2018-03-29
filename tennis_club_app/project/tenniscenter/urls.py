from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('selection/', views.selection, name='selection'),
    path('join/', views.join, name='join'),
    path('aggregation/', views.aggregation, name='aggregation'),
    path('division/', views.division, name='division'),
    path('nestedaggregation/', views.nestedAggregation, name='nestedaggregation'),
    path('deletecascade/', views.deleteCascade, name='deletecascade'),
    path('deletestudentmember/', views.deleteNoCascade, name='deletestudentmember'),
    path('updateprogramtaught/', views.updateNumberOfPeople, name='updateprogramtaught'),
    
    
    
    
]