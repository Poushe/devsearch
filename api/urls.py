from django.urls import path
from . import views

urlpatterns=[
    path('', views.getRoutes),
    path('projects/',views.getAllproject),
    path('singleproject/<str:pk>',views.getSingleproject),
]