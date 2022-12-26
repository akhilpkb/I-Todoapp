from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('lstview/', views.TaskListView.as_view(), name='lstview'),
    path('dtlview/<int:pk>/', views.TaskDetailView.as_view(), name='dtlview'),
    path('uptview/<int:pk>/', views.TaskUpdateView.as_view(), name='uptview'),
    path('dltview/<int:pk>/', views.TaskDeleteView.as_view(), name='dltview'),
]
