from django.urls import path
from leadsApp import views

urlpatterns = [
    path('', views.getRoutes),
    path('leads/', views.getLeads),
    path('leads/<str:pk>/', views.getLead)
]
