from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('resume/<int:id>/',views.Resume,name='resume'),
    path('list',views.Profile_list,name='list'),
]
