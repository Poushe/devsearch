from django.urls import path
from . import views

urlpatterns=[
    path('',views.projects,name="projects"),
    path('project/<str:pk>/',views.project, name='project'),
    path('projects/project-form',views.project_form,name='project-form'),
    path('projects/user-form',views.user_form,name='user-form'),
    path('projects/update-form/<str:pk>/',views.update_project,name='update-form'),
    path('projects/delete-form/<str:pk>/',views.delete_project,name='delete-form'),
    path('projects/projectlist',views.projectlistedit,name='projectlist'),
]